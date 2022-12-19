import base 
import login
import menu
# Admin - Admin

def start():
    base.init_base()
    menu.get_menu(login.user_login())

start()