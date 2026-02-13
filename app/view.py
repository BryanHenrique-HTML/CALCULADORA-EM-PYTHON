import flet as ft
from flet import Colors

TEMA_ESCURO = {
    "FUNDO": ft.Colors.BLACK,
    "NUM": "#333333",
    "FUNC": "#A5A5A5",
    "OP": "#FF9F0A",
    "TEXTO": Colors.WHITE,
}

TEMA_CLARO = {
    "FUNDO": ft.Colors.WHITE,
    "NUM": "#E5E5E5",
    "FUNC": "#B1B1B1",
    "OP": "#FF9F0A",
    "TEXTO": Colors.BLACK,
}

botoes = [
    {"operador": "AC", "tipo": "FUNC"},
    {"operador": "±", "tipo": "FUNC"},
    {"operador": "%", "tipo": "FUNC"},
    {"operador": "⌫", "tipo": "FUNC"},
    {"operador": "7", "tipo": "NUM"},
    {"operador": "8", "tipo": "NUM"},
    {"operador": "9", "tipo": "NUM"},
    {"operador": "*", "tipo": "OP"},
    {"operador": "4", "tipo": "NUM"},
    {"operador": "5", "tipo": "NUM"},
    {"operador": "6", "tipo": "NUM"},
    {"operador": "-", "tipo": "OP"},
    {"operador": "1", "tipo": "NUM"},
    {"operador": "2", "tipo": "NUM"},
    {"operador": "3", "tipo": "NUM"},
    {"operador": "+", "tipo": "OP"},
    {"operador": "0", "tipo": "NUM"},
    {"operador": ".", "tipo": "NUM"},
    {"operador": "=", "tipo": "OP"},
    {"operador": "/", "tipo": "OP"},
]


def construir_interface(page, controller, model):
    tema_atual = TEMA_ESCURO
    page.bgcolor = tema_atual["FUNDO"]
    page.window_resizable = False
    page.window_width = 250
    page.window_height = 380
    page.title = "CALCULADORA_SIMPLES"
    page.window_always_on_top = True

    resultado = ft.Text(
        value=model.valor_atual,
        color=tema_atual["TEXTO"],
        size=30,
        text_align=ft.TextAlign.RIGHT,
        width=230,
    )

    btns = []

    def on_click(e):
        atual = resultado.value
        click = e.control.content.value
        ops = ("+", "-", "*", "/")

        if click == "AC":
            resultado.value = "0"

        elif click == "⌫":
            resultado.value = atual[:-1] if len(atual) > 1 else "0"

        elif click == "%":
            resultado.value = controller.aplicar_porcentagem(atual)

        elif click == "±":
            if atual.startswith("-"):
                resultado.value = atual[1:]
            elif atual != "0":
                resultado.value = "-" + atual

        elif click == "=":
            resultado.value = controller.calcular(atual)
            model.historico.append(f"{atual} = {resultado.value}")

        elif click in ops:
            resultado.value = atual[:-1] + click if atual[-1] in ops else atual + click

        else:
            resultado.value = click if atual == "0" else atual + click

        page.update()

    for item in botoes:
        btn = ft.Container(
            content=ft.Text(item["operador"], color=tema_atual["TEXTO"]),
            width=50,
            height=50,
            bgcolor=tema_atual[item["tipo"]],
            alignment=ft.Alignment.CENTER,
            border_radius=25 if item["operador"] == "0" else 100,
            on_click=on_click,
        )
        btns.append(btn)

    page.add(
        resultado,
        ft.Row(btns, wrap=True, width=250),
    )
