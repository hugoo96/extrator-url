import re

endereco = "Rua Rio de Janeiro 129, Bairro Cruz Alta, Santa Cruz do Capibaribe, PE, 55195-018"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)