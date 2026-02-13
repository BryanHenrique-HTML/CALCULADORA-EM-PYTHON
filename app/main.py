import flet as ft
from model import CalculatorModel
from controller import CalculatorController
from view import construir_interface




def main(page: ft.Page):
    model = CalculatorModel()
    controller = CalculatorController(model)
    construir_interface(page, controller, model)


ft.run(main)
