class Pessoa:
    def cumprimentar(self):
        return f'Olá Glauber  {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(id(p))
