import tkinter as tk

from guiproject.auth_service import register


def clear_window(window):
    for child in window.winfo_children():#dava mi vsichki neshta na ekrana kato obekti
        child.destroy()#tova shte ni izchisti ekrana

def render_main_screen(window):
    tk.Button(window, text='Login',
              bg='green',
              fg='white',
              command=lambda:print('the login button has benn clicked')
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
            result =register()

    tk.Button(window, text='Register',
              bg='green',
              fg='black',
              command=on_register#tova e reference
              ).grid(row=5, column=1)  # grida go slaga na mqstoto


if __name__ == '__main__':
    window = tk.Tk()#tova e samata vizializaciq na prozoreca
    window.geometry('700x700')#razmerite
    window.title('My GUI Shop')#tova e kakvo da pishe vmesto tk
    render_main_screen(window)
    window.mainloop()#staratira
