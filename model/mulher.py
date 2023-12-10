from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base

# colunas = Name,Radius,Texture,Perimeter,Area,Smoothness,Compactness,Concavity,ConcavePoints,Symmetry,FractalDimension,Outcome
class mulher(Base):
    __tablename__ = 'mulheres'
    
    id = Column(Integer, primary_key=True)
    name = Column("Name", String(50))
    rad_mean = Column("RadiusMean", Float)
    tex_mean = Column("TextureMean", Float)
    perim_mean = Column("PerimeterMean", Float)
    area_mean = Column("AreaMean", Float)
    smoo_mean = Column("SmoothnessMean", Float)
    comp_mean = Column("CompactnessMean", Float)
    concav_mean = Column("ConcavityMean", Float)
    cp_mean = Column("ConcavePointsMean", Float)
    sym_mean = Column("SymmetryMean", Float)
    fd_mean = Column("FractalDimensionMean", Float)
    outcome = Column("Diagnosis", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, name:str, rad_mean:float, tex_mean:float, perim_mean:float, area_mean:float,
                 smoo_mean:float, comp_mean:float, concav_mean:float, cp_mean:float,
                 sym_mean:float, fd_mean:float, outcome:int, data_insercao:Union[DateTime, None] = None):
        """
        Cria um mulher

        Arguments:
            name: nome da mulher
            rad_mean: média das distâncias do centro até os pontos na periferia (Representa a média das distâncias do centro até os pontos que formam o perímetro de uma célula)
            tex_mean: Textura (desvio padrão dos valores em escala de cinza): Refere-se à variação da intensidade dos tons de cinza na imagem da célula.
            perim_mean: Perímetro: É o comprimento total do contorno da célula.
            area_mean: Área: Representa a área total ocupada pela célula.
            smoo_mean: Suavidade (variação local nos comprimentos dos raios): Indica quão suave é a variação nos comprimentos dos raios da célula.
            comp_mean: Compacidade (perímetro^2 / área - 1.0): É uma medida que combina informações sobre o perímetro e a área da célula.
            concav_mean: Concavidade (gravidade das porções côncavas do contorno): Avalia a severidade das regiões côncavas na borda da célula.
            cp_mean: Pontos Côncavos (número de porções côncavas do contorno): Indica quantas regiões côncavas existem na borda da célula.
            sym_mean: Simetria: Avalia a simetria da célula.
            fd_mean: Dimensão Fractal ("aproximação de linha costeira" - 1): Uma medida da complexidade estrutural da célula, às vezes comparada à complexidade da linha costeira em geometria fractal.
            outcome: diagnóstico, indicando se a célula é benigna (B) ou maligna (M).
            data_insercao: data de quando o mulher foi inserido à base
        """
        self.name = name
        self.rad_mean = rad_mean
        self.tex_mean = tex_mean
        self.perim_mean = perim_mean
        self.area_mean = area_mean
        self.smoo_mean = smoo_mean
        self.comp_mean = comp_mean
        self.concav_mean = concav_mean
        self.cp_mean = cp_mean
        self.sym_mean = sym_mean
        self.fd_mean = fd_mean
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao