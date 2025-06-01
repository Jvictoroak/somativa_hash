# Alexandre Andrioli Tucci
# João Victor Saboya Ribeiro de Carvalho
import json
import hashlib
import itertools
import string
import time

with open('usuariosSecao1.json', 'r') as arquivo:
    usuariosJson = json.load(arquivo)

def percorrerJson(json, length):
    inicio = time.time()
    usuariosJsonDescriptografado = []
    for i in range(len(json)):
        usuario = json[i]['usuario']
        senha, tempo = encontrarSha256(length, json[i]['senha'])
        usuario_dict = {'usuario': usuario, 'senha': senha}
        usuariosJsonDescriptografado.append(usuario_dict)
        print(f"Tempo: {tempo}")
        print([usuario_dict])
    fim = time.time()
    print('\nTempo Total: ', fim-inicio)
    exit()

def encontrarSha256(length, hash):
    characters = string.ascii_letters + string.digits + string.punctuation 
    inicio = time.time()
    for combo in itertools.product(characters, repeat=length):
        attempt = ''.join(combo)
        attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()
        if attempt_hash == hash:
            fim = time.time()
            tempo = fim - inicio
            return attempt, tempo
    percorrerJson(usuariosJson, length+1)

percorrerJson(usuariosJson, 1)
