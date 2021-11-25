# **Ideia Geral**

Este programa se divide em 4 partes:
* extract.py - extrai os dados através de um loop e verificação do status 
do servidor.
* timsort.py - organiza os dados em ordem crescente.
* server.py - realiza a chamada dos últimos 2 e com o resultado ele envia os
dados para um servidor criado com flask.
* main.py - está parte foi criada com o intuito de centralizar o programa
e tornar mais fácil a execução dele.

Na chamada da função extract_data() no arquivo server.py pode ser regulado
de qual página deseja começar a coleta de dados. Deixei setado pra 9950 pra que
tivesse um resultado rápido mas não muito pequeno.

# **Bibliotecas utilizadas**

resquest - pegar o conteudo da API
json - carregar os dados json
flask - criação da API

# **Utilização**

Apos rodar o arquivo main.py pode se acessar o localhost:5000 aonde estarão todos
os dados.

# **Considerações**

Foi realizada uma tentativa de integrar o python com os valores organizados,
assim eles seriam armazenados lá e posteriormente criar a API a partir deles. Seria feito desta
forma para criar uma páginação offset com limit e range com o intuito de melhorar a visualização
dos dados.
Em conjunto com os códigos tem um arquivo em csv e json com aproximadamente 85000 valores ordenados.
O arquivo connectio.py tem a função de colocar os dados organizados no banco de dados de forma
automatizada.

# **Conclusão**

Neste projetos, consegui atingir grande parte dos meus objetivos, mas infelizmente não todos eles
caso seja possível peço que me recomendem formas de melhor e uma solução para criar a páginação da API
pois não consegui achar uma explicação concreta.
Meu cronograma de funções está presente no arquivo projeto.txt, ele foi mais um guia para me
orientar no que devia ser feito.

Muito obrigado pelo projeto, foi de grande ajuda para minha evolução. Peço que se puderem
me deem uma orientação de melhoria e principalmente sobre uma forma de criar a páginação de uma API.
