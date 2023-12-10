from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, Mulher, Model
from logger import logger
from schemas import *
from flask_cors import CORS

# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
mulher_tag = Tag(name="mulher", description="Adição, visualização, remoção e predição de mulheres com Cancêr de Mama")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de listagem de mulheres
@app.get('/mulheres', tags=[mulher_tag],
         responses={"200": MulherViewSchema, "404": ErrorSchema})
def get_mulheres():
    """Lista todos os mulheres cadastrados na base
    Retorna uma lista de mulheres cadastrados na base.
    
    Args:
        nome (str): nome do mulher
        
    Returns:
        list: lista de mulheres cadastrados na base
    """
    session = Session()
    
    # Buscando todos os mulheres
    mulheres = session.query(Mulher).all()
    
    if not mulheres:
        logger.warning("Não há mulheres cadastradas na base :/")
        return {"message": "Não há mulheres cadastradas na base :/"}, 404
    else:
        logger.debug(f"%d mulheres encontradas" % len(mulheres))
        return apresenta_mulheres(mulheres), 200

# Rota de adição de mulher
@app.post('/mulher', tags=[mulher_tag],
          responses={"200": MulherViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: MulherSchema):
    """Adiciona um novo mulher à base de dados
    Retorna uma representação dos mulheres e diagnósticos associados.
    
    Args:
            name (str): nome da mulher
            rad_mean (float): média das distâncias do centro até os pontos na periferia (Representa a média das distâncias do centro até os pontos que formam o perímetro de uma célula)
            tex_mean (float): Textura (desvio padrão dos valores em escala de cinza): Refere-se à variação da intensidade dos tons de cinza na imagem da célula.
            perim_mean (float): Perímetro: É o comprimento total do contorno da célula.
            area_mean (float): Área: Representa a área total ocupada pela célula.
            smoo_mean (float): Suavidade (variação local nos comprimentos dos raios): Indica quão suave é a variação nos comprimentos dos raios da célula.
            comp_mean (float): Compacidade (perímetro^2 / área - 1.0): É uma medida que combina informações sobre o perímetro e a área da célula.
            concav_mean (float): Concavidade (gravidade das porções côncavas do contorno): Avalia a severidade das regiões côncavas na borda da célula.
            cp_mean (float): Pontos Côncavos (número de porções côncavas do contorno): Indica quantas regiões côncavas existem na borda da célula.
            sym_mean (float): Simetria: Avalia a simetria da célula.
            fd_mean (float): Dimensão Fractal ("aproximação de linha costeira" - 1): Uma medida da complexidade estrutural da célula, às vezes comparada à complexidade da linha costeira em geometria fractal.
        
    Returns:
        dict: representação do mulher e diagnóstico associado
    """
    
    # Carregando modelo
    ml_path = 'ml_model/cancer_mama_lr.pkl'
    modelo = Model.carrega_modelo(ml_path)
    
    mulher = Mulher(
        name=form.name.strip(),
        rad_mean=form.rad_mean,
        tex_mean=form.tex_mean,
        perim_mean=form.perim_mean,
        area_mean=form.area_mean,
        smoo_mean=form.smoo_mean,
        comp_mean=form.comp_mean,
        concav_mean=form.concav_mean,
        cp_mean=form.cp_mean,
        sym_mean=form.sym_mean,
        fd_mean=form.fd_mean,
        outcome=Model.preditor(modelo, form)
    )
    logger.debug(f"Adicionando mulher com nome: '{mulher.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se mulher já existe na base
        if session.query(mulher).filter(mulher.name == form.name).first():
            error_msg = "mulher já existente na base :/"
            logger.warning(f"Erro ao adicionar mulher '{mulher.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando mulher
        session.add(mulher)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado mulher de nome: '{mulher.name}'")
        return apresenta_mulher(mulher), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar mulher '{mulher.name}', {error_msg}")
        return {"message": error_msg}, 400

# Métodos baseados em nome
# Rota de busca de mulher por nome
@app.get('/mulher', tags=[mulher_tag],
         responses={"200": MulherViewSchema, "404": ErrorSchema})
def get_mulher(query: MulherBuscaSchema):
    """Faz a busca por um mulher cadastrada na base a partir do nome

    Args:
        nome (str): nome da mulher
        
    Returns:
        dict: representação da mulher e diagnóstico associado
    """
    
    mulher_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{mulher_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    mulher = session.query(mulher).filter(mulher.name == mulher_nome).first()
    
    if not mulher:
        # A mulher não foi encontrada
        error_msg = f"mulher {mulher_nome} não encontrada na base :/"
        logger.warning(f"Erro ao buscar a mulher '{mulher_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"mulher encontrada: '{mulher.name}'")
        # retorna a representação do mulher
        return apresenta_mulher(mulher), 200
    
# Rota de remoção de mulher por nome
@app.delete('/mulher', tags=[mulher_tag],
            responses={"200": MulherViewSchema, "404": ErrorSchema})
def delete_mulher(query: MulherBuscaSchema):
    """Remove um mulher cadastrado na base a partir do nome

    Args:
        nome (str): nome da mulher
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    mulher_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre mulher #{mulher_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando mulher
    mulher = session.query(mulher).filter(mulher.name == mulher_nome).first()
    
    if not mulher:
        error_msg = "mulher não encontrada na base :/"
        logger.warning(f"Erro ao deletar mulher '{mulher_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(mulher)
        session.commit()
        logger.debug(f"Deletada mulher #{mulher_nome}")
        return {"message": f"mulher {mulher_nome} removido com sucesso!"}, 200