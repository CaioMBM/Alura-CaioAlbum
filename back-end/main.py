from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Cria a instância da aplicação FastAPI
app = FastAPI()

mensagem = {"mensagem": "Olá, pessoal"}

@app.get("/")
def exibir_home():
    return mensagem

# Configuração do Middleware CORS para permitir requisições de qualquer origem (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite qualquer origem
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], # Permite todos os headers
)

# Definição dos caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista com as 30 figurinhas. 
# Deixamos ativas apenas as figurinhas de id 1 e 2 cujas imagens já existem no diretório.
# As outras figurinhas (do id 3 ao 30) estão comentadas até que as imagens sejam adicionadas.
figurinhas = [
    {
        "id": 1,
        "nome": "Avatar",
        "categoria": "Filmes favoritos",
        "imagem_url": "/figurinhas/1/imagem"
    },
    {
        "id": 2,
        "nome": "Exterminador do Futuro 2",
        "categoria": "Filmes favoritos",
        "imagem_url": "/figurinhas/2/imagem"
    },
    {
        "id": 3,
        "nome": "Homem-Aranha (2002)",
        "categoria": "Filmes favoritos",
        "imagem_url": "/figurinhas/3/imagem"
    },
    {
        "id": 4,
        "nome": "Harry Potter e o Prisioneiro de Azkaban",
        "categoria": "Filmes favoritos",
        "imagem_url": "/figurinhas/4/imagem"
    },
    {
        "id": 5,
        "nome": "Jurassic Park",
        "categoria": "Filmes favoritos",
        "imagem_url": "/figurinhas/5/imagem"
    },
    {
        "id": 6,
        "nome": "Dragon Ball Z",
        "categoria": "Animes favoritos",
        "imagem_url": "/figurinhas/6/imagem"
    },
    {
        "id": 7,
        "nome": "Dan Da Dan",
        "categoria": "Animes favoritos",
        "imagem_url": "/figurinhas/7/imagem"
    },
    {
        "id": 8,
        "nome": "Attack on Titan",
        "categoria": "Animes favoritos",
        "imagem_url": "/figurinhas/8/imagem"
    },
    {
        "id": 9,
        "nome": "Jojo's Bizarre Adventures",
        "categoria": "Animes favoritos",
        "imagem_url": "/figurinhas/9/imagem"
    },
    {
        "id": 10,
        "nome": "Naruto Shippuden",
        "categoria": "Animes favoritos",
        "imagem_url": "/figurinhas/10/imagem"
    },
    {
        "id": 11,
        "nome": "Os Simpsons",
        "categoria": "Séries de animação",
        "imagem_url": "/figurinhas/11/imagem"
    },
    {
        "id": 12,
        "nome": "Castlevania",
        "categoria": "Séries de animação",
        "imagem_url": "/figurinhas/12/imagem"
    },
    {
        "id": 13,
        "nome": "Arcane",
        "categoria": "Séries de animação",
        "imagem_url": "/figurinhas/13/imagem"
    },
    {
        "id": 14,
        "nome": "X-men: Evolution",
        "categoria": "Séries de animação",
        "imagem_url": "/figurinhas/14/imagem"
    },
    {
        "id": 15,
        "nome": "X-men: 97'",
        "categoria": "Séries de animação",
        "imagem_url": "/figurinhas/15/imagem"
    },
    {
        "id": 16,
        "nome": "Friends",
        "categoria": "Séries favoritas",
        "imagem_url": "/figurinhas/16/imagem"
    },
    {
        "id": 17,
        "nome": "Grimm",
        "categoria": "Séries favoritas",
        "imagem_url": "/figurinhas/17/imagem"
    },
    {
        "id": 18,
        "nome": "Modern Family",
        "categoria": "Séries favoritas",
        "imagem_url": "/figurinhas/18/imagem"
    },
    {
        "id": 19,
        "nome": "Stranger Things",
        "categoria": "Séries favoritas",
        "imagem_url": "/figurinhas/19/imagem"
    },
    {
        "id": 20,
        "nome": "The Vampire Diaries",
        "categoria": "Séries favoritas",
        "imagem_url": "/figurinhas/20/imagem"
    },
    {
        "id": 21,
        "nome": "Dishonored",
        "categoria": "Jogos favoritos pt.1",
        "imagem_url": "/figurinhas/21/imagem"
    },
    {
        "id": 22,
        "nome": "Uncharted 3",
        "categoria": "Cálculo Espacial",
        "imagem_url": "/figurinhas/22/imagem"
    },
    {
        "id": 23,
        "nome": "Lego Batman",
        "categoria": "Jogos favoritos pt.1",
        "imagem_url": "/figurinhas/23/imagem"
    },
    {
        "id": 24,
        "nome": "Resident Evil 7",
        "categoria": "Jogos favoritos pt.1",
        "imagem_url": "/figurinhas/24/imagem"
    },
    {
        "id": 25,
        "nome": "Dying Light",
        "categoria": "Jogos favoritos pt.1",
        "imagem_url": "/figurinhas/25/imagem"
    },
    {
        "id": 26,
        "nome": "Battlefield 3",
        "categoria": "Jogos favoritos pt.2",
        "imagem_url": "/figurinhas/26/imagem"
    },
    {
        "id": 27,
        "nome": "Injustice",
        "categoria": "Jogos favoritos pt.2",
        "imagem_url": "/figurinhas/27/imagem"
    },
    {
        "id": 28,
        "nome": "Assassins Creed: Unity",
        "categoria": "Jogos favoritos pt.2",
        "imagem_url": "/figurinhas/28/imagem"
    },
    {
        "id": 29,
        "nome": "Minecraft",
        "categoria": "Jogos favoritos pt.2",
        "imagem_url": "/figurinhas/29/imagem"
    },
    {
        "id": 30,
        "nome": "Valorant",
        "categoria": "Jogos favoritos pt.2",
        "imagem_url": "/figurinhas/30/imagem"
    },
]

# Endpoint GET "/figurinhas" que retorna a lista de figurinhas ativas
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# Endpoint GET "/figurinhas/{id}/imagem" que retorna a imagem correspondente ao ID
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Constrói o padrão do glob com 2 dígitos para o id, seguido por qualquer caractere não numérico.
    # Exemplo: id=1 vira "01[!0-9]*", buscando "01-alan-turing.jpg" mas não "012.jpg"
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    
    # Usa glob para localizar arquivos que correspondam a esse padrão na pasta de imagens
    arquivos_encontrados = glob.glob(padrao)
    
    # Se nenhum arquivo for encontrado, lança um erro HTTP 404 (Not Found)
    if not arquivos_encontrados:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
        
    # Retorna o arquivo encontrado como uma resposta de arquivo
    return FileResponse(arquivos_encontrados[0])
