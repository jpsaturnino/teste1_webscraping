"""
Jose Paulo
Teste1_WebScrapping
"""
from bs4 import BeautifulSoup as bs
import requests

URL = "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss"


def get_soup(url):
    return bs(requests.get(url).content, "html.parser")


def get_nome_arquivo(str):
    cont = 0
    nome_arquivo = ""
    for i in range(len(str) - 1, 0, -1):
        if str[i] == "-":
            cont += 1
        else:
            if cont == 2:
                return nome_arquivo
            nome_arquivo = str[i] + nome_arquivo


def baixar_tiss(soup):
    links = soup.find_all("a")
    for link in links:
        if "padrao-tiss_componente-organizacional" in link.get("href"):
            with open(
                get_nome_arquivo(link.get("href")),
                "wb",
            ) as f:
                f.write(requests.get(link.get("href")).content)


def buscar_tiss():
    soup = get_soup(URL)
    links = soup.find_all("a")
    for link in links:
        if "padrao-tiss-2013" in link.get("href"):
            return get_soup(link.get("href"))
    return None


def main():
    soup = buscar_tiss()
    if soup:
        baixar_tiss(soup)
    else:
        print("Scraper desatualizado, verifique os links!")


__name__ == "__main__" and main()
