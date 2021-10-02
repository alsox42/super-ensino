# super-ensino
API simula uma lista de exercícios e alternativas armazenando a resposta do usuário, e exibindo 
seu desempenho em acerto/erros e aproveitamento.

1 - criar uma aplicação Django que permita a um usuário pelo Django
    Admin criar exercícios com as respectivas alternativas (OK)
2 - Listar os exercícios disponíveis. (OK)
3 - Carregar os detalhes de um exercício específico (OK)
4 - Armazenar a resposta dada a um determinado exercício (OK)
5 - Resumo de desempenho na lista de exercícios contendo:
    - Total de acertos (OK) 
    - Total de erros (OK)
    - Aproveitamento (OK)
     
OBS:
"lembrando que apenas uma delas pode ser considerada correta" 
Não fiz porque de inicio achei que já estava certo,
depois entendi que poderia controlar essa ação a partir das opções
abaixo, mas não dava mais tempo:

clean.py verificando se já tinha alguma outra opção com True
metodo save() verificando se outra opção tinha True, se tiver
desmarca e marca a atual..

*****************************************************************
"Caso o exercício já tenha sido respondido, trazer o
ID da resposta dada à questão"

Escolher fazer os serializers com ModelSerializer deu produtividade
por um lado e limitou meu controle do código por outro lado. Essa opção
não esta funcionando corretamente, porque para cada exercicio a api
está listando todas as respostas atribuidas para aquele exercicio. Como
não consigo captura o usuario logado da forma que fiz, então o sistema 
não se comporta adequadamente. Teria que desfazer esse endpoint e cria-lo
de forma mais manual, dessa forma faria tudo no proprio viewSet já teria
acesso ao user logado e o item seria atendido na integra...



