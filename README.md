# DerivadorDeGramatica
    
### Alunos: Augusto Savi e Gean Homem Marzarroto

## :information_source:  Tecnologias Usadas

:snake: Python

## :information_source: Executando localmente on Linux
To clone and run this application, you'll need [Git](https://git-scm.com),. From your command line:

```bash
#Verifique se você tem o python instalado
$ python3 --version

#caso não o tenha instalado, sigo os seguintes passos
$ sudo apt-get update
$ sudo apt-get install python3.6

# instale o tkinter(Usado para gerar a interface grafica)
$ sudo apt install python3-tk

# Clone esse repositorio
$ git clone https://github.com/AugustoSavi/DerivadorDeGramatica.git

# Caminhe ate a pasta 
$ cd DerivadorDeGramatica

# Execute o main.py
$ python3 main.py
```
## :information_source: Como Utilizar o Programa :information_source:

### Ao executar o programa aparecera essa tela:
![image](https://user-images.githubusercontent.com/32443720/94982042-ca333780-050d-11eb-887b-a91ca310b63a.png)

### Caso não queira utilizar os exemplos, ensira a gramatica linha a linha no input e clique no botão input  
![image](https://user-images.githubusercontent.com/32443720/94982076-f949a900-050d-11eb-94e4-670421462aa3.png)

### Apos clicar no botão input a linha ira aparecer no TextBox
![image](https://user-images.githubusercontent.com/32443720/94982130-8260e000-050e-11eb-8b63-fda5f82d300b.png)


###  Apos terminar de informar a gramatica, informe em "Não terminal" por onde derivação deve começar, após isso é só clicar em "Start"
![image](https://user-images.githubusercontent.com/32443720/94982178-ed121b80-050e-11eb-9c2e-1d499c6ed77a.png)


### Após Clicar em "Start" a derivação ira ocorrer
![image](https://user-images.githubusercontent.com/32443720/94982218-3b271f00-050f-11eb-8588-e7e1e7ad52d3.png)

### O botão "limpar gramatica" Limpa todos os campos e a gramatica
![image](https://user-images.githubusercontent.com/32443720/94982277-8d684000-050f-11eb-9c06-b219cca90786.png)

### Caso sua gramatica fique em loop utilize o "Stop"
![image](https://user-images.githubusercontent.com/32443720/94982303-c3a5bf80-050f-11eb-86c4-0fdda4bf11cf.png)

### Os exemplos preenchem automaticamente a gramatica e o não terminal inicial, basta clicar em Start 
![image](https://user-images.githubusercontent.com/32443720/94982320-ea63f600-050f-11eb-923a-2bd88329ffc9.png)

## :information_source: Exemplos

### Exemplo 1
```
S = aCb
C = ab
```

### Exemplo 2
```
S = Cde|deA
A = Ea|D|S
C = ded
D = deA|S
E = ead
```


### Exemplo 3

```
S = ABC
C = BaB | c
B = b | bb
A = a
```