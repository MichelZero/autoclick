# Construa uma classe em Python que, ao ser instanciada, retorna um conjunto 
# contendo todos os números pares entre dois valores específicos, incluindo 
# esses valores. A classe recebe esses dois valores durante a inicialização.

class NumerosPares:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def obter_pares(self):
        if self.inicio % 2 != 0:
            self.inicio += 1  # Garante que o início seja um número par

        pares = {x for x in range(self.inicio, self.fim + 1, 2)}
        return pares


# Exemplo de uso
inicio = 10
fim = 20

numeros_pares = NumerosPares(inicio, fim)
pares = numeros_pares.obter_pares()

print(f'Números pares entre {inicio} e {fim}: {pares}')
print(type(pares))
