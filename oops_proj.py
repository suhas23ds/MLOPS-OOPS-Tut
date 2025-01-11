class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.login=False
        self.msg=""
        self.menu()
    
    def menu(self):
        user_input=input('''Well come to chatbook !! how would you like to proceed?
                            1. Press 1 to sigin
                            2. Press 2 to singup
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit
                            
                            --->''')

        if user_input == "1":
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input =="3":
            self.my_post()
        elif user_input =="4":
            self.send_message()
        else:
            exit()

    def signup(self):
        email = input("enter your email id here :")
        password=input('enter your password here:')
        self.username=email
        self.password=password
        print("You have login succefully ")
        print("\n")
        self.menu()
    def signin(self):
        if self.username== '' and self.password=="":
            print('Please signup first by pressing 1 in the main menu :')
        else:
            uname=input('enter your email/username here :')
            pwd=input('enter your password here :')
            if self.username==uname and self.password==pwd:
                print("you have signed in successfully !!")
                self.login=True
            else:
                print('Please input correct credentials')
        print("\n")
        self.menu()

    def my_post(self):
        if self.login == True:
            txt=input("enter your message here")
            print(f'your post suceefully posted -{txt}')
        else:
            print('you need to sigin first to post something')
        print('\n')
        self.menu()

    def send_message(self):
        if self.msg == True:
            txt=input('enter the mesage to your friend ')
            frnd=input('whom to send the message')
            print(f'message send to the {txt}')
        else:
            print('you need to sigin before sending msg ')
        print('\n')
        self.menu()

obj=chatbook()
