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
                print("Oki u can pass")
                global boolean
                boolean = True
    else:
        imposter()