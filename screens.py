import tkinter as tk
from guiproject.auth_service import register,login
from products_service import get_all_products

def clear_window(window):
    for child in window.winfo_children():#dava mi vsichki neshta na ekrana kato obekti
        child.destroy()#tova shte ni izchisti ekrana


def render_product_screen(window):
    clear_window(window)

    products = get_all_products()
    row = 0
    column=0
    for product in products:#3na3 go pravim
        if column == 3:
            row+=5
            column = 0
        tk.Label(window,text=product['name']).grid(row=row,column=column)
        tk.Label(window, text=product['img']).grid(row=row+1, column=column)
        tk.Label(window, text=f"Price: {product['price']}").grid(row=row+2, column=column)
        tk.Label(window, text=f"Count: {product['count']}").grid(row=row+3, column=column)
        tk.Button(window, text=f"Buy").grid(row=row+4, column=column)
        column+=1
def render_login_screen(window):
    clear_window(window)
    tk.Label(window, text='Enter your username:').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)  # izliza input s koito moga da pisha po nego

    tk.Label(window, text='Enter your password:').grid(row=1, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)  # pri showa kato vuvejdame neshto shte budat replacnati sus zvezdichka

    def on_login():
        username_value = username.get()
        password_value = password.get()

        result = login(username_value,password_value)
        if result:
            render_product_screen(window)
        else:
            tk.Label(window, text='Invalid credentials!', fg='red').grid(row=2, column=1)



    tk.Button(window, text='Login',
              bg='green',
              fg='black',
              command=on_login  # tova e reference
              ).grid(row=3, column=1)  # grida go slaga na mqstoto



def render_main_screen(window):
    tk.Button(window, text='Login',
              bg='green',
              fg='white',
              command=lambda:render_login_screen(window)
              ).grid(row=0,column=0)#grida go slaga na mqstoto
    tk.Button(window, text='Register',
              bg='yellow',
              fg='black',
              command=lambda: render_register_screen(window)
              ).grid(row=0, column=1)  # grida go slaga na mqstoto


def render_register_screen(window):
    clear_window(window)

    tk.Label(window,text='Enter your username:').grid(row=0,column=0)
    username = tk.Entry(window)
    username.grid(row=0,column=1)#izliza input s koito moga da pisha po nego
    tk.Label(window,text='Enter your email:').grid(row=1, column=0)
    email = tk.Entry(window)
    email.grid(row=1, column=1)  # izliza input s koito moga da pisha po nego
    tk.Label(window,text='Enter your password:').grid(row=2, column=0)
    password = tk.Entry(window,show='*')
    password.grid(row=2, column=1)#pri showa kato vuvejdame neshto shte budat replacnati sus zvezdichka
    tk.Label(window,text='Confirm your password:').grid(row=3, column=0)
    confirm_password = tk.Entry(window,show='*')
    confirm_password.grid(row=3, column=1)  # izliza input s koito moga da pisha po nego

    def on_register():
        username_value = username.get()
        email_value = email.get()
        password_value = password.get()
        confirm_password_value = confirm_password.get()

        if password_value != confirm_password_value:
            tk.Label(window,text='Password must match!', fg='red').grid(row=4,column=1)
        else:
            result =register(username_value,email_value,password_value)#sus alt+enter da mi importne
            if result:
                render_login_screen(window)
            else:
                tk.Label(window, text='Username is already registered!', fg='red').grid(row=4, column=1)


    tk.Button(window, text='Register',
              bg='green',
              fg='black',
              command=on_register#tova e reference
              ).grid(row=5, column=1)  # grida go slaga na mqstoto

