import random
import csv


class M:
    f = open('Book1.csv')
    type(f)
    csvreader = csv.reader(f)

    PSL = []
    UNL= []
    Lines = []
    rows = []
    Header= []
    Header = next(f)
    for row in csvreader:
        UNL.append(row[0])
        rows.append(row)

def login():
    Username = input('Enter your Username: ')
    if Username in M.UNL:
        Password = input('Enter Password: ')
        for user in M.rows:
            if user[0] == Username:
                if user[1] == Password :
                    print(f'Welcome back {Username}!')
                    print(f'Your winning {user[2]}$')
                    print(f'Your losing {user[3]}$')
                    user[2] = int(user[2])
                    user[3] = int(user[3])
                    print(f'The Difference {user[2]-user[3]}$')
                    login()
                else:
                    print('Wrong Password!')
                    login()
    else:
        print('Error')
        login()
login()