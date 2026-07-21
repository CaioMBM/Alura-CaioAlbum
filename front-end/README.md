# 🏆 Alura Album - Copa do Mundo Tech

O **Alura Album** é um tributo interativo em formato de álbum de figurinhas virtual, celebrando as mentes mais brilhantes e influentes da história da tecnologia, tanto no cenário nacional quanto no internacional. O projeto simula a experiência física de colecionar figurinhas, trazendo elementos visuais modernos, interatividade fluida por meio de gestos de arraste e efeitos sonoros realistas.

---

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é criar uma aplicação web interativa e envolvente que:
1. Apresente pioneiros da Inteligência Artificial, Python, Banco de Dados, Sistemas Operacionais e Educadores de Tecnologia brasileiros.
2. Conecte-se de forma dinâmica a um servidor backend para preencher os slots de figurinhas com imagens reais.
3. Proporcione uma experiência de usuário (UX) premium através de animações, efeitos sonoros sintetizados e transições tridimensionais (3D Page Flip).

---

## 📁 Estrutura de Arquivos e Funcionalidades

O frontend do projeto é composto por três arquivos principais:

### 1. 📄 `index.html`
* **Descrição:** A fundação estrutural do álbum de figurinhas.
* **Funcionalidades:**
  * Define o layout e as páginas do álbum (Capa, Categorias e Contracapa).
  * Estrutura os slots (`.sticker-slot`) onde as figurinhas dos criadores e tecnologias são coladas.
  * Fornece os botões de navegação lateral (Anterior/Próximo) e o botão para ativar ou desativar os sons do aplicativo.
  * Carrega a biblioteca de animação 3D `PageFlip` via CDN e o script principal de controle.

### 2. 🎨 `style.css`
* **Descrição:** A folha de estilos responsável pelo visual futurista e transições fluidas.
* **Funcionalidades:**
  * Configura variáveis globais de cores e gradientes de fundo.
  * Cria efeitos de iluminação e animações premium como o efeito *glitch* nos títulos, mini cards e a esfera geométrica 3D na capa.
  * Cuida da responsividade e do posicionamento dos elementos interativos.
  * Define o visual dinâmico dos slots e a animação de aparecimento ("colagem") suave das figurinhas de forma individual.

### 3. ⚙️ `app.js`
* **Descrição:** A inteligência por trás do álbum, responsável por integrar dados e adicionar comportamentos interativos.
* **Funcionalidades:**
  * **Integração com API:** Busca as informações e imagens das figurinhas a partir do backend FastAPI (comunicação via `fetch`) e preenche o álbum automaticamente.
  * **Efeitos Sonoros:** Utiliza a *Web Audio API* para sintetizar, de forma matemática e dinâmica, o som de fricção e deslocamento do papel ao virar as páginas, dispensando arquivos de áudio pesados.
  * **Navegação:** Mapeia a interação por cliques em botões, arraste manual (mouse e touch screen) e teclas direcionais do teclado (setas esquerda e direita).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Um navegador web moderno com suporte a HTML5, CSS3 e Web Audio API.
* Backend da aplicação configurado e rodando localmente (para preenchimento das figurinhas).

### Executando o Backend
Caso você possua o servidor backend configurado em FastAPI, navegue até a pasta correspondente e inicie o servidor:
```bash
cd backend/dia-3
uvicorn main:app --reload
```
O servidor deverá rodar em `http://localhost:8000`.

### Executando o Frontend
1. Abra o arquivo `index.html` diretamente em seu navegador, ou utilize uma extensão de servidor local (ex: *Live Server* no VS Code).
2. Se o backend estiver ativo, as fotos dos especialistas serão carregadas automaticamente nos slots vazios!
