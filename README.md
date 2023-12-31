# Observer ![IFRN Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Instituto_Federal_do_Rio_Grande_do_Norte_-_Marca_Vertical_2015.svg/25px-Instituto_Federal_do_Rio_Grande_do_Norte_-_Marca_Vertical_2015.svg.png)


## Atividade de Padrões de Projeto


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/leonardolmai/) José Leonardo

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/MoisesMonter) Moisés Monteiro

Nesta atividade, vamos explorar o padrão de projeto Observer utilizando o Python 3.11.4 e o pip 23.1.2.

## UML 
### Resumo
Observer tem como padrão de projeto de software (comportamental), que permite em interações muitos-para-um entre objetos, onde quando haja modificação em um objeto também haja uma notificação em todos seus dependentes.


Objeto de  Modificação - é chamado de sujeito/observado

Objeto dependente - serão chamado de observadores e serão notificados

![Visualização do PDF](UML.png)

[UML OBSERVER](UML.png)

### Padrão Observer - Pontos Positivos e Negativos

O padrão Observer apresenta diversas vantagens, incluindo:

- **Baixo acoplamento entre objetos**: O padrão Observer permite que o sujeito (objeto observado) e os observadores (objetos dependentes) sejam independentes um do outro, facilitando a manutenção e a evolução do sistema.

- **Reusabilidade de componentes**: A adição e remoção de novos observadores podem ser feitas sem modificar o código do sujeito, tornando o sistema mais flexível e extensível.

- **Notificações customizadas**: Os observadores podem ser notificados apenas sobre eventos específicos que são relevantes para eles, permitindo comportamentos diferentes sem afetar os outros.

Entretanto, há também alguns pontos negativos a serem considerados:

- **Overhead**: O aumento no número de observadores pode levar a uma sobrecarga significativa nas notificações, especialmente se as operações dos observadores forem demoradas ou complexas.

- **Ordem de notificação indefinida**: A ordem em que os observadores são notificados não é garantida, o que pode ser problemático em cenários em que a ordem das notificações é importante para o comportamento do sistema.

- **Observadores desatualizados**: Observadores podem ser notificados sobre alterações que não são mais relevantes para eles, caso não desvinculem corretamente suas inscrições após seu uso, o que requer gerenciamento manual.

Com o padrão Observer, é possível alcançar um código mais flexível e modular, permitindo uma melhor organização das dependências entre os objetos em um sistema.

# Extrair UML do nosso Projeto Python

### Instalação

Antes de começarmos, verifique se você já tem o Python 3.11.4 instalado em seu sistema. Para verificar a versão do Python, execute o seguinte comando:
| Dependences | comand |
| ------ | ------ |
| Pip | --v |
| Python | --version |


Agora, vamos instalar o Pylint, que é uma ferramenta de análise de código para o Python, e o Graphviz, que é usado para renderizar diagramas UML.

```markdown
pip install pylint
pip install graphviz
```

| Framework | Version | More Dependences |
| ------ | ------ | ------ | 
| graphviz | 0.20.1 | https://www.graphviz.org/download/ |
| pylint | 2.17.5 | |

```markdown
ao terminar as duas instalações acesse https://graphviz.org/download/ para completar instalação de graphviz em sua maquina

```

### Gerando Diagramas UML com Pyreverse

Para gerar diagramas UML usando o Pyreverse, primeiro, certifique-se de que o Graphviz esteja instalado corretamente em seu sistema. Em seguida, vá para o diretório do seu projeto e execute o seguinte comando para gerar o arquivo .dot:


Através do Pylint utilizaremos o Pyreverse...

```markdown
Pyreverse faz parte do Pylint e é uma ferramenta que permite gerar diagramas UML a partir do código-fonte Python. Ele analisa o código e produz arquivos .dot contendo os diagramas de classes e/ou pacotes, fornecendo uma representação visual da estrutura do código.
```

## Criando arquivo .dot

Com pylint instalado Use o seguinte comando para gerar o arquivo .dot com o diagrama UML do no codigo observer.py

```markdown
pyreverse observer.py
```

### Convertendo .dot para PNG e PDF

Para converter o arquivo .dot gerado pelo Pyreverse em uma imagem PNG ou PDF, você pode usar o Graphviz. Execute o seguinte comando para converter para PNG:

```markdown
dot -Tpng classes.dot -o classes.png
```
E o seguinte comando para converter para PDF:

```markdown
dot -Tpdf classes.dot -o classes.pdf
```
Lembre-se de substituir `classes.dot` pelo nome do arquivo .dot gerado pelo Pyreverse caso seja necessário.

