
class Atleta:
    def __init__(self, nome,idade, peso, aposentado):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.aposentado= aposentado

    def status(self):
         print(f"{self.nome},  {self.idade} anos, pesa {self.peso} "
               f"kg,aposentado" if self.aposentado else "ativo")


class Corredor (Atleta):
        def Correr(self):
            if not self.aposentado:
                print(f"{self.nome} está correndo.")
            else:
                print(f"{self.nome} está aposentado e não pode correr.")
class Nadador (Atleta):
        def Nadar(self):
            if not self.aposentado:
                print(f"{self.nome} está nadando.")
            else:
                print(f"{self.nome} está aposentado e não pode nadar.")

class Ciclista (Atleta):
        def Pedalar(self):
            if not self.aposentado:
                print(f"{self.nome} está pedalando.")
            else:
                print(f"{self.nome} está aposentado e não pode pedalar.")