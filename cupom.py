nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def imprime_dados_loja():
  saida = f"{nome_loja}\n"
  saida += f"{logradouro}, {numero} {complemento}\n"
  saida += f"{bairro} - {municipio} - {estado}\n"
  saida += f"CEP:{cep} Tel {telefone}\n"
  saida += f"{observacao}\n"
  saida += f"CNPJ: {cnpj}\n"
  saida += f"IE: {inscricao_estadual}\n"
  return saida

  