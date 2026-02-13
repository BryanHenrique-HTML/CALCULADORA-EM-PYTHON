import flet as ft


# TEMAS

TEMA_ESCURO = {
    "FUNDO": ft.Colors.BLACK,
    "NUM": "#333333",
    "FUNC": "#A5A5A5",
    "OP": "#FF9F0A",
    "TEXTO": ft.Colors.WHITE
}


TEMA_CLARO = {
    "FUNDO": ft.Colors.WHITE,
    "NUM": "#E5E5E5",
    "FUNC": "#B1B1B1",
    "OP": "#FF9F0A",
    "TEXTO": ft.Colors.BLACK
}



COR_FUNDO = "#000000"
COR_NUM = "#333333"
COR_FUNC = "#A5A5A5"
COR_OP = "#FF9F0A"

botoes = [
    {'operador': 'AC', 'tipo': 'FUNC'},
    {'operador': '±', 'tipo': 'FUNC'},
    {'operador': '%', 'tipo': 'FUNC'},
    {'operador': '⌫', 'tipo': 'FUNC'},

    {'operador': '7', 'tipo': 'NUM'},
    {'operador': '8', 'tipo': 'NUM'},
    {'operador': '9', 'tipo': 'NUM'},
    {'operador': '*', 'tipo': 'OP'},

    {'operador': '4', 'tipo': 'NUM'},
    {'operador': '5', 'tipo': 'NUM'},
    {'operador': '6', 'tipo': 'NUM'},
    {'operador': '-', 'tipo': 'OP'},

    {'operador': '1', 'tipo': 'NUM'},
    {'operador': '2', 'tipo': 'NUM'},
    {'operador': '3', 'tipo': 'NUM'},
    {'operador': '+', 'tipo': 'OP'},

    {'operador': '0', 'tipo': 'NUM'},
    {'operador': '.', 'tipo': 'NUM'},
    {'operador': '=', 'tipo': 'OP'},
    {'operador': '/', 'tipo': 'OP'},
]

def main (page: ft.Page):
    tema_atual = TEMA_ESCURO
    historico_completo = []
    page.bgcolor = tema_atual["FUNDO"]
    page.animate_bgcolor = ft.Animation(400, ft.AnimationCurve.EASE_IN_OUT)
    page.window_resizable = False
    page.window_width = 250
    page.window_height = 380
    page.title = 'CALCULADORA_SIMPLES'
    

    history = ft.Text(value ="", color=ft.Colors.GREEN_400, size=14)

    result = ft.Text(
        value= '0', 
        color=tema_atual["TEXTO"],
        size=30,
        width=230,
        text_align=ft.TextAlign.RIGHT
        )
    

    btn_containers = []

    def toggle_tema(e):
        nonlocal tema_atual
        tema_atual = TEMA_CLARO if tema_atual == TEMA_ESCURO else TEMA_ESCURO

    # Fundo e textos
        page.bgcolor = tema_atual["FUNDO"]
        result.color = tema_atual["TEXTO"]
        history.color = tema_atual["TEXTO"]

    # Ícone do toggle
        if tema_atual == TEMA_CLARO:
         toggle.icon = ft.Icons.DARK_MODE
         toggle.icon_color = ft.Colors.BLACK
        else:
           toggle.icon = ft.Icons.LIGHT_MODE
           toggle.icon_color = ft.Colors.WHITE

        btn_historico.icon_color = ft.Colors.BLACK if tema_atual == TEMA_CLARO else ft.Colors.WHITE
   
        for i, item in enumerate(botoes):
           btn_containers[i].bgcolor = tema_atual[item['tipo']]
           btn_containers[i].content.color = tema_atual["TEXTO"]   

        page.update()

    toggle = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        icon_color=ft.Colors.WHITE,
        on_click=toggle_tema
    )

    def mostrar_historico(e):
        dialog.content = ft.Column(
            [ft.Text(linha) for linha in historico_completo]
            if historico_completo else [ft.Text("Nenhuma operação realizada ainda.")],
            scroll="auto",
            expand=True
        )

        dialog.actions = [
            ft.TextButton("fechar", on_click=fechar_dialog)
        ]

        if dialog not in page.overlay:
            page.overlay.append(dialog)

        dialog.open = True
        page.update()

    
    def fechar_dialog (e=None):
        dialog.open = False
        page.update()

    btn_historico = ft.IconButton(
        icon=ft.Icons.ACCESS_TIME,
        icon_color=ft.Colors.WHITE,
        on_click=mostrar_historico,
    )

    dialog = ft.AlertDialog(title = ft.Text("Histórico"), modal=True) 
    


    def calculate():
        try:
            allowed = "0123456789+-*/."
            for char in result.value:
                if char not in allowed:
                    return 'Erro'
                
            valor = eval(result.value)
            if isinstance(valor, float):
                valor = round(valor, 5)
                valor = f"{valor:.5f}".rstrip('0').rstrip('.')

            return str(valor)
        except:
            return 'Erro'      

    def select(e):
        current = result.value
        clicked = e.control.content.value
        operators = ('/', '*', '-', '+')

        if clicked == 'AC':
            result.value = '0'

        elif clicked == '⌫':
            if len(current) > 1:
                result.value = current[:-1]
            else:
                result.value = '0'        

        elif clicked == '%':
            try:
                for op in ('+', '-', '*', '/'):
                    if op in current:
                        base,percent = current.rsplit(op, 1)
                        base = float(base)
                        percent = float(percent) / 100

                        if op =='+':
                            result.value = str(base + (base * percent))
                        elif op == '-':
                            result.value = str(base - (base * percent))
                        elif op == '*':
                            result.value = str(base * percent)
                        elif op == '/':
                            result.value = str(base / percent)
                        return
                result.value = str(float(current) / 100)
            except:
                result.value =  'Erro'                    

        elif clicked == '±':
            if current.startswith('-'):
                result.value = current[1:]

            else:
                if current != '0':
                    result.value = '-' + current           

        elif clicked.isdigit() or clicked  == '.':
            if clicked == '.':
                # paga o ultimo numero apos o ultimo operador 
                last_number = current.split('/')[-1].split('*')[-1].split('-')[-1].split('+')[-1]
                if '.' in last_number:
                    return # bloqueia o segundo ponto 
            if current == '0':    
                result.value = clicked
            else:
                result.value = current + clicked

        elif clicked in operators:
            if current[-1] in operators:
                # SUBSTITUI o operador
                result.value = current[:-1] + clicked
            else:
                result.value = current + clicked
        elif clicked == '=':
            resultado = calculate()
            result.value = resultado
            historico_completo.append(f"{current} = {resultado}")


    display = ft.Container(
        content=ft.Column(
            controls=[
                history,
                result
            ],
            horizontal_alignment=ft.CrossAxisAlignment.END
        ),
        padding=ft.padding.only(right=10, bottom=10),
        height=80,
        alignment= ft.Alignment.CENTER_RIGHT
    )
    
    for item in botoes:
         btn = ft.Container(
            content=ft.Text(
                value=item['operador'],
                color=tema_atual["TEXTO"]
            ),
            width=50,
            height=50,
            bgcolor=tema_atual[item['tipo']],
            border_radius=25 if item['operador'] == '0' else 100,
            alignment=ft.Alignment.CENTER,
            on_click=select,
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            shadow=[
                ft.BoxShadow(
                   blur_radius=8,
                   offset=ft.Offset(0, 2),
                   color=ft.Colors.with_opacity(0.25, ft.Colors.BLACK)
                )
            ]

         )
         btn_containers.append(btn)


    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn_containers,
        alignment=ft.MainAxisAlignment.END
    )


    page.add(
        ft.Row(
            controls=[toggle, btn_historico],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=230
            ),
        display,
        keyboard
    )
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
