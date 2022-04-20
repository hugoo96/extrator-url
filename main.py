# url = 'https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'

# # Separa base e os parametros
# indice_interrogacao = url.find('?')
# url_base = url[:indice_interrogacao]
#
# url_parametros = url[indice_interrogacao+1:]
# print(url_parametros)
#
# # Busca o valor de um parametro
# parametro_busca = 'quantidade'
# indice_parametro = url_parametros.find(parametro_busca)
#
# indice_valor = indice_parametro + len(parametro_busca) + 1
# indice_e_comercial = url_parametros.find('&', indice_valor)
# if indice_e_comercial == -1:
#     valor = url_parametros[indice_valor:]
# else:
#     valor = url_parametros[indice_valor:indice_e_comercial]
# print(valor)

# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
# url = ' '

# Sanitização da URL
# url = url.replace(' ', '')
#
# # Validação da URL
# if url == '':
#     raise ValueError('A URL está vazia')
# indice_interrogacao = url.find('?')
# print(indice_interrogacao)
# url_base = url[:indice_interrogacao]
# print(url_base)
# url_parametros = url[indice_interrogacao+1:]
# print(url_parametros)
# parametro_busca = 'moedaDestino'
# indice_parametro = url_parametros.find(parametro_busca)
# print(indice_parametro)
# indice_valor = indice_parametro + len(parametro_busca) + 1
# print(indice_valor)
#
# indice_e_comercial = url_parametros.find('&', indice_valor)
# print(indice_e_comercial)
# if indice_e_comercial == -1:
#     valor = url_parametros[indice_valor:]
# else:
#     valor = url_parametros[indice_valor:indice_e_comercial]
# print(valor)



print(not bool(0))








