import tabulate
from var import table,today,time
def main():
    start()





def add_balance(n:int,path="balance.csv"):
    with open(path) as file:
        for line in file:
            balance=line.strip().split(",")
        b=int(balance[1])
        b+=n
    with open(path,"w") as file:
        file.write(f"Balance,{b}")




def withdraw(n:int,path="balance.csv"):
    with open(path) as file:
        for line in file:
            balance=line.strip().split(",")
        b=int(balance[1])
        if b>=n:
            b-=n
            with open(path,"w") as file:
                file.write(f"Balance,{b}")
        else:
            print("Balance Insufficient")
            raise ValueError
    




def view_balance(path="balance.csv"):
    with open(path) as file:
        for line in file:
            balance=line.strip().split(",")
        print("Balance:",balance[1])




def last(path2="transaction history.csv"):
    global table
    table=[]
    with open(path2) as file:
        for line in file:
            row_list=line.strip().split(",")
            table.append(row_list)
        print(tabulate.tabulate(table,headers="firstrow",tablefmt="fancy_grid"))






def ins():
    global table
    table=[]
    with open("_.csv") as file:
        for line in file:
            row_list=line.strip().split(",")
            table.append(row_list)
        print(tabulate.tabulate(table,headers="firstrow",tablefmt="fancy_grid"))





def start():
    while True:
        ins()
        action=input("Command: ").strip().upper()
        match action:
            case "A":
                try:
                    amount=int(input("Enter Amount: "))
                    add_balance(amount)
                    with open("transaction history.csv","a") as file:
                        file.write(f"\nAdd,{amount},{today},{time}")
                except (ValueError,TypeError):
                    pass
                
            case "W":
                try:
                    amount=int(input("Enter Amount: "))
                    withdraw(amount)
                    with open("transaction history.csv","a") as file:
                        file.write(f"\nwithdrawn,{amount},{today},{time}")
                except (ValueError,TypeError):
                    pass

            case "V":
                view_balance()
                input("To continue Press Enter: ")
            case "L":
                last()
                input("To continue Press Enter: ")
            case "X":
                print("Thanks For using!!")
                break
            case _:
                print("Invalid Input: ")
                input("Press Enter To continue")




if __name__=="__main__":
    main()
