import csv

class M:
    ins = []
    s = []
    N= []
    f= open('Book1.csv')
    type(f)
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
        s.append(row)
        N.append(row[0])



import csv

def signup():
    print('Welcome to the sign-up page!')
    username = input('Enter your username: ')
    if username in M.N:
        print('Username already exists! Plz try again!')
        signup()
    password = input('Enter your password: ')
    Winning = (input('Winning Money: '))
    try:
        int(Winning)
    except:
        print('Enter a number! Plz try again!')
        signup()
    Losing = (input('Losing Money: '))
    try:
        int(Losing)
    except:
        print('Enter a number! Plz try again!')
        signup()
        ins = "\n"+username+(",")+password+(",")+Winning+(",")+Losing
        with open('Book1.csv', 'a', newline='') as f:
            f.write(ins)
            f.close()
        print('Sign-up successful!')
    else:
        print('Error! Plz try again!')
        signup()
      
  
    
        
signup()


