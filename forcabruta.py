# import hashlib
# print(hashlib.sha256("A".encode()).hexdigest()) # 559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd

import hashlib
import itertools
import string

# Hash SHA-256 da senha alvo (ex: hash da senha "Ab1!")
target_hash = "559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd"

# Conjunto de caracteres possíveis (você pode incluir símbolos se quiser)
characters = string.ascii_letters + string.digits + string.punctuation  # abc...XYZ0123...

# Tamanho da senha (exatos 4 caracteres)
length = 4

# Força bruta
for combo in itertools.product(characters, repeat=length):
    attempt = ''.join(combo)
    attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

    if attempt_hash == target_hash:
        print(f"Senha encontrada: {attempt}")
        break
else:
    print("Senha não encontrada.")
