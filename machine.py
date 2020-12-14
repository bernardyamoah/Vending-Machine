

money = 78
correct_work_id = ""
pencils = 5
juice = 5
crackers = 5
toffees = 10
pkt_notes = 5
boolean = False

# Functions for the customer
def obj6():
    global pencils
    global juice 
    global crackers
    global toffees
    global pkt_notes
    print(f'''
    The vending machine has:
    {pencils} pencils,
    {juice} juice boxes,
    {crackers} cracker packs
    {toffees} toffees
    and {pkt_notes} pocket notebooks. :D
    ''')
def introduce_the_game():
    print('''Hello!
    This is the vending machine game.
    How to play:
    After the displayed message, u can call a function just by writing its name.
    'Objects' tells u how many items and in what qty its loaded.
    'Buy' lets u buy an item.
    
    If you are a worker, then confirm ur id and name by calling the 'take' or 'refill' function
    to take the money or refill the vending machine. Enjoy! :D''')
def change_qty(money1, pencil1, pkt_notes1, toffee1, juice1, crackers1):
    global pencils
    global juice 
    global crackers
    global toffees
    global pkt_notes
    global money
    pencils -= pencil1
    pkt_notes -= pkt_notes1
    toffees -= toffee1
    juice -= juice1
    crackers -= crackers1
    money += money1
# some of the most useless but nice functions...don't bully them >:C
def not_enough():
    print("I don't have enough...pls refill :C")
def enough():
    print("Awesome! You got it!")
def imposter():
    print("GEt OuT U IMpoSTER!!!!!!")
# more useful functions
def buy():
    item = input("Whatcha' wanna buy? (1 - pencils, 2 - crackers, 3 - pocket notebooks, 4 - toffees, 5 - juice boxes, back - to main menu)(pls use the numbers, u don't have type the words))")
    if item == "1":
        if pencils == 0:
            not_enough()
        elif pencils > 0:
            qty_p = int(input("How many?"))
            if qty_p > pencils:
                not_enough()
            elif qty_p <= pencils:
                change_qty(qty_p*2, qty_p, 0, 0, 0, 0)
                enough()
    elif item == "2":
        if crackers == 0:
            not_enough()
        elif crackers > 0:
            qty_c = int(input("How many packs?"))
            if qty_c > crackers:
                not_enough()
            elif qty_c <= crackers:
                change_qty(qty_c*10, 0, 0, 0, 0, qty_c)
                enough()
    elif item == '3':
        if pkt_notes == 0:
            not_enough()
        elif pkt_notes > 0:
            qty_pk  = int(input("How many pocket notes?"))
            if qty_pk > pkt_notes:
                not_enough()
            elif qty_pk <= pkt_notes:
                change_qty(qty_pk*20, 0, qty_pk, 0, 0, 0)
                enough()
    elif item == "4" :
        if toffees == 0:
            not_enough()
        elif toffees > 0:
            qty_t = int(input("How many?"))
            if qty_t > toffees:
                not_enough()
            elif qty_t <= toffees:
                change_qty(qty_t, 0, 0, qty_t, 0, 0)
                enough()
    elif item == "5":
        if juice == 0:
            not_enough()
        elif juice > 0:
            qty_j = int(input("How many boxes?"))
            if qty_j > juice:
                not_enough()
            elif qty_j <= juice:
                change_qty(qty_j*15, 0, 0, 0, qty_j, 0)
    elif item == "back":
        pass
    else:
        print("Pls choose one of the given options, I can't understand what u r saying...")
# functions for workers
def verification():
    
    print("I need to verify that u r a worker and not some... some bad guy")
    userid = input("Pls input ur username: ")
    workid = input("Pls input ur (work) card number:")

    if userid == "Sara":
        global correct_work_id
        print("Okay...ur name matches to one of the workers")
        if userid == "Sara" :
            global correct_work_id
            correct_work_id = "90638652"
            if workid != correct_work_id:
                imposter()
            else:
                print("Oki ur workid matches too. U can pass")
                print("""
                And hi Sara!
                """)
                global boolean
                boolean = True
    else:
        imposter()

def refill():
    verification()
    if boolean == False:
        print("Sorry can't grant access...U iMpOsTeR!!!")
        pass
    elif boolean == True:
        juice2 = int(input("Write how many juice boxes u wanna refill :D :"))
        crackers2 = int(input("Write how many packs of crackers u wanna give :D: "))
        toffee2 = int(input("Write how many toffees u wanna refill :D :"))
        pkt_notes2 = int(input("Write how many pocket notebooks u wanna refill :D "))
        pencils2 = int(input("Write how many pencils u wanna refill :D :"))
        change_qty(0, -pencils2, -pkt_notes2, -toffee2, -juice2, -crackers2)
def take():
    verification()
    if boolean == False:
        print("Sorry can't grant access...U iMpOsTeR!!!")
    elif boolean == True:
        print("Sure! U can take the money!")
        if money > 0:
            print(f'I gave u ${money} :D')
            change_qty(-money, 0, 0, 0, 0, 0)
def do_smt():
    choose_action = input("Write action (buy, objects, refill, take, exit)(write 'how to play' for instructions):") 
    return choose_action
while True:
    action = do_smt()
    if action == "buy":
        buy()
    elif action == "refill":
        refill()
    elif action == "take":
        take()
    elif action == "objects":
        obj6()
    elif action == "how to play":
        introduce_the_game()
    elif action == "exit":
        print("Bye! Hope u had a good expirience! (unless ur an ImPoStEr trying to take money!!!)")
        break

# correct workid = 90638652
# correct userid = Sara 
    
