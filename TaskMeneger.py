import flet as ft
import time


def main(page: ft.Page):

    def checkbox_activate(checkbox):
        '''
        Удалим дело после нажатия checkbox
        '''
        checkbox.visible = False
        time.sleep(1)
        page.update()

    def add_task(e):
        # Добавим чекбокс
        new_checkbox = ft.Checkbox(label=new_task.value, on_change=lambda e: checkbox_activate(new_checkbox))
        page.add(new_checkbox)

        # Обновим поле с текстом
        new_task.value = ''
        new_task.focus()
        page.update()

    def use_enter(e):
        '''
        Попробуем настроить, чтобы добавлялось действие
        при нажатии на Enter
        '''
        add_task(e)

    new_task = ft.TextField(label='Что нужно сделать?', on_submit=use_enter)
    button = ft.ElevatedButton(text='Добавить!', on_click=add_task)

    page.add(ft.Row(controls=[new_task, button]))

    new_task.focus()

ft.app(target=main)
