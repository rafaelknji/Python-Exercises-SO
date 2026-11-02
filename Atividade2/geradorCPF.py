## Crie um aplicativo que gere 30 cpfs válidos

import random

for i in range(30):
    cpf = ""

    for j in range(11):
        cpf += str(random.randint(0, 9))

    print(f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")