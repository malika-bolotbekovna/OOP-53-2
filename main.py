# import my_module as md 
# print(md.add(3, 4))


# from my_module import add, Test
# print(add(3, 4))


# from my_pac import add, min

# print(add.add(3, 5))
# print(min.min(8, 5))



# from my_pac_2.classes import Test1, Test2
# from my_pac_2 import Test1, Test2

# print(type(Test1))
# print(type(Test2))

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')



# import requests

# answer = requests.get(url="https://fanat.geekstudio.kg/api/v1/block/about_us/")
# print(answer)


# from tkinter import *

# from my_pac_2.classes import *

# print(Test1)
# print(Test2)

# from flet import Page

# import flet as ft

# def main(page: ft.Page):
#     page.title = "Flet counter example"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()

#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()

#     page.add(
#         ft.Row(
#             [
#                 ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.Icons.ADD, on_click=plus_click),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         )
#     )

# ft.app(main)

# doesn't work
# from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)