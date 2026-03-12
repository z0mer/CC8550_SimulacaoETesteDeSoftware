# Relatório da Atividade 05 

## 1. Introdução

Este relatório apresenta os resultados da aplicação de testes de mutação sobre um programa Python contendo cinco funções matemáticas e lógicas básicas (`subtrair`, `eh_multiplo_de_tres`, `menor_numero`, `calcular_dobro_se_par`, e `classificar_temperatura`). O objetivo foi avaliar a qualidade de uma suíte de 10 casos de teste desenvolvidos com o framework `pytest`, utilizando duas abordagens de mutação: manual e automatizada.

## 2. Análise de Mutação Manual

Na abordagem manual, foram introduzidas intencionalmente 10 mutações no código original (uma modificação por mutante). As mutações consistiram na substituição de operadores relacionais e aritméticos (ex.: alterar `a < b` para `a <= b`, ou `temp >= 30` para `temp > 30`).

Após a execução da suíte de testes original contra os mutantes manuais, obtiveram-se os seguintes resultados:

* **Total de mutantes gerados:** 10
* **Mutantes Mortos (Detectados):** 8
* **Mutantes Sobreviventes (Não detectados):** 2
* **Mutation Score (Escore de Mutação):** 80,0%

**Avaliação Manual:** A suíte de testes conseguiu detectar a grande maioria dos defeitos de fluxo lógico direto. Os 2 mutantes que sobreviveram revelaram que os testes não contemplavam adequadamente os valores limites das condicionais de contorno (ex.: valores perfeitamente iguais nas condicionais de `<` e `>=`).

## 3. Análise de Mutação Automatizada (Mutmut)

Para a abordagem automatizada, utilizou-se a ferramenta `mutmut` sobre o arquivo fonte. A ferramenta gerou mutações exaustivas de forma automática, alterando operadores, modificando constantes numéricas e manipulando valores de retorno em todas as funções.

A execução do `mutmut` contra a mesma suíte de testes do `pytest` retornou os seguintes resultados:

* **Total de mutantes gerados:** 25
* **Mutantes Mortos (Detectados):** 19
* **Mutantes Sobreviventes (Não detectados):** 6
* **Mutation Score (Escore de Mutação):** 76,0%

**Avaliação Automatizada:** A análise revelou 6 mutantes sobreviventes. Ao investigar esses sobreviventes, constatou-se a existência de lacunas de cobertura nos testes, tais como:

1. **Ausência de classes de equivalência intermediárias:** A ramificação `elif` da função `classificar_temperatura` (que retorna "Agradável") não possuía nenhum caso de teste associado.
2. **Deficiência na análise de valor limite (Boundary Value Analysis):** A função `menor_numero` não foi testada com argumentos iguais (ex.: `a = 5`, `b = 5`), permitindo que mutantes que alteravam operadores restritos para não-restritos sobrevivessem.

## 4. Comparação de Resultados e Conclusão

| Métrica | Abordagem Manual | Abordagem Automatizada |
| --- | --- | --- |
| **Mutantes Gerados** | 10 | 25 |
| **Mutantes Mortos** | 8 | 19 |
| **Mutantes Sobreviventes** | 2 | 6 |
| **Mutation Score** | 80,0% | 76,0% |

**Conclusão:** Embora a abordagem manual seja útil para introduzir o conceito e validar fluxos básicos, ela é ineficiente e dependente da intuição do testador. A inserção manual resultou em uma falsa impressão de robustez (80% de Mutation Score), pois falhou em explorar mutações em constantes e retornos isolados.

Em contrapartida, a abordagem automatizada (Mutmut) foi substancialmente mais exaustiva. Ao gerar um volume mais de duas vezes maior de mutantes (25 automáticos vs. 10 manuais), a ferramenta revelou a verdadeira cobertura estrutural dos testes (76%). Conclui-se que o uso de ferramentas automatizadas de mutação é fundamental para evidenciar deficiências críticas na suíte de testes (especialmente relacionadas a valores limite e fluxos não testados), fornecendo dados precisos para a melhoria contínua da qualidade do software.