# Atividade Prática 04 – Técnicas Caixa-Branca

Disciplina: CC8550 – Simulação e Teste de Software (FEI)

---

## Como executar os testes

```bash
pytest atividade_04/
```

---

## Exercício 1 – Caminhos Independentes

### Função
```python
def verificar(n): ...
```

### Grafo de Fluxo de Controle (GFC)
```
[1] Início / entrada de n
     |
[2] n > 0 ?
   /       \
 Sim        Não
  |          |
[3] n%2==0? [6] n < 0 ?
 /    \       /     \
Sim   Não   Sim     Não
 |     |     |       |
[4]   [5]   [7]     [8]
"Par" "Ím." "Neg." "Zero"
```

### Complexidade Ciclomática
- Predicados: 3 (`n > 0`, `n % 2 == 0`, `n < 0`)
- **V(G) = 3 + 1 = 4**

### Caminhos Independentes
| # | Caminho | Condição |
|---|---------|----------|
| 1 | 1→2(S)→3(S)→4 | n > 0 e par |
| 2 | 1→2(S)→3(N)→5 | n > 0 e ímpar |
| 3 | 1→2(N)→6(S)→7 | n < 0 |
| 4 | 1→2(N)→6(N)→8 | n == 0 |

### Tabela de Casos de Teste
| ID | Entrada | Saída Esperada | Critério |
|----|---------|----------------|----------|
| CT1 | n=4 | "Par positivo" | Caminho 1 |
| CT2 | n=3 | "Impar positivo" | Caminho 2 |
| CT3 | n=-1 | "Negativo" | Caminho 3 |
| CT4 | n=0 | "Zero" | Caminho 4 |

---

## Exercício 2 – Cobertura de Comandos e Ramos

### Função
```python
def classificar(x): ...
```

### Grafo de Fluxo de Controle (GFC)
```
[1] Início / entrada de x
     |
[2] x > 100 ?
   /         \
 Sim          Não
  |            |
[3] "Alto"  [4] x > 50 ?
             /          \
           Sim           Não
            |             |
         [5] "Medio"  [6] "Baixo"
```

### Complexidade Ciclomática
- Predicados: 2 (`x > 100`, `x > 50`)
- **V(G) = 2 + 1 = 3**

### Caminhos Independentes
| # | Caminho | Condição |
|---|---------|----------|
| 1 | 1→2(S)→3 | x > 100 |
| 2 | 1→2(N)→4(S)→5 | 50 < x ≤ 100 |
| 3 | 1→2(N)→4(N)→6 | x ≤ 50 |

### Cobertura C0 e C1
- **C0 (comandos):** 3 CTs necessários (um por `return`).
- **C1 (ramos):** 3 CTs necessários (True/False de cada `if`). Os mesmos 3 CTs cobrem C0 e C1.

### Tabela de Casos de Teste
| ID | Entrada | Saída Esperada | Critério |
|----|---------|----------------|----------|
| CT1 | x=150 | "Alto" | C0+C1, Caminho 1 |
| CT2 | x=75 | "Medio" | C0+C1, Caminho 2 |
| CT3 | x=30 | "Baixo" | C0+C1, Caminho 3 |
| CT4 | x=100 | "Medio" | Valor limite |
| CT5 | x=50 | "Baixo" | Valor limite |

---

## Exercício 3 – Cobertura de Condição

### Função
```python
def acesso(idade, membro): ...
```

### Grafo de Fluxo de Controle (GFC)
```
[1] Início / entrada de idade, membro
     |
[2] (idade >= 18) AND membro ?
   /                          \
 Sim                          Não
  |                            |
[3] "Permitido"            [4] "Negado"
```

### Complexidade Ciclomática
- Predicados: 1 (condição composta)
- **V(G) = 1 + 1 = 2**

### Cobertura de Condição (CC) vs Cobertura de Ramos (C1)
| CT | idade >= 18 | membro | Resultado | C1 | CC |
|----|-------------|--------|-----------|----|----|
| 1  | True        | True   | Permitido | ✓  | ✓  |
| 2  | True        | False  | Negado    |    | ✓  |
| 3  | False       | True   | Negado    |    | ✓  |
| 4  | False       | False  | Negado    | ✓  | ✓  |

- **C1:** 2 CTs necessários.
- **CC:** 4 CTs necessários. CC é mais rigorosa pois exercita todas as combinações das subcondições.

---

## Exercício 4 – Teste de Ciclo

### Função
```python
def somar_ate(n): ...
```

### Grafo de Fluxo de Controle (GFC)
```
[1] Início / soma=0
     |
[2] i < n ? (for/range)
   /        \
 Sim         Não
  |           |
[3] soma+=i  [4] return soma
  |
 (volta → [2])
```

### Complexidade Ciclomática
- Predicados: 1 (condição do laço)
- **V(G) = 1 + 1 = 2**

### Tabela de Casos de Teste
| ID | Entrada | Saída Esperada | Cenário |
|----|---------|----------------|---------|
| CT1 | n=0 | 0 | Laço ignorado (0 iterações) |
| CT2 | n=1 | 0 | Laço 1 vez (range(1)=[0]) |
| CT3 | n=5 | 10 | Laço várias vezes (0+1+2+3+4=10) |
| CT4 | n=2 | 1 | Variação (0+1=1) |

---

## Exercício 5 – Teste de Ciclo Aninhado

### Função
```python
def percorrer_matriz(m, n): ...
```

### Grafo de Fluxo de Controle (GFC)
```
[1] Início / entrada m, n
     |
[2] i < m ? (laço externo)
   /        \
 Sim         Não
  |           |
[3] j < n ?  [6] Fim
   /       \
 Sim        Não
  |          |
[4] print  [5] próx. i
  |
 (volta → [3] → [2])
```

### Complexidade Ciclomática
- Predicados: 2 (condição de cada laço)
- **V(G) = 2 + 1 = 3**

### Tabela de Casos de Teste
| ID | Entrada | Execuções de print | Cenário |
|----|---------|-------------------|---------|
| CT1 | m=0, n=0 | 0 | Ambos ignorados |
| CT2 | m=1, n=0 | 0 | Laço j ignorado |
| CT3 | m=1, n=3 | 3 | i=1 vez, j=3 vezes |
| CT4 | m=3, n=3 | 9 | Ambos várias vezes |
| CT5 | m=3, n=1 | 3 | i=3 vezes, j=1 vez |

---

## Exercício 6 – Teste Completo (Integrador)

### Função
```python
def analisar(numeros): ...
```

### Grafo de Fluxo de Controle (GFC)
```
[1] Início / total=0
     |
[2] n in numeros? (laço)
   /               \
 Sim               Não
  |                 |
[3] n>0 AND       [7] total>10?
    n%2==0?        /          \
   /       \     Sim           Não
 Sim        Não   |             |
  |          |  [8]"Acima"  [9]"Abaixo"
[4]total+=n [5] n<0?
              /     \
            Sim     Não
             |       |
         [6]total-=1 [continue]
              |
           (volta → [2])
```

### Complexidade Ciclomática
- Predicados: laço, `n>0 AND n%2==0`, `n<0`, `total>10`
- **V(G) ≈ 5**

### Tabela de Casos de Teste
| ID | Entrada | Saída Esperada | Critério |
|----|---------|----------------|---------|
| CT1 | [] | "Abaixo" | Laço 0 iterações |
| CT2 | [2] | "Abaixo" | 1 iteração, n par positivo, total≤10 |
| CT3 | [2,4,6] | "Acima" | Várias iterações, total>10 |
| CT4 | [-1] | "Abaixo" | n negativo |
| CT5 | [1] | "Abaixo" | n ímpar positivo → continue |
| CT6 | [12] | "Acima" | 1 iteração, total>10 |
| CT7 | [4,-1,3] | "Abaixo" | Valores mistos |

### Pares def-uso de `total`
- `def total=0` → uso em `total+=n`, `total-=1`, `total>10`, `return`
- `def total+=n` → uso em `total>10`, `return`
- `def total-=1` → uso em `total>10`, `return`

---

## Exercício 7 – Fluxo de Dados

### Função
```python
def desconto(preco, cliente_vip): ...
```

### Definições e Usos de Variáveis
| Variável | Definição (linha) | Usos (linhas) |
|----------|-------------------|---------------|
| `preco` | L1 | L2, L4, L5 |
| `cliente_vip` | L1 | L3 |
| `total` | L2, L5, L7 | L6, L8 |
| `desconto` | L4 | L5 |

### Pares Def-Uso de `total`
| Par | Definição | Uso | Condição |
|-----|-----------|-----|----------|
| (L2, L6) | `total=preco` | `if total<50` | sempre |
| (L2, L8) | `total=preco` | `return total` | cliente_vip=False e total≥50 |
| (L5, L6) | `total=preco-desc` | `if total<50` | cliente_vip=True |
| (L5, L8) | `total=preco-desc` | `return total` | cliente_vip=True e total≥50 |
| (L7, L8) | `total=50` | `return total` | total original < 50 |

### Tabela de Casos de Teste
| ID | Entrada | Saída Esperada | Critério |
|----|---------|----------------|---------|
| CT1 | preco=100, vip=False | 100 | All-Defs def(L2); (L2,L6)+(L2,L8) |
| CT2 | preco=30,  vip=False | 50  | All-Defs def(L7); (L2,L6)+(L7,L8) |
| CT3 | preco=100, vip=True  | 80  | All-Defs def(L5); (L5,L6)+(L5,L8) |
| CT4 | preco=30,  vip=True  | 50  | All-Uses (L5,L6)+(L7,L8) |
| CT5 | preco=50,  vip=False | 50  | Valor limite total==50 |
| CT6 | preco=60,  vip=True  | 50  | total=48<50 com vip |

### Par def-uso não coberto por C1
O par **(L5, L8)** — `cliente_vip=True` e `total >= 50` — pode não ser coberto pelos CTs de C1 que verificam apenas o True/False de cada `if` isoladamente. É necessário incluir explicitamente um CT com `preco=100, cliente_vip=True` (CT3) para cobrir esse par.
