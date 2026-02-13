class CalculatorModel:
    def __init__(self):
        self.valor_atual = "0"
        self.historico = []

    def resetar(self):
        self.valor_atual = "0"
