import random

getal = random.randint(1, 1000)

score = 0

for i in range(0,20 ):
    getal = random.randint(1, 1000)
    for i in range(10):
        print ('(Quit om te stoppen)\n')



        gekozengetal = int(input("Kies een getal tussen de 1 t/m 1000! : "))


        if gekozengetal > 1000:
            exit()
        
        elif gekozengetal == (getal):
            print('Geraden')
            score = score + 1
            print ('Jouw score is: '+ str(score))
            break

        elif gekozengetal < (getal):
            print ('Schat hoger!')

            if gekozengetal > getal-20 and gekozengetal < getal+20:
               
                print('Het is heel warm!')
            elif gekozengetal > getal-50 and gekozengetal < getal+50:
                print('het is warm!')

        elif gekozengetal > (getal):
            print ('Schat lager!')

            if gekozengetal > getal-20 and gekozengetal < getal+20:
                print('Het is heel warm!')

            elif gekozengetal > getal-50 and gekozengetal < getal+50:
                print('Het is warm!')
    print("\nEr is een nieuw getal gekozen!")
    print (f"Jouw score = {score}")
    doorspelen = input ('Wil je doorspelen antwoord met ja/nee : ')
    if doorspelen == ('nee'):
        break

    

