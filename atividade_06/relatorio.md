# Relatório da Atividade 06

## 1. Resultados dos Testes
Fiz todos os testes que a atividade pedia usando a biblioteca Pytest, que é o padrão que costumo usar. Peguei nos exemplos do PDF, adaptei-os e criei pelo menos um teste novo e original para cada categoria (Limites, Tipagem, Fluxo, Integração e Doubles). Correu tudo super bem e os testes passaram todos sem erros!

## 2. O Bug Oculto (Encontrado e Corrigido!)
O professor deixou um erro de propósito na função `potencia` lá no ficheiro `calculadora.py`. O código estava a tentar guardar a conta no histórico sem o símbolo da matemática (estava a ficar `base expoente = resultado` em vez de `base ** expoente = resultado`). 
Descobri isto porque o meu teste com o **Mock** falhou: ele esperava que a calculadora enviasse a string com o `**` para o histórico, e ela não estava a enviar. Para consertar, foi só ir ao código fonte e colocar o `**` dentro da formatação da string.

## 3. Cobertura de Código
Consegui atingir 100% de cobertura no `calculadora.py`! No começo não estava a dar 100% porque aquelas linhas de segurança do código (os `raise TypeError` e `raise ValueError`) não estavam a ser ativadas. A solução foi criar testes de tipagem que forçavam a barra: mandei letras no lugar de números e tentei dividir por zero. Com isso, o teste passou por dentro de todos os `if`s de erro e cobriu tudo.

## 4. Stub vs Mock na Prática
Fazer isto na prática ajudou muito a entender a diferença:
- **Stub:** Usei para "enganar" a calculadora. Basicamente, criei um repositório falso e fingi que ele já tinha dados ou que estava vazio. Assim, consegui testar se a calculadora sabia fazer as contas sem depender do repositório de verdade. É focado no estado.
- **Mock:** Usei como "espião". O Mock não estava lá apenas para devolver um valor, ele serviu para me provar se a calculadora estava a comunicar direito com o repositório. Ele garantiu-me que a função `salvar` foi chamada e mostrou-me exatamente o texto que a calculadora tentou guardar (foi a minha salvação para achar o bug!). É focado no comportamento.
