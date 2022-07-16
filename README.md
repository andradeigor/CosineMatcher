# CosineMatcher

Projeto desenvolvido por [Igor Andrade](https://github.com/andradeigor). Este projeto foi feito como projeto final da disciplina Algebra Linear Algorítmica, consiste em uma implementação do cosseno para servir como um Template Matching.

- [Como usar](#como-usar)
- [Demonstração](#demonstração)
- [Responsividade](#responsive)
- [Tecnologias](#tecnologias)
- [Contribuidores](#contribuidores)
- [Licença](#licença)

## 🖋 Teoria:

### Para entender este projeto é preciso ter em mente como funciona o cálculo do cosseno em Álgebra Linear:

![graph](https://user-images.githubusercontent.com/21049910/179328904-26d99ad5-de1e-4368-95c8-743d9869ec10.png)

### O Cosseno entre os vetores A e B pode ser calculado da seguinte forma:

## $cos(A,B) = \frac{A'.B}{||A||\; ||B||}$

### Outra coisa que vale chamar atenção é que o cosseno entre dois ângulos varia de [ -1 , 1 ], e ele pode ser interpretado como o quão próximo dois vetores são. Embora não seja uma métrica perfeita, ele irá resultar em 1 caso um vetor(A) seja uma combinação linear do outro vetor(B). E irá retornar 0 caso os vetores sejam perpendiculares. Assim, podemos ver o cos como uma % do quão próximo o nosso vetor é de outro.

### Agora que entendemos o que é o cos e como ele é definido, precisamos entender como calcular ele, e como traduzir isso para computação. Começaremos entendendo o numerador da operação:

### Considere A, B dois vetores em $R^2$ de modo que $A= [x_1,x_2]$ e $B=[y_1,y_2]$

## $A'.B= x_1*y_1+x_2*y_2$

### Uma forma de escrever isso mais genérico e em "matemática" seria:

## ${\displaystyle \sum_{i=1}^{k} x_i*y_i}$

### Uma das vatagens de escrever nessa notação é que independente de qual dimensão esteja nossos vetores, essa formula vai funcionar. Não só isso, como também é inderessante notar que mesmo que não sejamos capaz de imaginar o que seria o cosseno entre dois vetores em $R^n$ essa forma de escrever ele não só nos permite calcular, como também nos dá de fato uma medida de semelhança entre esses dois vetores.

### Agora, falta analizarmos a parte do denominador da formula do cosseno:

### Seja A um vetor qualquer em $R^2$ tal que $A=[x_1,x_2]$ dizemos que:

## $||A||^2 = A'.A$

### Por comparação com a formula acima, podemos concluir que:

## $||A||^2 = A'.A = x_1^2+x_2^2$

### Assim:

## $||A||^2 = x*1^2+x_2^2 = {\displaystyle \sum*{i=1}^{k} x_i^2} $

### Por fim, temos que:

## $||A||= {\sqrt{\displaystyle \sum\_{i=1}^{k} x_i^2}} $

### Agora, finalmente podemos "ver" como calcular o cosseno entre dois vetores de forma mais "matemática", que também é uma forma mais simples de ser implementada computacionalmente:

## $cos(A,B) = \frac{A'.B}{||A||\; ||B||} = \frac{\displaystyle \sum_{i=1}^{k} x_i*y_i}{\sqrt{\displaystyle \sum_{i=1}^{k} x_i^2 * \displaystyle \sum_{i=1}^{k} y_i^2}}$

### Em estetística, essa formula é chamada de "Pearson correlation coefficient". Aqui, podemos ver que ela nada mais é do que cosseno entre dois vetores.

### Por fim, um "truque" que muitas vezes é usado quando estamos calculando essa correlação entre dois vetores é tirar a média de todos os pontos envolvidos naquele vetor. Imagine a seguinte situação:

![graph2](https://user-images.githubusercontent.com/21049910/179334430-af0221f8-b277-4cc7-9d84-1c7c9fecef59.png)

### Queremos calcular o cosseno entre dois pontos: G e J. Entretanto, se considerarmos seus vetores como vindo da origem, iremos ter uma relação que não reflete como eles se relacionam dentro do seu universo de pontos. Para corrigir isso, é comum retirarmos a média entre todos os pontos envolvidos, isso faz com que todos os pontos sejam "transladados" para a original. Uma outra forma de entender é que a origem passa a ser o ponto M(verde na figura). Assim, temos finalmente a versão mais comum da formula:

## $cos(A,B) = \frac{A'.B}{||A||\; ||B||} = \frac{\displaystyle \sum_{i=1}^{k} (x_i-\overline{x})*(y_i-\overline{y})}{\sqrt{\displaystyle \sum_{i=1}^{k} (x_i-\overline{x})^2 * \displaystyle \sum_{i=1}^{k} (y_i-\overline{y})^2}}$

## 🤖 Como Usar:

Rodando o Servidor localmente

```bash
 # Clone esse repositório
 $ git clone https://github.com/andradeigor/ts-landing-page

 # Acesse a pasta do projeto
 $ cd ts-landing-page

 # Instale dependências
 $ yarn

 # Starte o Projeto
 $ yarn start

```

## 📜 Demonstração:

![demonstration](https://media1.giphy.com/media/6vwUeAP0tN2sI3nQZY/giphy.gif?cid=790b76118a124e0d1427f4c892d9af8e7b7c997496567ce0&rid=giphy.gif&ct=g)

## 📜 Reponsividade:

![responsive](https://media0.giphy.com/media/S5wV4tHJlQq2YMAen8/giphy.gif?cid=790b7611de91134d28c6feb0c04c2ef9bcc38537df01c458&rid=giphy.gif&ct=g)

## 💻 Tecnologias

- React
- Typescript
- React-Hook-Form
- Styled Components

## 👥 Contribuidores

Esses são os contribuidores do projeto (<a href="https://allcontributors.org/docs/en/emoji-key">emoji key</a>).
\

<table>
  <tr>
    <td align="center"><a href="https://github.com/andradeigor"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/21049910?v=4" width="100px;" alt=""/><br /><sub><b>Igor Andrade</b></sub></a><br /><a href="https://github.com/andradeigor/DiscordBotUFRJ/commits?author=andradeigor" title="Igor Andrade">🤔 💻 🚧</a></td>
  </tr>
</table>

## 📖 Licença

Este projeto está licenciado sob a licença <a href="https://choosealicense.com/licenses/mit/">MIT</a>.
