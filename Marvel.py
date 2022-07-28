#Biblioteca usada como interface para o Algoritmo MD5
import hashlib 
import time
import requests

#Chaves de API para aplicação
#private key
particular = '8e984e6f3db7d42835691daf235f24d965e4ae09'
#public key
publica = '38319c4f351525a37a246d1629a65bbe'


#Construindo o MD5
#Chamando a função para criptografar
m = hashlib.md5()
#Coleta o tempo atual 
ts = str(time.time())
#Adicionando todas as parcelas de criptografia na forma de bytes
m.update(bytes(ts,'utf-8')) # O tempo atual  
m.update(bytes(particular,'utf-8'))
m.update(bytes(publica,'utf-8'))
hasht = m.hexdigest() # Cria o MD5

#Montando URL de requisição 
base = "https://gateway.marvel.com" #Página base para todas as requisições 
personagem = input("Digite o nome em inglês do personagem: \n")
requisicao = "\v1\public\characters?name=" + personagem + "&orderBy=name&limit=1" # oque queremos da requisicao

#Juntando todas as partes da URL
URL = base + requisicao + "&ts" + ts + "&apikey" + publica + "&hash=" + hasht
#Fazendo a requisição

dados = requests.get(URL).json()  

#Verificia se existe uma descrição dentro dos dados recebidos 

try:
   # descricao = dados["data"]["results"][0]["description"]
   descricao = dados["data"]["results"][0]["description"]
except:
    exit("Você digitou um personagem inválido")
print(descricao) 
