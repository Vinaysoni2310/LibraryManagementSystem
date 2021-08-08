import datetime as dt
import time as t
import random

books ={10001:{"Name":"The Fault in Our Stars","Author Name":"John Green","Total Pages":500,"ISBN":9780525478812,"Status":"Available","Published Year":2002,"Total Copies":4,"Copies Available":4},
        10002:{"Name":"The Night Circus","Author Name":"Erin Morgenstern","Total Pages":389,"ISBN":9780307744432,"Status":"Available","Published Year":1998,"Total Copies":3,"Copies Available":3},
        10003:{"Name":"Last Night at the Lobster","Author Name":"Stewart O'Nan","Total Pages":250,"ISBN":9780143114420,"Status":"Available","Published Year":2007,"Total Copies":1,"Copies Available":1},
        10004:{"Name":"Braiding Sweetgrass","Author Name":"Robin Wall Kimmerer","Total Pages":600,"ISBN":9781571313560,"Status":"Available","Published Year":2013,"Total Copies":2,"Copies Available":2},
        10005:{"Name":"Station Eleven","Author Name":"Emily St. John Mandel","Total Pages":279,"ISBN":9780804172448,"Status":"Available","Published Year":2009,"Total Copies":3,"Copies Available":3},
        10006:{"Name":"Revolution 2020","Author Name":"Chetan Bhagat","Total Pages":469,"ISBN":9780525478869,"Status":"Available","Published Year":2000,"Total Copies":5,"Copies Available":5}}

u_details = {}
book_req ={}
issued_book={}
return_req = {}
history = {}
admin_list = {"admin":"admin"}




class LMS:
    """This is a class to manage books of library"""
    def __init__(self):
        print(('*')*20,"Welcome to Asiatic library !!!",('*')*20)
        self.admin = False
        self.user = False




    #****************************************** Login & registration ***************************************************

    def login(self):
        """This is a function where user login"""
        input1 = input("\n\t\t\t\t\t Select a profile to login:"
                       "\n\t\t\t\t\t Press 1- Admin"
                       "\n\t\t\t\t\t Press 2-Borrower"
                       "\n\t\t\t\t\t Press 3-Register from here\n=>")
        if input1 == "1":
            email = input("Enter Email ID\n")
            password = input("Enter Password\n")
            print("Logging in...\n\n")
            t.sleep(0.5)
            if email in admin_list and password== admin_list[email]:
                print(('*')*15,"Welcome Admin to Asiatic Library. What changes you would like to do??",('*')*15)
                self.admin = True
            else:
                print("Invalid credentials for admins")
                self.login()

        elif input1 == "2":
            self.email = input("Enter Email ID\n")
            password = input("Enter Password\n")
            print("Logging in...\n\n")
            t.sleep(0.5)
            if self.email in u_details and password == u_details[self.email]["Password"]:
                print(('*')*20,"Welcome to Asiatic Library !!!",('*')*20)
                self.user = True
            else:
                print("Wrong Credentials. Please try again")
                self.login()
        elif input1 =="3":
            self.register()

        else:
            print("Invalid Option")
            self.login()


    def register(self):
        """This is function for registeration"""
        d ={}
        self.name = input("Enter your Full Name:\n")
        self.number = input("Enter your Contact Number:\n")
        self.email = input("Enter your Email Id:\n")
        self.DOB = input("Enter your DOB in DD/MM/YYYY Format:\n")
        self.password = input("Enter your Password\n")
        d[self.email] = {"Full Name":self.name,"DOB":self.DOB,"Contact Number":self.number,"Password":self.password}
        print("Please wait while we register your details")
        t.sleep(1)
        print("Registration Successful")
        u_details.update(d)
        self.login()

    #*********************************************** User Functions ****************************************************


    def view_books(self):
        print("\n")
        print("{: >26} {: >26} {: >20} {: >20}".format("ID", "Book Name", "Total Copies","Copies Available"))
        print(("-")*100)
        for item in books:
            print("{: >26} {: >26} {: >20} {: >20}".format(item,books[item]["Name"],books[item]["Total Copies"],books[item]["Copies Available"]))



    def request(self):
        print("\n***** Hello, please request the book and admin will lend you the book if it's available.Thank you!! *****")
        print("***** You can lend a book only for 15 days or else you have to pay fine of Rs.100!!! *****\n")
        id_ = int(input("Enter the Id of book you want to request for:\n"))
        if id_ in books:
            if self.email in book_req:
                book_req[self.email].append([id_, dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
                print(f"Successfully requested for {id_}. Please wait while the admin accepts your request.")
            else:
                book_req[self.email] = [[id_, dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]]
                print(f"Successfully requested for {id_}. Please wait while the admin accepts your request.")

        else:
            print("Enter a valid Book ID!!!")


    def return_book(self):
        input1 = int(input("Enter the book Id you want to return:\n"))
        for name in issued_book:
            if self.email == name:
                for items in issued_book[name]:
                    if items[0] == input1:
                        current_date = dt.date.today()
                        borrowed_date =  items[1]
                        fine = (current_date-borrowed_date).days
                        if fine > 14:
                            print("You've to pay a fine of Rs.100 for late submission of book to admin.")
                            ans = input("Type yes to pay fine:\n").upper()
                            if ans == "YES":
                                print("Successfully returned")
                                if name in return_req:
                                    return_req[name].append([items[0],"Returned with fine"])
                                else:
                                    return_req[name] = [[items[0], "Returned with fine"]]
                            else:
                                print("No fine No submission of book!!! Interest will keep on adding")
                        else:
                            print("Submitted on time. No Fine for you!!!")
                            print("Successfully returned")
                            if name in return_req:
                                return_req[name].append([items[0], "No fine"])
                            else:
                                return_req[name] = [[items[0], "No fine"]]
                    else:
                        print("Enter a valid Book ID")

    def view_detail(self):
        det =  int(input("Enter the Book Id you want to see details of!!!\n=>"))
        print("Loading Details...")
        t.sleep(0.5)
        if det in books:
            print("Title: ", books[det]["Name"])
            print("Author Name: ", books[det]["Author Name"])
            print("Published Year: ", books[det]["Published Year"])
            print("Pages: ", books[det]["Total Pages"])
            print("ISBN: ", books[det]["ISBN"])


    def hist(self):
        if history == {}:
            print("No books issued yet")
        else:
            for user in history:
                if self.email == user:
                    for i in history[user]:
                        print(f"Took {i[0]} on {i[1]}")
                else:
                    print("Empty...")


    #*********************************************** Admin Functions ***************************************************

    def add_book(self):
        d = {}
        name = input("Enter the Title of the book:\n")
        if name == "":
            return self.add_book()
        else:
            author = input("Author Name:\n")
            pages = int(input("Pages:\n"))
            copies = int(input("Copies:\n"))
            isbn = random.randrange(9000000000000,10000000000000)
            publish_year = int(input("Published Year:\n"))
            d[max(books)+1] = {"Name":name,"Author Name":author,"Total Pages":pages,"ISBN":isbn,"Published Year":publish_year,"Total Copies":copies,"Copies Available":copies}
            books.update(d)


    def remove_book(self):
        rem = int(input("Enter the Book Id you want to remove from list:\n"))
        if rem in books:
            books.pop(rem)
        else:
            print("Enter a valid Book Id")
            self.remove_book()

    def issue_book(self):
        for name in book_req:
            for items in book_req[name]:
                id = items[0]
                if books[id]["Copies Available"] >= 1:
                    da = dt.date.today()
                    if name in issued_book:
                        issued_book[name].append([id,da])
                        books[id]["Copies Available"] -= 1
                        if name in history:
                            history[name].append([id,da])
                        else:
                            history[name] = [[id,da]]
                        print(f"{id} has been successfully issued to {name} on {da}")
                        book_req[name].remove(items)
                    else:
                        issued_book[name] = [[id,da]]
                        books[id]["Copies Available"] -= 1
                        if name in history:
                            history[name].append([id,da])
                        else:
                            history[name] = [[id,da]]
                        print(f"{id} has been successfully issued to {name} on {da}")
                        book_req[name].remove(items)

                else:
                    print("Cannot issue this book as no copies are available")


    def ret_book(self):
        for name in return_req:
            for items in return_req[name]:
                books[items[0]]["Copies Available"] += 1
                return_req[name].remove(items)
                print("Successfully Updated in Library")
            else:
                print("Try again!!!")


    def issued_list(self):
        for name in issued_book:
            for items in issued_book[name]:
                email = name
                yo = items[1]
                print(f"{items[0]} is issued to {email} on {yo}")

    def create_admin(self):
        mailid = input("Enter the email Id of another admin:\n")
        passw = input("Create a password for another admin:\n")
        admin_list[mailid] = passw
        print(f"Successfully added {mailid} to admins")



    def menu(self):
        input4 = input("\n\t\t\t\t\t\tPress 1 => Login\n\t\t\t\t\t\tPress 2 => Register\n\t\t\t\t\t\tPress 3 => Exit\n=>")
        if input4 == '1':
            self.login()
        elif input4 == '2':
            self.register()
        elif input4 == '3':
            print("See ya!!!")
        else:
            print("Invalid Selection")
            self.menu()


        ans = True
        if self.user:
            while ans:
                try:
                    print("\n\t\t\t\t\t D => Display Books\n\t\t\t\t\t "
                          "A => Request a book\n\t\t\t\t\t "
                          "R => Return a Book\n\t\t\t\t\t "
                          "H => Borrowed History\n\t\t\t\t\t "
                          "V => View book details\n\t\t\t\t\t "
                          "E => Exit(Please select this to exit and sign in as admin and process all the requests)")
                    print("---------------------------------------------------------------")
                    self.choice = input("Please Enter 'D'/'A'/'R'/'H'/'V'/'E' :\n").upper()
                    if self.choice == "E":
                        print("Thank you!!! Please check in a while if admin has processed your request if any.Bubye!!!")
                        ans = False
                        self.user = False
                        self.menu()
                    elif self.choice == "D":
                        self.view_books()
                    elif self.choice == "A":
                        self.request()
                    elif self.choice == "R":
                        self.return_book()
                    elif self.choice == "H":
                        self.hist()
                    elif self.choice == "V":
                        self.view_detail()
                    else:
                        self.menu()
                except Exception as e:
                    print(e)

        elif self.admin:
            ans = True
            while ans:
                try:
                    print(("-")*100)
                    self.choice = input("\n\t\t\t\t\t Please Enter"
                                        "\n\t\t\t\t\t 'D' to Display Books"
                                        "\n\t\t\t\t\t 'A' to Add a Book"
                                        "\n\t\t\t\t\t 'R' to Remove a Book"
                                        "\n\t\t\t\t\t 'V' to see Book details"
                                        "\n\t\t\t\t\t 'L' to see Issued Book list"
                                        "\n\t\t\t\t\t 'I' to confirm Issue requests"
                                        "\n\t\t\t\t\t 'U' to Update the returned books back to library"
                                        "\n\t\t\t\t\t 'C' to Create another admin"
                                        "\n\t\t\t\t\t 'E' to exit(Please select this to exit and sign in as borrower to check if request has been accepted)\n=>").upper()
                    if self.choice == "E":
                        print("Byee admin!!!")
                        self.admin = False
                        ans = False
                        self.menu()
                    elif self.choice == "A":
                        self.add_book()
                    elif self.choice == "D":
                        self.view_books()
                    elif self.choice == "R":
                        self.remove_book()
                    elif self.choice == "V":
                        self.view_detail()
                    elif self.choice == "I":
                        self.issue_book()
                    elif self.choice == "U":
                        self.ret_book()
                    elif self.choice == "L":
                        self.issued_list()
                    elif self.choice == "C":
                        self.create_admin()
                    else:
                        pass
                except Exception as e:
                    print(e)


vin = LMS()
vin.menu()
