class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.login=False
        self.menu()
    
    def menu(self):
        user_input=input('''Well come to chatbook !! how would you like to proceed?
                            1. Press 1 to sigin
                            2. Press 2 to singup
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit''')

        if user_input == "1":
            pass
        elif user_input =="2":
            pass
        elif user_input =="3":
            pass
        elif user_input =="4":
            pass
        else:
            exit()

obj =chatbook()