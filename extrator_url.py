import re


class ExtratorURL:
    def __init__(self, url):
        self.url: str = self.sanitiza_url(url)
        self.valida_url()

    def __str__(self):
        return self.url + '\n' + 'Parâmetros: ' + self.get_url_parametros() + '\n' + 'URL base: ' + self.get_url_base()

    def __len__(self):
        len(self.url)

    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self, url: str) -> str:
        if type(url) == str:
            return url.replace(' ', '')
        else:
            return ''

    def valida_url(self) -> None:
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é valida')

    def get_url_base(self) -> str:
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self) -> str:
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca) -> str:
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

url = 'https://bytebank.com/cambio?quantidade=100&MoedaOrigem=dolar&moedaDestino=real'
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moedaDestino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')
conversao = int(quantidade) * VALOR_DOLAR
print('{} dolares valem {} reais.'.format(quantidade, conversao))
