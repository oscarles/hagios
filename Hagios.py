from random import randint

vie1 = 50
vie2 = 50

potion = 3

while True:
    
    if vie1 >= 0 and vie2 >= 0:

        choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if choix == '1':
            attaque = randint(5,10)
            attaque_enememie = randint(5,15)
            vie1 -= attaque_enememie
            vie2 -= attaque
            if vie1 >=0 and vie2 >=0:
                print(f"Vous avez infligé {attaque} de dégats")
                print(f"L'énemie vous a infligé {attaque_enememie} points de dégats")
                print(f"Il vous reste {vie1} points de vie.")
                print(f"Il reste {vie2} points de vie à l'ennemi.")
                print("-" * 5)
            else:
                if vie2 <=0:
                    print(f"Vous avez infligé {attaque} de dégats")
                else:
                    print(f"L'énemie vous a infligé {attaque_enememie} points de dégats")
                    continue


        elif choix == '2':
            soin = randint(15,50) 
            potion -= 1
            print(f"Vous récuperez {soin} de vie ({potion} potions restantes) ")
            vie1 += soin
            attaque_enememie = randint(5,15)
            vie1 -= attaque_enememie
            print(f"L'énemie vous a infligé {attaque_enememie} points de dégats")
            print(f"Il vous reste {vie1} points de vie.")
            print(f"Il reste {vie2} points de vie à l'ennemi.")
            print(f"Il vous reste {potion} potions !")
            print("-" * 5)

            print("Vous passez votre tour ...")
            attaque_enememie = randint(5,15)
            vie1 -= attaque_enememie
            print(f"L'énemie vous a infligé {attaque_enememie} points de dégats")
            print(f"Il vous reste {vie1} points de vie.")
            print(f"Il reste {vie2} points de vie à l'ennemi.")
            print(f"Il vous reste {potion} potions !")
            print("-" * 50)
        else:
            continue

    else:
        
        if vie2 <= 0:
            print(f"Bravos, tu as gagné !")
            print(f"Il te restais {potion} potions !")
            break
        else:
            print(f"Dommage, vous avez perdu, l'enemie avais {vie2} de point de vie ")
            print(f"Il vous restais {potion} potions !")
            break
        





