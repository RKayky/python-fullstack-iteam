# 🐍 Desafios – Módulo 1: Introdução ao Python
**Curso de Capacitação em Desenvolvimento Full Stack – ITEAM**  
Professor: Msc. Hygo Sousa De Oliveira

---

> **Como usar este repositório:**
> - Leia o enunciado de cada exercício com atenção.
> - Crie um arquivo `.py` para cada solução (ex: `ex01.py`, `ex02.py`...).
> - Os exercícios estão divididos em três níveis: 🟢 Básico | 🟡 Intermediário | 🔴 Avançado.
> - O gabarito está disponível em `gabarito.py`, mas tente resolver sozinho primeiro!

---

## 📅 Dia 1 – História, Filosofia e Configuração do Ambiente

### 🟢 Exercício 01 – O Clássico com Personalidade
Todo programador começa com "Hello, World!". Mas aqui vamos além:  
Escreva um script que exiba, em linhas separadas:
1. `Olá, Mundo!`
2. Seu nome completo
3. A frase: `Python: simples, poderoso e elegante.`

> 💡 *Dica: use a função `print()` três vezes.*

---

### 🟢 Exercício 02 – Inspecionando o Ambiente
Escreva um script que importe o módulo `sys` e exiba:
1. A versão do Python instalada (`sys.version`)
2. O sistema operacional em uso (`sys.platform`)

> 💡 *Dica: `import sys` e use `print()` para exibir as informações.*

---

### 🟢 Exercício 03 – O Zen na Prática
O **Zen of Python** pode ser acessado com `import this`.  
Escreva um script que:
1. Importe o módulo `this` para exibir o Zen.
2. Abaixo do import, adicione um comentário (`#`) explicando com suas próprias palavras **um** dos princípios que mais fez sentido para você.

> 💡 *Comentários são ignorados pelo interpretador, mas são essenciais para quem lê o código.*

---

### 🟡 Exercício 04 – Comentários como Documentação
Você recebeu o código abaixo **sem nenhum comentário**. Seu trabalho é **adicionar comentários explicativos** em cada linha e também uma **docstring** no topo descrevendo o que o programa faz:

```python
nome = "Ana Lima"
idade = 29
salario = 4500.00
ativo = True
print(nome, idade, salario, ativo)
```

> 💡 *Boas práticas: docstrings usam `"""texto"""` e comentários usam `#`.*

---

### 🟡 Exercício 05 – Primeira Análise de Erro
O código abaixo contém **erros propositais**. Identifique-os, corrija-os e explique em comentários o que estava errado:

```python
Print("Bem-vindo ao curso de Python")
nome = "Carlos
print("Aluno: " + nome)
print(Curso de Python)
```

> 💡 *Erros de sintaxe (`SyntaxError`) são os mais comuns para iniciantes. Saber lê-los é uma habilidade essencial.*

---

### 🔴 Exercício 06 – Explorando Tipos com `type()`
Escreva um script que crie **6 variáveis** com os seguintes valores e tipos:
- Um número inteiro representando o ano atual
- Um número de ponto flutuante representando uma temperatura em Celsius
- Uma string com o nome de uma cidade brasileira
- Um booleano indicando se está chovendo
- O valor especial `None` atribuído a uma variável chamada `previsao`
- Uma string vazia

Para cada variável, use `print()` para exibir o **valor** e seu **tipo** com `type()`.

Formato de saída esperado:
```
2025 → <class 'int'>
28.5 → <class 'float'>
...
```

> 💡 *A função `type()` retorna o tipo de qualquer objeto Python.*

---

## 📅 Dia 2 – Variáveis, Tipos, Operadores, Entrada e Saída

### 🟢 Exercício 07 – Calculadora de Área
Uma construtora precisa calcular a área de terrenos retangulares.  
Escreva um script que:
1. Armazene a largura (`12.5`) e o comprimento (`30.0`) em variáveis
2. Calcule e exiba a **área** (largura × comprimento)
3. Exiba o resultado formatado: `Área do terreno: 375.0 m²`

---

### 🟢 Exercício 08 – Conversor de Temperatura
Escreva um script que converta uma temperatura de **Celsius para Fahrenheit** e para **Kelvin**.

Fórmulas:
- `F = (C × 9/5) + 32`
- `K = C + 273.15`

Use o valor `36.5°C` (temperatura corporal) e exiba os três valores formatados.

---

### 🟢 Exercício 09 – Boas-vindas Personalizada
Escreva um script que:
1. Solicite ao usuário seu **nome** (`input()`)
2. Solicite sua **idade**
3. Exiba: `Olá, [nome]! Você tem [idade] anos e nasceu por volta de [ano_nascimento].`

> 💡 *Lembre-se: `input()` sempre retorna uma string. Para operar matematicamente, converta com `int()`.*

---

### 🟢 Exercício 10 – Divisão Inteira e Resto
Em sistemas de logística, é comum calcular quantas caixas completas cabem em um caminhão.  
Dado que um caminhão comporta **850 kg** e cada caixa pesa **32 kg**:
1. Calcule quantas caixas **completas** cabem (`//`)
2. Calcule o **peso restante** que não completa uma caixa (`%`)
3. Exiba os dois valores com mensagens claras

---

### 🟡 Exercício 11 – Formatação Profissional com f-strings
Uma empresa de RH precisa gerar fichas de funcionários.  
Escreva um script que armazene os dados abaixo e os exiba **formatados** conforme o modelo:

Dados:
- Nome: `Mariana Souza`
- Cargo: `Analista de Dados`
- Salário: `7850.50`
- Anos de empresa: `3`

Saída esperada:
```
=============================
     FICHA DO FUNCIONÁRIO    
=============================
Nome   : Mariana Souza
Cargo  : Analista de Dados
Salário: R$ 7.850,50
Tempo  : 3 ano(s) de empresa
=============================
```

> 💡 *Use f-strings e explore formatação de números: `{valor:,.2f}` ou `{valor:.2f}`.*

---

### 🟡 Exercício 12 – Calculadora de IMC
O Índice de Massa Corporal (IMC) é calculado pela fórmula: `IMC = peso / altura²`  
Escreva um script que:
1. Solicite o **peso** (kg) e a **altura** (m) via `input()`
2. Calcule o IMC
3. Exiba o resultado com **2 casas decimais** e uma mensagem informativa

Saída esperada (exemplo):
```
IMC calculado: 24.18
Consulte um profissional de saúde para interpretação do resultado.
```

---

### 🟡 Exercício 13 – Operadores Lógicos e de Comparação
Sem usar estruturas `if`, escreva um script que armazene dois números e use `print()` para responder diretamente (True/False):
1. O primeiro número é maior que o segundo?
2. Os dois números são iguais?
3. O primeiro é positivo **E** o segundo é positivo?
4. Pelo menos um dos dois é maior que 100?
5. O primeiro número é diferente de zero?

---

### 🟡 Exercício 14 – Troca de Variáveis
Um desenvolvedor júnior escreveu o código abaixo para trocar os valores de duas variáveis, mas está errado. Corrija-o de **duas formas diferentes**: usando uma variável auxiliar e usando o método idiomático do Python (sem variável auxiliar):

```python
a = 10
b = 20
a = b
b = a
print(a, b)  # Esperado: 20 10 — mas está imprimindo 20 20
```

---

### 🟡 Exercício 15 – Calculadora de Desconto
Uma loja online aplica as seguintes regras de desconto:
- Compras acima de R$ 200,00 → 10% de desconto
- O desconto é calculado sobre o valor total

Escreva um script que:
1. Peça o **valor da compra** via `input()`
2. Calcule o desconto e o valor final
3. Exiba tudo formatado em reais

> 💡 *Não use `if` ainda — calcule o desconto diretamente com os operadores que você conhece. Use `float()` para converter o input.*

---

### 🔴 Exercício 16 – Distância entre Dois Pontos
Em um sistema de geolocalização, é necessário calcular a distância euclidiana entre dois pontos no plano cartesiano.

Fórmula: `d = √((x2 - x1)² + (y2 - y1)²)`

Escreva um script que:
1. Defina dois pontos: `P1 = (3, 4)` e `P2 = (7, 1)`
2. Calcule a distância usando `**` para potência e `** 0.5` para raiz (ou importe `math.sqrt`)
3. Exiba o resultado com 4 casas decimais

---

### 🔴 Exercício 17 – Análise de Nota Fiscal
Você precisa processar uma nota fiscal simples. Escreva um script que solicite via `input()`:
- Descrição do produto
- Quantidade (inteiro)
- Preço unitário (float)

E exiba:
```
===== NOTA FISCAL =====
Produto   : [descrição]
Quantidade: [qtd] unidade(s)
Preço Unit: R$ [preço unitário]
Subtotal  : R$ [quantidade × preço]
Imposto   : R$ [12% do subtotal]
Total     : R$ [subtotal + imposto]
=======================
```

---

### 🔴 Exercício 18 – Conversão de Unidades Encadeada
Escreva um script que converta uma distância em **metros** (informada pelo usuário) para:
- Quilômetros (÷ 1000)
- Centímetros (× 100)
- Milímetros (× 1000)
- Polegadas (× 39.3701)
- Pés (× 3.28084)

Exiba todos os resultados em uma tabela formatada com `f-strings` e alinhamento.

---

### 🔴 Exercício 19 – Manipulação de Strings no Mundo Real
Você recebeu um e-mail mal formatado de um cliente: `"   joao.silva@EMPRESA.com.br   "`  
Escreva um script que:
1. Armazene a string exatamente como mostrada acima
2. Remova os espaços em branco extras
3. Converta para letras minúsculas
4. Extraia o **nome de usuário** (parte antes do `@`)
5. Extraia o **domínio** (parte depois do `@`)
6. Exiba cada resultado em uma linha separada com uma label clara

> 💡 *Explore métodos de string: `.strip()`, `.lower()`, `.split('@')`*

---

### 🔴 Exercício 20 – Calculadora de Investimento Simples
Um cliente quer saber o retorno de uma aplicação financeira.  
Escreva um script que solicite:
- Capital inicial (R$)
- Taxa de juros ao mês (%)
- Período em meses

E calcule o **Montante** pela fórmula de juros simples: `M = C × (1 + i × t)`

Exiba:
```
Capital Inicial : R$ [valor]
Taxa Mensal     : [taxa]%
Período         : [meses] meses
Juros Totais    : R$ [juros]
Montante Final  : R$ [montante]
```

> 💡 *Lembre-se de converter a taxa percentual para decimal dividindo por 100.*

---

## 📊 Tabela Resumo dos Exercícios

| # | Tópico Principal | Nível | Dia |
|---|-----------------|-------|-----|
| 01 | `print()` básico | 🟢 | 1 |
| 02 | Módulo `sys`, ambiente | 🟢 | 1 |
| 03 | Zen of Python, `import` | 🟢 | 1 |
| 04 | Comentários e docstrings | 🟡 | 1 |
| 05 | Leitura e correção de erros | 🟡 | 1 |
| 06 | Tipos de dados e `type()` | 🔴 | 1 |
| 07 | Variáveis, operadores aritméticos | 🟢 | 2 |
| 08 | Expressões matemáticas | 🟢 | 2 |
| 09 | `input()`, `int()`, f-string | 🟢 | 2 |
| 10 | Divisão inteira `//` e módulo `%` | 🟢 | 2 |
| 11 | Formatação avançada com f-strings | 🟡 | 2 |
| 12 | `input()`, `float()`, operadores | 🟡 | 2 |
| 13 | Operadores lógicos e de comparação | 🟡 | 2 |
| 14 | Troca de variáveis | 🟡 | 2 |
| 15 | Expressões com desconto | 🟡 | 2 |
| 16 | `math`, potência, raiz quadrada | 🔴 | 2 |
| 17 | Nota fiscal, `input()`, formatação | 🔴 | 2 |
| 18 | Conversão encadeada, alinhamento | 🔴 | 2 |
| 19 | Métodos de string | 🔴 | 2 |
| 20 | Juros simples, fórmulas | 🔴 | 2 |

---

*Bons estudos! Lembre-se: o melhor código é aquele que você entende quando relê amanhã. 🐍*
