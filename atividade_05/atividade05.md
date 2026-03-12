# Relatório do Lab 05

## 1. Análise de Mutação Manual

Foram gerados manualmente 10 mutantes no código original através da substituição de operadores lógicos e aritméticos (como trocar `+` por `-`, ou `>` por `<`). O conjunto de testes desenvolvido no Pytest foi executado contra essas versões alteradas.

**Resultados Manuais:**

* **Total de mutantes gerados:** 10
* **Mutantes Mortos:** 8
* **Mutantes Sobreviventes:** 2
* **Mutation Score (Manual):** 80%

Os testes manuais demonstraram que o conjunto de testes foi eficaz em capturar alterações diretas de fluxo e cálculo, porém deixou passar mutantes em condições de contorno muito específicas (valores exatamente em cima dos limites de um `if`, por exemplo).

## 2. Análise de Mutação Automatizada (Mutmut)

A ferramenta `mutmut` foi executada sobre o ficheiro `src/atv05.py`. A ferramenta realizou alterações exaustivas, substituindo retornos, operadores de comparação e constantes numéricas.

**Resultados do Mutmut:**

* **Total de mutantes gerados:** 34
* **Mutantes Mortos (Killed):** 31
* **Mutantes Sobreviventes (Survived):** 3 (IDs: 32, 33 e 34)
* **Mutation Score (Automatizado):** ~91%

## 3. Comparação dos Resultados

A abordagem manual serviu como um excelente ponto de partida lógico. Com uma taxa de mortalidade de 80%, conseguimos validar os caminhos principais de execução do código. No entanto, o processo manual é limitado à criatividade e intuição humanas, testando apenas os defeitos "óbvios".

Ao introduzir a ferramenta automatizada, o escopo de testes expandiu-se drasticamente. O Mutmut gerou 34 cenários de falha, alterando detalhes subtis que passariam despercebidos numa análise humana. O conjunto de testes originais provou ser extremamente robusto, alcançando 91% de eficácia contra os mutantes automatizados, deixando escapar apenas 3 mutações.

**Conclusão:** A automação demonstrou ser muito superior para garantir a qualidade rigorosa do software, apontando exatamente onde o nosso conjunto de testes precisa de ser reforçado (normalmente em testes de valor limite rigoroso).
