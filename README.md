# Social-Search-Prompt
Social Search Prompt é uma ferramenta em Python que permite realizar buscas inteligentes em redes sociais (como Instagram e Pinterest) utilizando a biblioteca ddgs (DuckDuckGo Search). O projeto foi pensado para facilitar pesquisas de hashtags e descrições SEO, trazendo resultados filtrados diretamente das plataformas desejadas.
# 📌 Social Search Prompt

**Social Search Prompt** é uma ferramenta em Python que permite realizar buscas inteligentes em redes sociais (Instagram e Pinterest) utilizando a biblioteca [`ddgs`](https://pypi.org/project/ddgs/) (DuckDuckGo Search).  
O projeto foi criado para facilitar pesquisas de **hashtags** e **descrições SEO**, trazendo resultados filtrados diretamente das plataformas desejadas.

---

## ✨ Funcionalidades
- Busca automatizada por **hashtags** em redes sociais.
- Entrada separada para **hashtags** e **descrição SEO**.
- Filtragem de resultados para exibir apenas links relevantes (`instagram.com` ou `pinterest.com`).
- Retorno estruturado com **título, URL e SEO description**.
- Suporte a múltiplas hashtags em uma única execução.

---

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/aceleradox/Social-Search-Prompt.git
cd Social-Search-Prompt
pip install ddgs
