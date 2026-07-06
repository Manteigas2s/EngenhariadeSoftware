from login import Login
from menu import Menu

login = Login()

if login.autenticar():
    menu = Menu()
    menu.iniciar()