# CosineMatcher

Projeto desenvolvido por [Igor Andrade](https://github.com/andradeigor). Este projeto foi feito como projeto final da disciplina Álgebra Linear Algorítmica, consiste em uma implementação do cosseno para servir como um Template Matching.

* [Teoria](#🖋-teoria)
* [Implementação](#💻-implementação)
* [Como Usar](#🤖-como-usar)
* [Demonstração](#📜-demonstração)
* [Tecnologias](#💻-tecnologias)
* [Contribuidores](#👥-contribuidores)
* [Licença](#📖-licença)

## 🖋 Teoria:
Para entender este projeto é preciso ter em mente como funciona o cálculo do cosseno em Álgebra Linear:

![graph](https://user-images.githubusercontent.com/21049910/179328904-26d99ad5-de1e-4368-95c8-743d9869ec10.png)

O Cosseno entre os vetores A e B pode ser calculado da seguinte forma:

$$cos(A,B) = \frac{A'.B}{||A|| ||B||}$$

Outra coisa que vale chamar atenção é que o cosseno entre dois vetores varia de [ -1 , 1 ], e ele pode ser interpretado como o quão próximo dois vetores são. Embora não seja uma métrica perfeita, ele irá resultar em 1 caso um vetor(A) seja uma combinação linear do outro vetor(B). E irá retornar 0 caso os vetores sejam perpendiculares. Assim, podemos ver o cos como uma % do quão próximo o nosso vetor é de outro.

Agora que entendemos o que é o cos e como ele é definido, precisamos entender como calcular ele, e como traduzir isso para computação. Começaremos entendendo o numerador da operação:

Considere A, B dois vetores em $R^2$ de modo que $A= [x_1,x_2]$ e $B=[y_1,y_2]$

$$A'.B= x_1* y_1+x_2 *y_2$$

Uma forma de escrever isso mais genérico e em "matemática" seria:

$${\displaystyle \sum_{i=1}^{k} x_i*y_i}$$

Uma das vantagens de escrever nessa notação é que independente de qual dimensão esteja nossos vetores, essa fórmula vai funcionar. Não só isso, como também é interessante notar que mesmo que não sejamos capaz de imaginar o que seria o cosseno entre dois vetores em $R^n$ essa forma de escrever ele não só nos permite calcular, como também nos dá de fato uma medida de semelhança entre esses dois vetores.

Agora, falta analisarmos a parte do denominador da fórmula do cosseno:

Seja A um vetor qualquer em $R^2$ tal que $A=[x_1,x_2]$ dizemos que:

$$||A||^2 = A'.A$$

Por comparação com a fórmula acima, podemos concluir que:

$$||A||^2 = A'.A = x_1^2+x_2^2$$

Assim:

$$||A||^2 = x_{1}^2+x_2^2 = {\displaystyle \sum_{i=1}^{k} x_i^2} $$

Por fim, temos que:

 $$||A||= {\sqrt{\displaystyle \sum_{i=1}^{k} x_i^2}} $$

Agora, finalmente podemos "ver" como calcular o cosseno entre dois vetores de forma mais "matemática", que também é uma forma mais simples de ser implementada computacionalmente:

$$cos(A,B) = \frac{A'.B}{||A||\; ||B||} = \frac{\displaystyle \sum_{i=1}^{k} x_i*y_i}{\sqrt{\displaystyle \sum_{i=1}^{k} x_i^2 * \displaystyle \sum_{i=1}^{k} y_i^2}}$$

 Em estatística, essa fórmula é chamada de "Pearson correlation coefficient". Aqui, podemos ver que ela nada mais é do que cosseno entre dois vetores.

Por fim, um "truque" que muitas vezes é usado quando estamos calculando essa correlação entre dois vetores é tirar a média de todos os pontos envolvidos naquele vetor. Imagine a seguinte situação:

![graph2](https://user-images.githubusercontent.com/21049910/179334430-af0221f8-b277-4cc7-9d84-1c7c9fecef59.png)

Queremos calcular o cosseno entre dois pontos: G e J. Entretanto, se considerarmos seus vetores como vindo da origem, iremos ter uma relação que não reflete como eles se relacionam dentro do seu universo de pontos. Para corrigir isso, é comum retirarmos a média entre todos os pontos envolvidos, isso faz com que todos os pontos sejam "transladados" para a origem. Uma outra forma de entender é que a origem passa a ser o ponto M(verde na figura). Assim, temos finalmente a versão mais comum da fórmula:

$$cos(A,B) = \frac{A'.B}{||A||\; ||B||} = \frac{\displaystyle \sum_{i=1}^{k} (x_i-\overline{x})*(y_i-\overline{y})}{\sqrt{\displaystyle \sum_{i=1}^{k} (x_i-\overline{x})^2 * \displaystyle \sum_{i=1}^{k} (y_i-\overline{y})^2}}$$

O objetivo desse trabalho é realizar esses cálculos para imagens, para fazer isso, basta entender que imagens são na verdade matrizes de pixel e estender os somatórios acima para duas dimensões. Fazendo isso, chegamos na mesma fórmula dada pela documentação do OpenCv para o cálculo de Template Matching:

![math](https://user-images.githubusercontent.com/21049910/179336556-37bf25c0-9646-42b8-abaf-30ef5889f53d.png)

Nessa fórmula, T e I são as matrizes do Template e Imagem, T' e I' são o valor da posição x,y menos a média.

## 💻 Implementação:
Queremos implementar o cosseno de modo que dada uma matriz I que seja mxn, um template T que seja kxj com k<=m e j<=n, nosso código percorra a matriz I de forma a gerar uma nova matriz R que contenha a % de semelhança entre T e a seção da matriz I naquela posição. Essa matriz R terá dimensões $(m-k+1)$ x $(n-j+1)$, assim, a posição de R que tiver a maior % será o melhor match em I para o nosso template:

![math](https://user-images.githubusercontent.com/21049910/179375527-e817b34e-1561-4236-9101-809f6c9f74e0.png)

Aqui, podemos ver claramente que a posição (1,1) possui a maior porcentagem, 100% neste caso, e se olharmos a matriz gerada nessa posição, podemos ver que de fato é onde o template se encontra.

Esse cálculo foi feito como relatado acima. Dado uma matriz I e o template T, criamos uma matriz de tamanho R e fazemos um loop que percorre essa matriz, calculando o cosseno em cada um dos pontos. O cálculo foi implementado da seguinte forma:

```python
def template_matching(I,T):
    w,h = T.shape
    W,H = I.shape
    mediaT = np.mean(T)
    results = np.zeros((W-w+1,H-h+1))
    for x in range(len(results)):
        for y in range(len(results[0])):
            results[x][y] = R(x,y,I,T,mediaT)
    return results
```

Aqui, a implementação do cálculo do cosseno:

```python
def R(x,y,I,T,mediaT):
    xt,yt = T.shape
    r_num = 0
    r_dem_T = 0
    r_dem_I = 0
    mediaI = np.mean(I[x:x+xt, y:y+yt])

    for xLinha in range(xt):
        for yLinha in range(yt):
            T_Linha = T[xLinha][yLinha] - mediaT
            I_Linha = I[x+xLinha][y+yLinha] - mediaI 
            r_num+= (T_Linha)*(I_Linha) 
            r_dem_T+= (T_Linha)**2
            r_dem_I += (I_Linha)**2

    r_dem = (math.sqrt((r_dem_T*r_dem_I)))
    if(r_dem ==0):
        return 0
    r = r_num/r_dem
    return r
``` 
Se abstrairmos um pouco o conceito de imagens, podemos interpretar imagens como matrizes. E, indo além, podemos usar esse algoritmo para procurar objetos dentro de imagens. É nisso que se foca esse projeto.

Agora, com isso em mente, podemos tomar a seguinte imagem como exemplo, e o seguinte template:

### Imagem:
![imagem](https://user-images.githubusercontent.com/21049910/179375714-a25f4e35-6a01-440d-879a-522880c804c3.png)

### Template:
![Template](https://user-images.githubusercontent.com/21049910/179375729-c0d76aaa-e166-488e-a144-548a4766c608.jpg)

Após o nosso algoritmo rodar por BASTANTE tempo(em torno de 10 minutos). Obtemos a matriz R, ao procurarmos o maior resultado dela e pegarmos o seu index, podemos desenhar um retângulo do tamanho do template em torno do local encontrado. Assim, confirmando que de fato nosso algoritmo funciona:

### Resultado:
![Resultado](https://user-images.githubusercontent.com/21049910/179375766-d140947f-904f-42ab-aa2e-a0ea6b32ff8a.png)

### Código:
```python
def main():
    template = cv2.imread("./templates/cano_top.png")
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    Image = cv2.imread("./templates/teste.png")
    Image_gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)

    y,x,_ = template.shape
    result_1 = template_matching(Image_gray,template_gray)
    result_1 = np.unravel_index(np.argmax(result_1, axis=None), result_1.shape)
    result_1 = result_1[::-1]
    Image = cv2.rectangle(Image, result_1, (result_1[0] + x, result_1[1] + y), (0,0,255),5)
    cv2.imshow("Eye", Image)
    cv2.waitKey(0)
```

Com isso, confirmamos que de fato nossa implementação funciona. Entretanto, para o propósito desse trabalho eu precisaria de uma implementação otimizada. Por ser algo fora do escopo do curso acabei por fazer o resto do trabalho utilizando a função disponível na biblioteca [OpenCV](https://docs.opencv.org/4.x/index.html). Assim, o que implementamos no final das contas foi um bot que utiliza cosseno como template matching para "zerar" Flappy Bird.

### Resultado Final:
![final](https://media.giphy.com/media/BZbFITdrcI54x2qYbF/giphy.gif)
## 🤖 Como Usar:

Rodando o Bot localmente

```bash
 # Clone esse repositório
 $ git clone https://github.com/andradeigor/CosineMatcher

 # Acesse a pasta do projeto
 $ cd CosineMatcher

 # Abre o Game.html no navegador e coloque em tela cheia

 # Starte o Projeto
 $ Python3 Main.py

```

## 📜 Demonstração:

![final](https://media.giphy.com/media/BZbFITdrcI54x2qYbF/giphy.gif)

## 💻 Tecnologias

- Python
- OpenCV
- Pygame
- mss
- pynput

## 👥 Contribuidores

Esses são os contribuidores do projeto (<a href="https://allcontributors.org/docs/en/emoji-key">emoji key</a>).


<table>
  <tr>
    <td align="center"><a href="https://github.com/andradeigor"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/21049910?v=4" width="100px;" alt=""/><br /><sub><b>Igor Andrade</b></sub></a><br /><a href="https://github.com/andradeigor/DiscordBotUFRJ/commits?author=andradeigor" title="Igor Andrade">🤔 💻 🚧</a></td>
  </tr>
</table>

## 📖 Licença

Este projeto está licenciado sob a licença <a href="https://choosealicense.com/licenses/mit/">MIT</a>.
