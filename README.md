# Dillinger
## _The Last Markdown Editor, Ever_

rtical_2015.svg/50px-Instituto_Federal_do_Rio_Grande_do_Norte_-_Marca_Vertical_2015.svg.png)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/leonardolmai/)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/MoisesMonter)

# Observer

## Atividade de Padrões de Projeto

![IFRN Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Instituto_Federal_do_Rio_Grande_do_Norte_-_Marca_Ve

Nesta atividade, vamos explorar o padrão de projeto Observer utilizando o Python 3.11.4 e o pip 23.1.2.


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
### Gerando Diagramas UML com Pyreverse

Para gerar diagramas UML usando o Pyreverse, primeiro, certifique-se de que o Graphviz esteja instalado corretamente em seu sistema. Em seguida, vá para o diretório do seu projeto e execute o seguinte comando para gerar o arquivo .dot:

```markdown
O Pyreverse irá analisar seu código Python e gerar um arquivo .dot com o diagrama UML correspondente.
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
Lembre-se de substituir `classes.dot` pelo nome do arquivo .dot gerado pelo Pyreverse.

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
