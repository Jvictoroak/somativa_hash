# Alexandre Andrioli Tucci
# João Victor Saboya Ribeiro de Carvalho
import json
from hashlib import sha256
import os

if not os.path.exists('usuariosSecao3.json'):
    with open('usuariosSecao3.json', 'w') as arquivo:
        json.dump([], arquivo, indent=4)

def cripitografarSenha(senha, salt=None):
    if salt is None:
        salt = os.urandom(15)
    senha_bytes = senha.encode('utf-8')
    senha_salt = senha_bytes + salt
    senha_hash = sha256(senha_salt).hexdigest()
    return [senha_hash, salt]

def cadastro(usuario, senha):
    senha_hash, salt = cripitografarSenha(senha)

    data = {
        'usuario': usuario,
        'senha': senha_hash,
        'salt': list(salt),
    }

    with open('usuariosSecao3.json', 'r') as arquivo:
        usuarios = json.load(arquivo)

    usuarios.append(data)

    with open('usuariosSecao3.json', 'w') as arquivo:
        json.dump(usuarios, arquivo, indent=4)

    print('Cadastro realizado com sucesso.')
    login(usuario, senha)

def login(usuario, senha):
    with open('usuariosSecao3.json', 'r') as arquivo:
        usuarios = json.load(arquivo)

    for usuario_salvo in usuarios:
        if usuario_salvo['usuario'] == usuario:
            salt = bytes(usuario_salvo['salt'])  # converte lista de volta para bytes
            senha_hash, _ = cripitografarSenha(senha, salt)
            if usuario_salvo['senha'] == senha_hash:
                print('Usuário autenticado com sucesso.')
                return
            break

    print('Usuário não autenticado.')

def interface():
    print('1. Cadastro')
    print('2. Login')
    opcao = int(input('Selecione a opção desejada: '))
    if opcao == 1:
        cadastro(input('Usuário: '), input('Senha: '))
    elif opcao == 2:
        login(input('Usuário: '), input('Senha: '))
    else:
        print('Opção inválida.')

interface()
