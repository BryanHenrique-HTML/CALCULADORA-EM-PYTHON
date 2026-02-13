class CalculatorController:
    def __init__(self, model):
        self.model = model

    def calcular(self, expressao):
        try:
            allowed = "0123456789+-*/."
            for char in expressao:
                if char not in allowed:
                    return "Erro"

            valor = eval(expressao)

            if isinstance(valor, float):
                valor = round(valor, 5)
                valor = f"{valor:.5f}".rstrip("0").rstrip(".")

            return str(valor)
        except:
            return "Erro"

    def aplicar_porcentagem(self, expressao):
        try:
            for op in ("+", "-", "*", "/"):
                if op in expressao:
                    base, percent = expressao.rsplit(op, 1)
                    base = float(base)
                    percent = float(percent) / 100

                    if op == "+":
                        return str(base + (base * percent))
                    if op == "-":
                        return str(base - (base * percent))
                    if op == "*":
                        return str(base * percent)
                    if op == "/":
                        return str(base / percent)

            return str(float(expressao) / 100)
        except:
            return "Erro"
