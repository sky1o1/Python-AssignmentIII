import pandas
import os

class console():

    deposit = 0
    balance = 0
    installment = 0


    def course(self):
        print("------------------------------------------------------------------------------------------")
        print("The courses we offer are as follows:")
        print("1, SOFTWARE ENGINEERING")
        print("2. HTML, CSS AND JS")
        print("3. PYTHON")
        print("4. DJANGO FRAMEWORK")
        print("5. DATABASE")
        print("6. REST API")
        print("7. REACT JS")
        print("------------------------------------------------------------------------------------------")


    def inq(self):
        print("------------------------------------------------------------------------------------------")
        print("Course held by INSIGHTS WORKSHOP")
        print("Duration: 3 months")
        print("Lecturer: Shrawan Paudel, Nabin Paudel, Sita Ram Gautam, Prakash Shrestha")
        print("Course Type: Online")
        print("Fees: Free")
        print("------------------------------------------------------------------------------------------")

    def registration(self):
        obj1 = console()
        while True:
            print("------------------------------------------------------------------------------------------")
            print("Select options for payment option for  registration")
            print("1. FULL PAYMENT")
            print("2. INSTALLMENT PAYMENT")
            opt = input("Enter your options: ")

            if opt == '1':
                self.deposit = int(input("Enter the amount: "))
                if self.deposit > 20000:
                    print("PLEASE DEPOSIT THE RIGHT AMOUNT")
                elif self.deposit < 20000:
                    print("INSUFFICIENT AMOUNT , PLEASE ENTER AGAIN")
                else:
                    print("SUCCESSFULLY DEPOSITED Rs: ", self.deposit)
                    console.balance = self.deposit
                    obj1.info_write()
                    return("------------------------------------------------------------------------------------------")

            elif opt == '2':
                if self.installment == 0:
                    self.installment = int(input("Deposit Rs 10000/- for the first installment payment: "))
                    if self.installment > 10000:
                        print("AMOUNT EXCEEDED!! PLEASE DEPOSIT THE RIGHT AMOUNT")
                    elif self.installment < 10000:
                        print("INSUFFICIENT AMOUNT , PLEASE ENTER AGAIN")
                    else:
                        print("SUCCESSFULLY DEPOSITED Rs: ", self.installment)
                        console.balance = self.installment
                        obj1.info_write()
                        return("------------------------------------------------------------------------------------------")


                elif self.installment == 10000:
                    self.installment += int(input("Deposit Rs 10000/- for the second installment payment: "))
                    if self.installment > 10000:
                        print("AMOUNT EXCEEDED!! PLEASE DEPOSIT THE RIGHT AMOUNT")
                    elif self.installment < 10000:
                        print("INSUFFICIENT AMOUNT , PLEASE ENTER AGAIN")
                    else:
                        print("SUCCESSFULLY DEPOSITED Rs: ", self.installment)
                        console.balance = self.installment + 10000
                        obj1.info_write()
                        return("------------------------------------------------------------------------------------------")

            else:
                print("Enter the correct option")
                continue

    def info_write(self):
        print("------------------------------------------------------------------------------------------")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        phone = int(input("Enter your phone number: "))
        email = input("Enter your email: ")
        balance = console.balance
        remaining = 20000 - self.balance
        info = pandas.DataFrame([[name, age, address, phone, email, balance, remaining]],
                                columns=['Name', 'Age', 'Address', 'Phone No.', 'Email', 'Total Balance',
                                         'Remaining Balance'])
        info.to_csv("info.csv", mode='a', header=True, index=False)

    def info_read(self):
        print("------------------------------------------------------------------------------------------")
        read = pandas.read_csv("info.csv")
        print(read)
        return ("------------------------------------------------------------------------------------------")

    def update(self):
        print("------------------------------------------------------------------------------------------")
        up = pandas.read_csv('info.csv')
        print(up)
        edit = int(input("Enter the row to be edited: "))
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        phone = int(input("Enter your phone number: "))
        email = input("Enter your email: ")
        total = int(input("Enter total balance: "))
        remaining = int(input("Enter remaining: "))
        up.loc[edit] = [name, age, address, phone, email, total, remaining]
        up.to_csv("info.csv", header=False, index=False)
        print(up)
        return("------------------------------------------------------------------------------------------")

    def dele(self):
        print("------------------------------------------------------------------------------------------")
        while True:
            data = pandas.read_csv("info.csv")
            print(data)
            leave = input("Do you want to leave the course? Y? N?: ")
            if leave == 'Y':
                del_r = int(input("Enter the rows to be deleted: "))
                data.drop(index=del_r,  inplace=True)
                data.to_csv("info.csv", header=True, index=False)
                balance = console.balance - 20000
                print("Your Rs 20000/- has been returned")
                print("Your total balance: ", balance)
                return data
            elif leave == "N":
                return "Thank You"
            else:
                print("Error")
                continue


cour = console()

while True:
    print("WELCOME TO INSIGHTS WORKSHOP")
    print("1. Courses")
    print("2. Inquiry")
    print("3. Registration")
    print("4. Student Information")
    print("5. Update")
    print("6. Delete")
    print("7. Exit")

    choice = input("Enter your option:\t")
    if choice == '1':
        cour.course()
    elif choice == '2':
        cour.inq()
    elif choice == '3':
        print(cour.registration())
    elif choice == '4':
        print(cour.info_read())
    elif choice == '5':
        print(cour.update())
    elif choice == '6':
        print(cour.dele())
    elif choice == '7':
        print("-------------")
        print("  THANK YOU")
        print("-------------")
        break
    else:
        print("Enter correct choice")
        continue



