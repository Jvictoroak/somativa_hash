# Alexandre Andrioli Tucci
# João Victor Saboya Ribeiro de Carvalho
import json
import hashlib
import itertools
import string
import time

with open('usuarios.json', 'r') as arquivo:
    usuariosJson = json.load(arquivo)
def percorrerJson(json):
    inicio = time.time()
    usuariosJsonDescriptografado = []
    for i in range(4):
        usuariosJsonDescriptografado.append({
            'usuario': json[i]['usuario'],
            'senha': encontrarSha256(4, json[i]['senha'])
        })
        print(usuariosJsonDescriptografado)    
    fim = time.time()
    print('tempo total: ', fim-inicio)

def encontrarSha256(length, hash):
    characters = string.ascii_letters + string.digits + string.punctuation  # abc...XYZ0123...
    # Força bruta
    inicio = time.time()
    for combo in itertools.product(characters, repeat=length):
        attempt = ''.join(combo)
        attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

        if attempt_hash == hash:
            fim = time.time()
            print(fim-inicio)
            return attempt
            break
    else:
        print("Senha não encontrada.")

percorrerJson(usuariosJson)
