from ddgs import DDGS

def buscar_instagram(hashtag, descricao, local="", limit=5):
    # monta a query com hashtag + descrição
    full_query = f"instagram #{hashtag.strip()} {descricao.strip()}"
    if local:
        full_query += f" {local.strip()}"

    resultados = []
    with DDGS() as ddgs:
        for r in ddgs.text(full_query, max_results=50):
            href = r.get("href", "")
            if "instagram.com" in href.lower():
                title = r.get("title", "Sem título")
                seo_description = r.get("body", "Sem descrição disponível.")
                resultados.append((title, href, seo_description))
                if len(resultados) >= limit:
                    break
    return resultados

def main():
    # input separado para hashtags
    hashtags_input = input("Digite as hashtags separadas por vírgula (sem #): ").strip()
    hashtags = [h.strip() for h in hashtags_input.split(",") if h.strip()]

    # input separado para descrição SEO
    descricao = input("Digite a descrição SEO: ").strip()

    local = input("Digite a cidade/bairro (ou deixe vazio): ").strip()
    limit = int(input("Digite o número de resultados por hashtag: ").strip())

    for hashtag in hashtags:
        print(f"\n🔎 Buscando resultados para #{hashtag} + {descricao}...\n")
        resultados = buscar_instagram(hashtag, descricao, local, limit)

        if resultados:
            print(f"✅ Foram encontrados {len(resultados)} resultados do Instagram para #{hashtag} + {descricao}:\n")
            for i, (title, href, seo_description) in enumerate(resultados, start=1):
                print(f"[{i}] {title}")
                print(f"URL: {href}")
                print(f"SEO Description: {seo_description}\n")
        else:
            print(f"⚠️ Nenhum resultado do Instagram encontrado para #{hashtag} + {descricao}.")

if __name__ == "__main__":
    main()
