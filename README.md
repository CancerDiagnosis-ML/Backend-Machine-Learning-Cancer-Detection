# Backend-Machine-Learning-Cancer-Detection

#### Este repositório é dedicado ao desenvolvimento do back-end de uma aplicação full stack voltada para classificação utilizando técnicas de machine learning. A aplicação tem como objetivo principal identificar padrões em dados relacionados ao câncer de mama, realizando previsões de classes.

Funcionalidades Principais
Carregamento do Modelo de Machine Learning:

O backend é responsável por carregar o arquivo do modelo de machine learning, o qual será utilizado para realizar predições.
O modelo será servido de forma embarcada, garantindo a eficiência e a integridade durante a execução das previsões.
Entrada de Novos Dados no Front-End:

A interface do usuário no front-end permitirá a entrada de novos dados relacionados a características específicas associadas ao câncer de mama.
Predição da Classe de Saída:

Utilizando o modelo carregado no backend, a aplicação realizará predições com base nos dados fornecidos pelo usuário.
O modelo classificará os dados de entrada, indicando se são associados a tumores benignos ou malignos.
Exibição do Resultado na Tela:

O resultado da predição será exibido na tela do front-end, proporcionando uma experiência interativa para o usuário.

### Acesse o código-fonte do Machine Learning no [Google Colab URL](https://colab.research.google.com/drive/14ISQT78C_FeCDxm-k6Y1B-yyLH1ch48x?usp=sharing)

&nbsp;

## Como executar por via linha de comando

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).


&nbsp;


Execute o seguinte comando para utilizar o ambiente virtual.

```
py -m venv env
```


```
(Unix/macOS)
$ source env/Scripts/activate

(Windows)
$ .\env\Scripts\activate
```

&nbsp;


Estando no ambiente virtual, execute o comando abaixo:

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

&nbsp;


Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```


&nbsp;


Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução. 
