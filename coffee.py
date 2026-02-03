#Statement of Requirements
#Functional Requirements:
# allows int values of coins valued 5-50 pence
# doesnt crash
#Non-Functional Requirements:
# prompts user to input int values of the coin
# change = total coin input - 75
def get_coin():
    global required
    global total
    required = 75
    total = 0
    while total <= required:
            insert = input("**INSERT COINS**\n*ONE AT A TIME*\n>> ")
            if insert.isdigit():
                coindict = [50,20,10,5]
                coin = int(insert)
                if coin in coindict:
                    total += coin
                    if total >= 75:
                         break
                    print("**ACCEPTED**\n*TOTAL:"+str(total)+"p*")
                else:
                    print("**INVALID COIN**\n*TRY AGAIN*")
            else:
                 coindict = [50,20,10,5]
                 print("**INVALID INPUT**\n*ONLY ALLOWS"+str(coindict)+"*")
    print("**DISPENSING**")
    return total, required

def coin_calc():
     global change
     if total > 75:
        change = total - required
        return change
     
def finish():
    if total > 75: 
        print("**CALCULATING**\n*CHANGE:"+str(change)+"p*\n**THANK YOU**")
    else:
        print("**THANK YOU**")
     

def cofe():
    get_coin()
    coin_calc()
    finish()
cofe()