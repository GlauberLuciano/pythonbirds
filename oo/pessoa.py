class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá Mundo'


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
    alanna.sobrenome = 'Caraciola'
    print(alanna.sobrenome)
    print((glauber.__dict__))
    print((alanna.__dict__))
    del glauber.filhos
    print(glauber.__dict__)
    print()
    Pessoa.olhos = 4
    print(Pessoa.olhos)
    print(glauber.olhos)
    alanna.olhos = 1
    print(alanna.olhos)
    print((alanna.__dict__))
    del alanna.olhos
    print(alanna.olhos)
