class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá Glauber  {id(self)}'

if __name__ == '__main__':
    glauber = Pessoa(nome='Glauber')
    alanna = Pessoa(glauber, nome='Alanna')
    print(Pessoa.cumprimentar(alanna))
    print(alanna.cumprimentar())
    print(id(alanna))
    print(alanna.nome)
    print((alanna.idade))
    for filho in alanna.filhos:
        print((filho.nome))


