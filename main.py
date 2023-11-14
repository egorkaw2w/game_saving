import random
import time
import json
import csv
def show_inventory():
    print("У твоего персонажа есть: \n")
    for i in hero:
        print(f"{i}  {str(hero[i])}")
        time.sleep(0.2)

def location():
    print("----Выбор локации----")
    for i in locate:
        print(i)
def saving():
    print("Сохраняю")
    with open ("saves.json","a") as file:
        json.dump(hero,file,ensure_ascii=False, indent = 4)
def saving_csv():
    print("сохранение csv")
    with open ("saves.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow(
            "ХР",
            "Sila",
            "Agila",
            "intelekt",
            "harizma"

        )
        with open("saves.json") as file:
            src = json.load(file)
            data = [[hero["healpoints"],hero["invetory"]]]
            with open("saves.csv","w",newline="") as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row)
# В общем. Честно не понял как сделать с csv. Пожалуйста объясните ^_^

    print("сохранил")



def destiny():
    damage = 1
    destiny = random.randint(1, 2)
    if destiny == 1:
        print("он промахнулся, а ты убежал в страхе")
        damage = 0
    elif destiny == 2:
        print("он проткунл тебя заточкой и ты скоропостижно умер")
        damage = 999
    hero["healpoints"] -= damage

locate = {"камера": {"параша", "шконка", "тайник"}}
hero_easy = {"healpoints": 30,"strength": 20, "agility": 20,  "intelekt": 20, "harizma": 20, "inventory": {"заточка": 1,"Кровные: ":150, "братки: ":10 , "aegis of the immortality": 1}}
hero_medium = {"healpoints": 20,"strength": 10, "agility": 10,  "intelekt": 10, "harizma": 10, "inventory": {"Кровные": 75},"плакат с Марго Робби": 1}
hero_hard = {"healpoints": 10,"strength": 5, "agility": 5,  "intelekt": 5, "harizma": 5, "inventory": ["Кровные: 15"]}
event = {1 : "тут сидит какой то чёрт, который хочет дать тебе по щам", 2: "Кто то оставил тебе вкусняшку", 3: "Тут записка"}
vkusnyahka = {1: "шоколадка", 2: "заточка", 3: "отравленная шоколадка"}
zapiska = {1: "Где твой лут?", 2: "я тебя люблю ! ", 3: "неразборчиво, но тут вроде есть мат"}
tainik = {}

# def proverka_na_smert():
#     if ["healpoints"] < 0:
#         print("К сожалению, вы умерли. Ваш труп выкинули и скормили диким псам, а инвентарь разделили между полицейскими")
#         return hpshka == False
def startmenu():
    print("Приветсвую тебя, юный воин! Сегодня ты попал на зону")
    print("-----------------------------------------------------------------")
    print("Выбери сложность игры:")
    print("1. Лёгкий - Ты сразу попадаешь на зону, будучи крутым челом. Ты сел за массовое убийство в чечне, все тебя боятся, а также не хотят с тобой драться. Ты начинаешь с максимальными характеристиками")
    print("2. Средний - Ты попадаешь  на зону, будучи обычным человеком, который сел на за маленькую кражу. Вы начинаете игру с средними характеристиками")
    print("3. Сложный - ты попадаешь на зону, будучи опущенным, тебе будет невероятно сложно поставить себя в данном обществе, но мы в тебя верим")


def podverhzhedie():
        print("Подтверди свой выбор")
        print("-----------------------------------------------------------------")
        choice = (input("Напиши: ПОДТВЕРЖДАЮ или ОТМЕНА "))
        print("-----------------------------------------------------------------")
        if choice == "ПОДТВЕРЖДАЮ":
            print("удачи и весёлой игры")
            print("-----------------------------------------------------------------")
            time.sleep(1)
            return "ПОДТВЕРЖДАЮ"
        elif choice == "ОТМЕНА":
            print("-----------------------------------------------------------------")
            time.sleep(1)
            return "ОТМЕНА"
        else:
            print("не понял")
            print("-----------------------------------------------------------------")
            startmenu()
            myhero = int(input("Сложность: "));
            time.sleep(1)

choice = ""

while choice != "ПОДТВЕРЖДАЮ":
    startmenu()
    print("-----------------------------------------------------------------")
    try:
        myhero = int(input("Сложность: "));
    except ValueError:
        print("Введи номер сложности \n")
        time.sleep(2)
        continue
    print("-----------------------------------------------------------------")
    if myhero == 1:
        hero = hero_easy
        print("Чтож, поздравляю тебя! Ты выбрал прекрасную жизнь, и я тебя понимаю, ведь даже на зоне можно, а главное нужно, жить с комфортом!")
        time.sleep(1)
        choice = podverhzhedie()
    elif myhero == 2:
        hero = hero_medium
        print("Мои поздравления! Ты станешь (возможно) прекрасным авторитетом!")
        time.sleep(1)
        choice = podverhzhedie()
    elif myhero == 3:
        hero = hero_hard
        print("Ух ты! Не завидую твоей учести, дорогой игрок. Тебе предстоит окунуться в мир, наполненый болью и страданием. Удачи тебе, я в тебя верю!")
        time.sleep(1)
        choice = podverhzhedie()
    else:
        print("Такой сложности нет, тебе что доступных не хватает?")
    time.sleep(1)

    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
if hero.get("healpoints") > 0:
    print("твой инвентарь: ")
    for i in  hero :
        print(f"{i}  {str(hero[i])}")
choice = None

pos = 0

while hero.get("healpoints") > 0:
    try:
        # proverka_na_smert()
        print("---------Меню---------")
        print("1. Проверить инвентарь")
        print("2. Проверить Локации")
        print("3. Сохраниться ")
        print("4. Выйти из игры ")
        print("5. Чекнуть сохранения")
        try:
            choice = int(input())
        except ValueError:
            print("Введи номер локи")
        if choice == 1:
            show_inventory()
        if choice == 2:
            location()
            loc = input()
            if  loc == "камера" :
                loc = locate["камера"]
                print("----------------------")
                for i in loc:
                    print(i)
                loc_1 = input()
                #///////////
                if loc_1 == "шконка":

                    print("Ты у шконки. ")
                    event_case = random.randint(1,3) #рандомное событие <event>
                    if event_case == 1: #дали шокоадку
                        print(event[1])
                        damage = random.randint(1, 10)
                        if damage in [1,2,3] :
                            print(f"тебя царапнули на {damage} урона")
                            hero["healpoints"] -= damage
                        elif damage in [4,5,6,7]:
                            print(f"тебя конкретно кацанули на {damage} урона")
                            hero["healpoints"] -= damage
                        elif damage in [8,9,10]:
                            print(f"Тебя изподтешка накромсали, и нанесли {damage} урона!")
                            hero["healpoints"] -= damage
    #/////////////////////////////////////////////////////////////
                    elif event_case == 2: # дали вкусняшку
                        print(event[2])
                        event_case =  random.randint(1,3) #рандом на вкусняшку
                        #////////////
                        if event_case == 1 :  #дали шоколадку
                            print(vkusnyahka[1])
                            if "шоколадка" in hero["inventory"]:
                                hero["inventory"]["шоколадка"] += 1
                            else:
                                hero["inventory"]["шоколадка"] = 1
                        elif event_case == 2 : #дали заточку
                            print(f" была добавлена {vkusnyahka[2]}")
                            if "заточка" in hero["inventory"]:
                                hero["inventory"]["заточка"] += 1
                            else:
                                hero["inventory"]["заточка"] = 1
                        elif event_case == 3: # отравили
                            print(vkusnyahka[3])
                            hero["healpoints"] -= 1
                            # proverka_na_smert()
                                #//////////////

                    elif event_case == 3: # дали записку ( третий ивент )
                        print(event[3])
                        event_case = random.randint(1,3)
                        if event_case == 1:
                            print(zapiska[1])
                            pos_1 = pos
                            pos_1 += 1
                            pos = pos_1
                        elif event_case == 2:
                            print(zapiska[2])
                        elif event_case == 3:
                            print(zapiska[3])

                elif loc_1 == "тайник":
                    print("вы у тайника ")
                    print("-----------------------------")
                    print("Что делать?")
                    print("1. Сложить шмотьё")
                    print("2. проверить тайник")
                    print("3. отойти")
                    choice_inv = int(input("Выберите действие (цифра)"))
                    if choice_inv == 1:
                        show_inventory()
                        print("----------------------")
                        print("Что сделаем?")
                        print("----------------------")
                        choice_inv = int(input("Выбери действие (цифра)"))
                        if choice_inv == 1:
                            try:
                                len(hero["inventory"]) == 0
                            except:
                                hero["inventory"] = dict()
                                print("Ваш инвентарь пустой :(")
                                continue
                            if len(hero["inventory"]):
                                print("сложены следующие вещи: " + str(hero["inventory"]))
                                inventory = hero.get('inventory')
                                tainik.update(inventory)
                                inventory.clear()
                                print("----------------------")
                                print("Дело сделано")
                                print("----------------------")
                            time.sleep(1.5)
                    elif choice_inv== 2:
                        print("Инвентарь тайника:" + str(tainik))
                        print("----------------------")
                        print("Что будем делать?")
                        print("----------------------")
                        print("1. Взять лут")
                        print("2. уйти")
                        choice_inv = int(input("Введите дейстие"))
                        if choice_inv == 1:
                            print("Берём лут")
                            time.sleep(0.5)
                            print("1")
                            time.sleep(0.5)
                            print("2")
                            time.sleep(0.5)
                            print("3")
                            time.sleep(0.5)
                            if len(tainik) != 0:
                                hero["inventory"].update(tainik)
                                tainik.clear()
                            try:
                                len(tainik) == 0
                                print("Тайник пуст :(")
                                continue
                            except:
                                tainik = dict()
                                print("Тайник пуст  <><>:(")
                                continue

                            continue
                        time.sleep(1.2)
                    elif choice_inv == 3:
                        print("я пошёл")
                        time.sleep(1.2)
                        continue
                elif loc_1 == "параша":
                    print("Тут какой то мутный тип")
                    print("подойдём?")
                    print("1. да")
                    print("2. нет")
                    choice = int(input("выбери действие"))
                    if choice == 1:
                        print("Приветсвутю тебя в моей лавке! Сегодня я могу предложить тебе")
                        print("--------------------")
                        print("Ассортимент")
                        print("1. Заточка 1шт за твои кровные )")
                        print("--------------------")
                        print("1. Покупаю!")
                        print("2. Мне ничего не нужно! Пойду я отсюда")
                        choice = int(input("выбери действие"))
                        if choice == 1:
                            print("Я что на торгаша похож?")
                            print("Лови заточку!")
                            destiny()
        elif choice == 3:
            saving()
        elif choice == 4:
            print("Вы уверены, что хотите выйти из игры?")
            print("1. да")
            print("2. нет")
            choice = int(input("Выберите: "))
            if choice == 1:
                print("Сохранить игру?")
                print("1. да")
                print("2. нет")
                choice = int(input("Выберите: "))
                if choice == 1:
                    saving_csv()
                    print("пока")
                    break
                elif choice == 2:
                    print("а ты рисковый")
                    break
            elif choice == 2:
                print("гуд")
                continue
        elif choice == 5:
            print("Сохранения")
            with open("saves.json","r") as file:
                save = json.load(file)
                print(save)
            print("Что делать?")
            print("1. Удалить сохранение")
            print("2. Выход")
            choice = int(input("Выбор: "))
            if choice == 1:
                with open ("saves.json","r") as file:
                    save = json.load(file)
                del save
                with open("saves.json","w") as file:
                    json.dump(save,file,indent = 4)
    except:
        print("")

if hero.get("healpoints") < 0:
    print("К сожалению, вы умерли. Ваш труп выкинули и скормили диким псам, а инвентарь разделили между полицейскими")












