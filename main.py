import json
from hashlib import sha256


def cadastro(usuario, senha):
    if(len(usuario) != 4 or len(senha) != 4):
        print('o usuario e a senha devem ter 4 caracters')
        cadastro(input('Usuario:'), input('Senha:'))
        return
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
    print('Cadastro realizado com sucesso')
    login(usuario, senha)

def login(usuario, senha):
    senha_hash = cripitografarSenha(senha)
    with open('usuarios.json', 'r') as arquivo:
        usuariosJson = json.load(arquivo)
    for i in range(len(usuariosJson)):
        if(usuariosJson[i]['usuario'] == usuario and usuariosJson[i]['senha'] == senha_hash):
            print('usuario autenticado')
            return
    print('usuario não autenticado')

def cripitografarSenha(senha):
    senha_bytes = senha.encode('utf-8')
    senha_hash = sha256(senha_bytes)
    senha_hex = senha_hash.hexdigest()
    return senha_hex

def interface():
    print('1. Cadastro')
    print('2. Login')
    opcao = int(input('Seleciona a opção desejada: \n'))
    if(opcao == 1):
        cadastro(input('Usuario:'), input('Senha:'))
    elif(opcao == 2):
        login(input('Usuario:'), input('Senha:'))

 
interface()