def main():
    amount=float(input("How much would you like in coins?"))
    #amount=round(amount,2)
    #amount=amount*100
    #amount=int(amount)
    print("OK, here you go:")
    print_coins(amount)

    #remainingAmount=coinCheck(25,amount)
    #if remainingAmount>0:
    #    remainingAmount=coinCheck(10,remainingAmount)
    #    if remainingAmount>0:
    #        remainingAmount=coinCheck(5,remainingAmount)
    #        if remainingAmount>0:
    #            print("Here's",remainingAmount,"1-cent Coins")
    #            print("A penny a day keeps the doctor away.")
    #    else:
    #        print("Have a nice day.")

    #else:
    #    print("Have a nice day.")

#def coinCheck(coinType,amount):
#    remainder=amount%coinType
#    remainder=round((int(remainder)),2)

#    if remainder == 0:
#        coinCount=int(amount/coinType)
#        print("Here's",coinCount,coinType,"-cent Coins")
#        return 0
#    else:
#        return remainder

def print_coins(amount):
    amount=amount*100
    amount=(round(amount,2))
    amount=int(amount)
    divisible = amount % 25
    divisible=round((int(divisible)),2)

    if divisible == 0:
        quarters=amount/25
        print("Here's ",int(quarters)," quarters")
    else:
        amount=amount-divisible
        quarters=amount/25
        print("Here's ",int(quarters)," quarters")

        remaining=divisible

        remainder=remaining % 10
        if remainder == 0:
            dimes=remaining/10
            print("Here's ",int(dimes)," dimes")
        else:
            remaining=remaining-remainder
            dimes=remaining/10
            print("Here's ",int(dimes)," dimes")

            remaining=int(remainder)
            if remaining < 5:
                print("Here's ",remaining,"pennies")
            else:
                remainder=remaining % 5
                if remainder == 0:
                    print("Here's  1  nickle")
                else:
                    print("Here's  1  nickle")
                    print("Here's ", remainder, " pennies")
main()