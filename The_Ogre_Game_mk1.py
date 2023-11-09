from random import randint

print("Hi. You've encountered some ogres. What will you do?")

number_of_ogres = 4
player_health = 8
first_aid = 3

print("There are", number_of_ogres, "ogres")
print("Your health is", player_health)

while number_of_ogres > 0 and player_health > 0:
    choice = input("Shall you fight them or try to retreat and prepare for another try? (y/n/r) ").lower()

    if choice == "y":
        ogre_power = randint(1, 8)
        player_power = randint(1, 10)

        if ogre_power > player_power:
            player_health -= 2
            if player_health < 1:
                player_health = 0
            print("* You were harmed during fight, the ogre is still alive and you're wounded. *")
            print("* Your health is now", player_health, "*")

            if player_health <= number_of_ogres and first_aid == 0:
                print("You're too weak, cannot win this.")
                print("That is the end.")
                break

        else:
            number_of_ogres -= 1
            player_health -= 1
            print("* Victory. There are now", number_of_ogres, "ogres remaining *")
            print("* You were wounded, your health is", player_health, "*")

            if player_health <= 0:
                print("You have died.")
                break

            elif player_health > 0:
                print("Must continue the fight.")
                continue

    elif choice == "n":
        print("You chose not to fight. The ogres continue their way and you lived to see another day.")

    elif choice == "r":
        if first_aid > 0:
            chance_for_first_aid = randint(1, 100)
            if chance_for_first_aid > 70:
                player_health += 2
                print("You were able to patch yourself up quite well, your health is now", player_health)
            elif chance_for_first_aid <= 70 and chance_for_first_aid > 30:
                player_health += 1
                print("You were able to freshen yourself a bit, your health is now", player_health)
            elif chance_for_first_aid < 30:
                player_health = 0
                print("You managed to bandage your head so tightly that you suffocated.")
                break

    else:
        print("Incorrect input. Please choose 'y' to fight or 'n' to avoid combat. ")

if number_of_ogres == 0 and player_health > 0:
    print("Congratulations! You've defeated all the ogres and survived.")
elif player_health <= 0:
    print("Your health has been depleted. You've been defeated by the ogres.")
