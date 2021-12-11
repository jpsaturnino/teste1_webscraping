"""
Jose Paulo
Teste1_WebScrapping
"""
from bs4 import BeautifulSoup as bs
import requests

URL = "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss"


def get_soup(url: str) -> bs:
    """
    Retorna o conteudo da pagina
    :param url: str
    :return: bs
    """
    return bs(requests.get(url).content, "html.parser")


def get_nome_arquivo(link: str) -> str:
    """
    Retorna o nome do arquivo a partir do link
    :param link: str
    :return: str
    :raises: Exception
    """
    nome_arquivo = ""
    for i in range(len(link) - 1, 0, -1):
        if link[i] != "/":
            nome_arquivo = link[i] + nome_arquivo
        else:
            return nome_arquivo


def baixar_tiss(soup: bs) -> None:
    """
    Faz o download do ultimo arquivo TISS.
    :param soup: Uma instancia de bs
    :return: None
    :raises: Exception
    """
    links = soup.find_all("a")
    for link in links:
        if "padrao-tiss_componente-organizacional" in link.get("href"):
            with open(
                get_nome_arquivo(link.get("href")),
                "wb",
            ) as arquivo_pdf:
                return arquivo_pdf.write(requests.get(link.get("href")).content)
    raise Exception("Não foi possivel baixar o arquivo TISS")


def buscar_tiss() -> bs:
    """
    Busca o ultimo arquivo TISS
    :return: bs
    :raises: Exception
    """
    soup = get_soup(URL)
    links = soup.find_all("a")
    for link in links:
        if "padrao-tiss-2013" in link.get("href"):
            return get_soup(link.get("href"))
    raise Exception(
        "Não foi possivel encontrar o arquivo TISS, verifique o link de acesso!"
    )


def main():
    soup = buscar_tiss()
    baixar_tiss(soup)


__name__ == "__main__" and main()
