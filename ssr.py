# carregar os dados
dados = [
    {"nome": "João", "cidade": "vargem grande do sul"},
    {"nome": "Maria", "cidade": "são paulo"}
]

# processar os dados
template = """\
<html>
<body>
<ul>
    <li> Nome: {dados[nome]}</li> 
    <li> Cidade: {dados[cidade]}</li>
</ul>  
</body>
</html>
"""

# renderizar resposta
for item in dados:
    print(template.format(dados=item))