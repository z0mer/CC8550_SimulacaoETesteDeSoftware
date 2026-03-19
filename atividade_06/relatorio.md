# Relatório de Atividade 06 - Testes de Unidade e Integração

## 1. Resultados dos Testes
A suíte de testes foi totalmente implementada e executada com sucesso utilizando a framework **Pytest**. Os exemplos fornecidos no guião da atividade foram adaptados para o formato desta framework e, conforme exigido, foi adicionado pelo menos um teste extra e original a cada categoria (Limites, Tipagem, Fluxos de Controlo, Integração e Doubles). Todos os testes passaram sem erros, garantindo que as operações matemáticas, os limites de valores e as exceções funcionam como o esperado.

## 2. Bug Encontrado e Corrigido
O defeito intencional estava localizado na função `potencia` dentro do ficheiro `src/calculadora.py`. 
- **O problema:** A formatação da *string* enviada para o histórico estava a omitir o operador matemático. O código original enviava `f"{base} {expoente} = {resultado}"`.
- **Como foi descoberto:** O erro foi detetado ao executar o teste com **Mock** (`test_mock_verifica_argumento_potencia`). O teste esperava que o repositório recebesse a *string* completa (com o `**`), o que causou uma falha na asserção.
- **A correção:** O código foi corrigido adicionando o operador na formatação: `f"{base} ** {expoente} = {resultado}"`.

## 3. Cobertura Obtida
Alcançámos **100% de cobertura** de linhas no ficheiro `calculadora.py`. 
- **Justificativa das linhas cobertas:** Numa primeira execução, as linhas correspondentes aos comandos `raise TypeError` e `raise ValueError` não estavam a ser alcançadas. Para atingir a cobertura total, implementámos os testes de validação de tipagem e de valores fora de intervalo, forçando a passagem de *strings* onde deveriam estar números e provocando divisões por zero. Isto garantiu que todas as ramificações de erro fossem efetivamente testadas.

## 4. Reflexão Prática: Diferença entre Stub e Mock
Ao implementar a secção de *Test Doubles*, a diferença de responsabilidades ficou evidente:
- **Stub:** Foi utilizado para fornecer dados "enlatados" e controlar o estado (como forçar o `total()` a retornar 0), permitindo que a calculadora funcionasse em isolamento sem precisar que o repositório estivesse realmente pronto ou a guardar dados. É um teste de **estado**.
- **Mock:** Foi utilizado para monitorizar as chamadas. Não estávamos focados apenas no resultado do cálculo, mas sim em verificar se a calculadora cumpria o seu contrato de comunicação, confirmando se o método `salvar` do repositório era invocado o número certo de vezes e com os argumentos exatos. É um teste de **comportamento** (interação).