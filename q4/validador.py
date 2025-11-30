import re

padrao = re.compile(
    r'^((\$|[A-Za-z]+\$?)'
    r'((-?((0|[1-9][0-9]{0,2}(\.[0-9]{3})*),[0-9]{2,}))'
    r'|\(((0|[1-9][0-9]{0,2}(\.[0-9]{3})*),[0-9]{2,})\)'
    r'))$'
)

def validar_valor(valor):
    return bool(padrao.match(valor))

def main():
    arquivo = "valores.txt"

    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            valor = linha.strip()
            if not valor:
                continue

            if validar_valor(valor):
                print(f"{valor} → Válido")
            else:
                print(f"{valor} → Inválido")

if __name__ == "__main__":
    main()
