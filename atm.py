# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:48:09 2019

@author: USER
"""

#ATM MACHINE
import sys
class ATM:
    def __init__(self):
        self.customers={}
        self.name=''
        self.user=''
        self.pin=''
        self.moneybank={}
        self.moneybank[self.user]=0
        self.trans=''
        self.depoamount=0
        self.withamount=0
        self.Register()
        
    def welcome(self):
        print("\n____________Welcome to LINUS BANK OF NIGERIA.____________")
    
    def Register(self):
        self.welcome()
        print("       **********REGISTRATION PAGE**********       ")
        self.name=input("Enter your name (Surname followed by last name): ")
        if " " not in self.name:
            print("Make sure the names are separated by space!")
            self.Register()
        else:
            gba=self.name.index(" ")
            nim=self.name[:gba]
            self.Gender(nim)
            self.Pin()
            self.further()
            
    def further(self):
        furtherTrans=input("""\nWould you like to perform any transaction?"
              1. Yes
              2. No
              """)
        if furtherTrans=="2":
            self.further2()
        elif furtherTrans=="1":
            self.login()
            self.transactions()
        else:
            print("Invalid option!")
            self.further()
    def login(self):
        print(self.customers)
        self.user=input("\nEnter your ATM security pin: ")
        if self.user in self.customers:
            print("___________ ",self.customers[self.user],"___________")
        else:
            print("Wrong Pin!")
            self.login()
            
    def transactions(self):
        trans=["1. Withdraw            2. Deposit","3. Transfer            4. Balance","5. Recharge            6. Cancel"]
        print("Enter the number corresponding to the right Transaction...")
        for n in trans:
            print(n)
        self.trans=input()
        if self.trans=="1":
            self.withdraw()
        elif self.trans=="2":
            self.deposit()
    def further2(self):
        print("Thanks for Registering with LINUS BANK of Nigeria!")
        furtheruser=input("""1. Register another user.
                   2. Back
                     3. Quit
                  """)
        if furtheruser=="1":
            self.Register()
        elif furtheruser=="2":
            self.further()
        elif furtheruser=="3":
            self.Quit()       
        else:
            print("\nEnter a valid option!")
            self.further2()    
    
    def Quit(self):
        sys.exit
    
    def Pin(self):
        self.pin=input("Create a login pin: ")
        confirmPin=input("Confirm the pin: ")
        if confirmPin==self.pin:
            print("\n       *******************************************       ")
            print("\nLogin Pin created succesfully...Your Pin is '",self.pin,"'.")
            self.customers[self.pin]=self.name
        else:
            print("The pin doesn't match!")
            self.Pin()
            return self.customers
        print("\n",self.customers)    
    
    def Gender(self,nim):
        gender=input("Gender(Male/Female): ")
        wlcm= "{} {}! Welcome to Linus Bank of Nigeria. Registration succesful"
        if gender.lower()=="female":
            print("\n",wlcm.format("Mrs",nim))
        elif gender.lower()=="male":
            print("\n",wlcm.format("Mr",nim))
        else:
            print("\nEnter a valid gender!")
            self.Gender(nim)
    def withdraw(self):
        pass
    
    def deposit(self):
        print()
        self.depoamount=eval(input("Enter the amount you want to deposit(Naira): "))
        self.moneybank[self.user] += self.depoamount
        print("Your deposit of N",self.depoamount," is successful!")
        input()
#def Transactions():
ch=ATM()
