from tkinter import Tk, LEFT, X, RIGHT
from tkinter.ttk import Label, Button, Entry, Combobox, Frame


class Food():
    # Atributos
    name = ''
    calories = 0  # cal
    ingredients = ''
    portion = ''  # gr, taza, ml..
    carbs = 0  # gr
    fat = 0  # gr

    # Métodos
    def __init__(self, name, calories, ingredients, portion, carbs, fat):
        self.name = name
        self.calories = calories
        self.ingredients = ingredients
        self.portion = portion
        self.carbs = carbs
        self.fat = fat

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories

    def get_fat(self):
        return self.fat


def show_food_form():
    global entry_foodName
    global entry_foodCalories
    global entry_foodIngredients
    global entry_foodPortion
    global entry_foodCarbohydrates
    global entry_foodFat
    global frm_food

    btn_create_food.state(['disabled'])

    frm_food = Frame(root)

    frm_foodName = Frame(frm_food)
    Label(frm_foodName, text='Nombre del alimento').pack(side=LEFT)
    entry_foodName = Entry(frm_foodName)
    entry_foodName.pack(side=RIGHT)
    frm_foodName.pack(fill=X)

    frm_foodCalories = Frame(frm_food)
    Label(frm_foodCalories, text='Calorías').pack(side=LEFT)
    entry_foodCalories = Entry(frm_foodCalories)
    entry_foodCalories.pack(side=RIGHT)
    frm_foodCalories.pack(fill=X)

    frm_foodIngredients = Frame(frm_food)
    Label(frm_foodIngredients, text='Ingredientes').pack(side=LEFT)
    entry_foodIngredients = Entry(frm_foodIngredients)
    entry_foodIngredients.pack(side=RIGHT)
    frm_foodIngredients.pack(fill=X)

    frm_foodPortion = Frame(frm_food)
    Label(frm_foodPortion, text='Porción').pack(side=LEFT)
    entry_foodPortion = Entry(frm_foodPortion)
    entry_foodPortion.pack(side=RIGHT)
    frm_foodPortion.pack(fill=X)

    frm_foodCarbohydrates = Frame(frm_food)
    Label(frm_foodCarbohydrates, text='Carbohidratos').pack(side=LEFT)
    entry_foodCarbohydrates = Entry(frm_foodCarbohydrates)
    entry_foodCarbohydrates.pack(side=RIGHT)
    frm_foodCarbohydrates.pack(fill=X)

    frm_foodFat = Frame(frm_food)
    Label(frm_foodFat, text='Grasa que aporta').pack(side=LEFT)
    entry_foodFat = Entry(frm_foodFat)
    entry_foodFat.pack(side=RIGHT)
    frm_foodFat.pack(fill=X)

    Button(frm_food, text='Guardar información del alimento',
           command=save_food).pack()

    frm_food.pack(fill=X)


def save_food():
    food = Food(entry_foodName.get(), float(entry_foodCalories.get()), entry_foodIngredients.get(
    ), entry_foodPortion.get(), float(entry_foodCarbohydrates.get()), float(entry_foodFat.get()))
    food_list.append(food)
    frm_food.destroy()
    btn_create_food.state(['!disabled'])


def close_menu():
    frm_menu.destroy()
    frm_footer.destroy()


def add_food(event):
    global total_calories
    global total_fat
    Label(frm_menu, text=f'{food_list[cmb_foods.current()].get_name()}\t{food_list[cmb_foods.current()].get_calories()}\t{food_list[cmb_foods.current()].get_fat()}').pack(
        fill=X)
    total_calories += food_list[cmb_foods.current()].get_calories()
    total_fat += food_list[cmb_foods.current()].get_fat()
    lbl_footer.configure(
        text=f'Calorías totales consumidas:{total_calories}\t\tGrasas totales consumidas:{total_fat}')


def create_menu():
    global frm_menu
    global cmb_foods
    global lbl_footer
    global frm_footer

    aux_list = []
    frm_menu = Frame(root)
    cmb_foods = Combobox(frm_menu)

    for food in food_list:
        aux_list.append(food.get_name())

    cmb_foods['values'] = aux_list
    cmb_foods.state(['readonly'])
    cmb_foods.bind('<<ComboboxSelected>>', add_food)
    cmb_foods.pack()
    frm_menu.pack(fill=X)

    frm_footer = Frame(root)
    lbl_footer = Label(
        frm_footer, text=f'Calorías totales consumidas:{total_calories}\t\tGrasas totales consumidas:{total_fat}')
    lbl_footer.pack(
        fill=X)
    Button(frm_footer, text='Cerrar menú', command=close_menu).pack()
    frm_footer.pack(fill=X)


# Lista de alimentos
food_list = []

total_calories = 0
total_fat = 0

root = Tk()
root.geometry('400x600')
root.title('Contador de calorías')

frm_buttons = Frame(root)
btn_create_food = Button(
    frm_buttons, text='Ingresar alimentos', command=show_food_form)
btn_create_food.pack(side=LEFT)
btn_create_menu = Button(
    frm_buttons, text='Crear menú del día', command=create_menu)
btn_create_menu.pack(side=RIGHT)
frm_buttons.pack(fill=X)

root.mainloop()
