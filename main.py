import json
from hashlib import sha256

usuario = input('Usuario:')
senha = input('Senha:')

def cadastro(usuario, senha):
    senha_hash = cripitografarSenha(senha)
    data = {
        'usuario': usuario,
        'senha': senha_hash
    } 

    with open('usuarios.json', 'r') as arquivo:
        usuariosJson = json.load(arquivo)
    usuariosJson.append(data)
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuariosJson, arquivo, indent=4)


def cripitografarSenha(senha):
    senha_bytes = senha.encode('utf-8')
    senha_hash = sha256(senha_bytes)
    senha_hex = senha_hash.hexdigest()
    return senha_hex

cadastro(usuario, senha)
