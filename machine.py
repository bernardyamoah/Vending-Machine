money = 0

pencils = 5
juice = 5
crackers = 5
toffees = 10
pkt_notes = 5

# Functions for the customer
def objects():
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
    
    If u r a worker, then confirm ur id and name by caling the 'take' or 'refill' function
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
    item = input("Whatcha' wanna buy? (1 - pencils, 2 - crackers, 3 - pocket notebooks, 4 - toffees, 5 - juice boxes(pls use the numbers, u don't have type the words))")
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
    else:
        print("Pls choose one of the given options, I can't understand what u r saying...")
# functions for workers
def verification():
    print("I need to verify that u r a worker and not some... some bad guy")
    userid = input("Pls input ur username: ")
    # workid = input("Pls input ur (work) card number:")
    # correct_work_id = ""
    if userid == "Adam" or userid == "Sara":
        print("Okay...ur name matches to one of the workers")
    if userid == "Adam":
        global correct_work_id
        correct_work_id = "15568947"
    elif userid == "Sara":
        global correct_work_id
        correct_work_id = "9063865y"
    
    else:
        print("")

def take():
    pass
