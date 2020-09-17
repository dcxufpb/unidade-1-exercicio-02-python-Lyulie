import cupom
from cupom import imprime_dados_loja

cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
cupom.logradouro = "Av. Projetada Leste"
cupom.numero = 500
cupom.complemento = "EUC F32/33/34"
cupom.bairro = "Br. Sta Genebra"
cupom.municipio = "Campinas"
cupom.estado = "SP"
cupom.cep = "13080-395"
cupom.telefone = "(19) 3756-7408"
cupom.observacao = "Loja 1317 (PDP)"
cupom.cnpj = "42.591.651/0797-34"
cupom.inscricao_estadual = "244.898.500.113"

def test_exercicio1():
    assert imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_exercicio2_tudo_vazio():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    cupom.nome_loja = ""
    cupom.logradouro = ""
    cupom.numero = 0
    cupom.complemento = ""
    cupom.bairro = ""
    cupom.municipio = ""
    cupom.estado = ""
    cupom.cep = ""
    cupom.telefone = ""
    cupom.observacao = ""
    cupom.cnpj = ""
    cupom.inscricao_estadual = ""

    assert imprime_dados_loja() == '''
, 0 
 -  - 
CEP: Tel 

CNPJ: 
IE: 
'''

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "Rodolpho Vidros LTDA"
    cupom.logradouro = "Av. Rui Carneiro"
    cupom.numero = 50
    cupom.complemento = "de esquina"
    cupom.bairro = "Miramar"
    cupom.municipio = "João Pessoa"
    cupom.estado = "PB"
    cupom.cep = "58038-000"
    cupom.telefone = "(83) 8888-0000"
    cupom.observacao = "Loja 202/2"
    cupom.cnpj = "42.591.651/0797-34"
    cupom.inscricao_estadual = "244.898.500.113"
    #E atualize o texto esperado abaixo
    assert imprime_dados_loja() == '''Rodolpho Vidros LTDA
Av. Rui Carneiro, 50 de esquina
Miramar - João Pessoa - PB
CEP:58038-000 Tel (83) 8888-0000
Loja 202/2
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''
