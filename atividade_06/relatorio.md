# Relatório da Atividade 06

## 1. Resultados dos Testes
Fiz todos os testes que a atividade pedia usando a biblioteca Pytest, que é o padrão que eu costumo usar. Peguei os exemplos do PDF, adaptei para o Pytest e criei pelo menos um teste novo e original para cada categoria (Limites, Tipagem, Fluxo, Integração e Doubles). Rodou tudo super bem e os testes passaram todos sem erros!

## 2. O Bug Oculto (Encontrado e Corrigido!)
O professor deixou um erro de propósito na função `potencia` lá no arquivo `calculadora.py`. O código estava tentando salvar a conta no histórico sem o símbolo da matemática (estava ficando `base expoente = resultado` em vez de `base ** expoente = resultado`). 
Descobri isso porque o meu teste com o **Mock** falhou: ele esperava que a calculadora enviasse a string com o `**` para o histórico, e ela não estava enviando. Para consertar, foi só ir no código fonte e colocar o `**` dentro da formatação da string.

## 3. Cobertura de Código
Consegui atingir 100% de cobertura no `calculadora.py`! No começo não estava dando 100% porque aquelas linhas de segurança do código (os `raise TypeError` e `raise ValueError`) não estavam sendo ativadas. A solução foi criar testes de tipagem que forçavam a barra: mandei letras no lugar de números e tentei dividir por zero. Com isso, o teste passou por dentro de todos os `if`s de erro e cobriu tudo.

## 4. Stub vs Mock na Prática
Fazer isso na prática ajudou muito a entender a diferença:
- **Stub:** Usei para "enganar" a calculadora. Basicamente, criei um repositório falso e fingi que ele já tinha dados ou que estava vazio. Assim, consegui testar se a calculadora sabia fazer as contas sem depender do repositório de verdade. É focado no estado.
- **Mock:** Usei como "espião". O Mock não estava lá apenas para devolver um valor, ele serviu para me provar se a calculadora estava se comunicando direito com o repositório. Ele garantiu que a função `salvar` foi chamada e me mostrou exatamente o texto que a calculadora tentou guardar (foi a minha salvação para achar o bug!). É focado no comportamento.
