from abc import ABC, abstractmethod

class Pagavel(ABC):
    @abstractmethod
    def calcular_pagamento(self):
        pass

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioCLT(Funcionario, Pagavel):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal

    def calcular_pagamento(self):
        return self.calcular_salario()


class Freelancer(Funcionario, Pagavel):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

    def calcular_pagamento(self):
        return self.calcular_salario()

funcionarios = [
    FuncionarioCLT("Ana", 3000),
    Freelancer("Carlos", 120, 50)
]

for f in funcionarios:
    print(f"{f.nome} receberá R$ {f.calcular_pagamento():.2f}")
