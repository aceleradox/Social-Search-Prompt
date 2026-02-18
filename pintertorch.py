from ddgs import DDGS

def buscar_pinterest(query, local="", limit=5):
    # força a query a incluir "pinterest" + termo
    full_query = f"pinterest {query.strip()}"
    if local:
        full_query += f" {local.strip()}"

    resultados = []
    with DDGS() as ddgs:
        # pega bastante resultados e filtra só os do Pinterest
        for r in ddgs.text(full_query, max_results=50):
            href = r.get("href", "")
            if "pinterest.com" in href.lower():
                title = r.get("title", "Sem título")
                snippet = r.get("body", "Sem descrição disponível.")
                resultados.append((title, href, snippet))
                if len(resultados) >= limit:
                    break
    return resultados

def main():
    query = input("Digite a query de busca: ").strip()
    limit = int(input("Digite o número de resultados: ").strip())
    local = input("Digite a cidade/bairro (ou deixe vazio): ").strip()

    resultados = buscar_pinterest(query, local, limit)

    if resultados:
        print(f"\n✅ Foram encontrados {len(resultados)} resultados do Pinterest:\n")
        for i, (title, href, snippet) in enumerate(resultados, start=1):
            print(f"[{i}] {title}")
            print(f"URL: {href}")
            print(f"Descrição: {snippet}\n")
    else:
        print("\nNenhum resultado do Pinterest encontrado.")

if __name__ == "__main__":
    main()
