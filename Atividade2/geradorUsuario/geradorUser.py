
import mysql.connector
import threading
import random
import string
import hashlib
import os
from queue import Queue

import os 
from dotenv import load_dotenv

load_dotenv()

fila = Queue()

def cadastrar():
    conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

    cursor = conexao.cursor()

    while True:
        usuario = fila.get()

        if usuario is None:
            fila.task_done()
            break

        nome, senha = usuario

        cursor.execute(
            "INSERT INTO usuarios (nome, senha) VALUES (%s, %s)",
            (nome, senha)
        )

        fila.task_done()

    conexao.commit()
    cursor.close()
    conexao.close()


for i in range(1000):
    nome = f"Usuario{i + 1}"

    senha = "".join(
        random.choices(string.ascii_letters + string.digits, k=10)
    )

    salt = os.urandom(16)
    hash_senha = hashlib.pbkdf2_hmac(
        "sha256", senha.encode(), salt, 100000
    )

    senha_segura = salt.hex() + ":" + hash_senha.hex()

    fila.put((nome, senha_segura))


thread = threading.Thread(target=cadastrar)
thread.start()

fila.put(None)
thread.join()

print("1000 usuários cadastrados!")
