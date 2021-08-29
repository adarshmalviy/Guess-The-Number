n=20
i= 1
print("\t\t\t***********LET'S GO!!************")
q=int(input("\nenter Number:"))

while(q!=n):
        for i in range(0,5):
            if q>n:
                print("\nChances Reamining::",5-i)
                q=int(input("\nEnter Again!. Hint: Smaller Number\n"))
            elif q<n:
                print("\nChances Reamining::", 5-i)
                q = int(input("\nEnter Again!. Hint: Larger Number\n"))
            elif q==n:
                break
        else:
            print("\n**** GAME OVER! :( ****")
            break
else:
    print("\n **** CONGRATULATIONS :) . YOU GOT IT CORRECT. ****")
    print("Number of Guesses You took to finish:",i)
