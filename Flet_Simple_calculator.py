import flet as ft

def main(page: ft.Page):
    page.title = "Calc App"
    result = ft.TextField(value="0", text_size=50, width=400, height=200, text_align=ft.TextAlign.CENTER)

    status = 0

    def on_number_click(event, number):
        nonlocal status
        if status == 1:
            result.value = ""
            status = 0
            result.update()
            page.update()

        if result.value == "0":
            result.value = number
        else:
            result.value += number
        result.update()
        page.update()

    def on_clear_click(event):
        result.value = ""
        result.update()
        page.update()
    def remove_last_added(event):
        result.value = result.value[:-1]
        result.update()
        page.update()
    
    def pressed_solve(event):
        try:
            result.value = str(eval(result.value))
        except:
            result.value = "Error"
        nonlocal status
        status = 1
        result.update()
        page.update()


    page.add(
        ft.Row(controls=[result], alignment=ft.MainAxisAlignment.CENTER, spacing=20, expand=True, vertical_alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            controls=[
                ft.ElevatedButton(content = ft.Text("AC", size = 20),width = 100, height = 50, on_click=on_clear_click),
                ft.ElevatedButton(content = ft.Text("←", size = 20),width = 100, height = 50, on_click=lambda event: remove_last_added(event)),
                ft.ElevatedButton(content = ft.Text("%", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "%")),
                ft.ElevatedButton(content = ft.Text("/", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "/")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(content = ft.Text("7", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "7")),
                ft.ElevatedButton(content = ft.Text("8", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "8")),
                ft.ElevatedButton(content = ft.Text("9", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "9")),
                ft.ElevatedButton(content = ft.Text("*", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "*")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(content = ft.Text("4", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "4")),
                ft.ElevatedButton(content = ft.Text("5", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "5")),
                ft.ElevatedButton(content = ft.Text("6", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "6")),
                ft.ElevatedButton(content = ft.Text("-", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "-")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(content = ft.Text("1", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "1")),
                ft.ElevatedButton(content = ft.Text("2", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "2")),
                ft.ElevatedButton(content = ft.Text("3", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "3")),
                ft.ElevatedButton(content = ft.Text("+", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "+")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
             controls=[
                ft.ElevatedButton(content = ft.Text("0", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "0")),
                ft.ElevatedButton(content = ft.Text(".", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, ".")),
                ft.ElevatedButton(content = ft.Text("=", size = 20),width = 100, height = 50, on_click=lambda event: pressed_solve(event)),
                ft.ElevatedButton(content = ft.Text("=", size = 20),width = 100, height = 50, on_click=lambda event: on_number_click(event, "=")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
    )

ft.app(target=main)