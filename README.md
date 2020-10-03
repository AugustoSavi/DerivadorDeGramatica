# DerivadorDeGramatica
    
### Alunos : Augusto Savi e Gean Homem Marzarroto

## :information_source:  Tecnologias Usadas

* Python

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
## :information_source: Atenção

Ainda esta em desenvolvimento


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