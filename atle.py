from biblioteca import *
atleta1 = Corredor("lady gaga", 30, 70, False)
atleta2 = Nadador("virginia ", 28, 60, True)
atleta3 = Ciclista("Alexandre de moraes", 35, 75, False)

print(atleta1.status())
atleta1.Correr()

print(atleta2.status())
atleta2.Nadar()

print(atleta3.status())
atleta3.Pedalar()
