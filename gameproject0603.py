import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def intro(house_owner):
    print_pause("You find yourself standing in an open field," +
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + house_owner +
                " is somewhere around here, " +
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty" +
                " (but not very effective) dagger.")


def house(house_owner, items):
    # things happen while the player choose to go to the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "
                + house_owner + ".")
    print_pause("Eep! This is the " + house_owner + "'s house!")
    print_pause("The " + house_owner + " attacks you!")
    if "sword" in items:
        print_pause("The Sword of Ogoroth shines brightly in your hand " +
                    "as you brace yourself for the attack.")
        fight(house_owner, items)
    else:
        print_pause("You feel a bit under-prepared for this, " +
                    "what with only having a tiny dagger.")
        fight(house_owner, items)


def fight(house_owner, items):
    # things happen while the player fights
    decision = input("Would you like to (1) fight or (2) run away?")
    if decision == "1":
        if "sword" in items:
            print_pause("As the " + house_owner +
                        " moves to attack, you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand" +
                        " as you brace yourself for the attack.")
            print_pause("But the " + house_owner +
                        " takes one look at your shiny new toy and runs away!")
            print_pause("You have rid the town of the " + house_owner +
                        ". You are victorious!")
            play_again()

        elif "sword" not in items:
            print_pause("You do your best..." +
                        "but your dagger is no match for the "
                        + house_owner + ".")
            print_pause("You have been defeated!")
            play_again()
    elif decision == "2":
        print_pause("You run back into the field. " +
                    "Luckily, you don't seem to have been followed.")
        choice(house_owner, items)


def cave(house_owner, items):
    # things happen while the player choose to go to the cave
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, " +
                    "and gotten all the good stuff. " +
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        choice(house_owner, items)

    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger " +
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("sword")
        choice(house_owner, items)


def choice(house_owner, items):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    player_choice = input("What would you like to do?\n" +
                          "(Please enter 1 or 2.)")
    if player_choice == "1":
        house(house_owner, items)
    elif player_choice == "2":
        cave(house_owner, items)
    else:
        print_pause("Sorry, I don't understand")
        choice(house_owner, items)


def play_again():
    again = input("GAME OVER!\n" "Would you like to play again? (y/n)")
    if again == "y":
        play_game()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.")


def play_game():
    items = []
    monsters = ["troll", "pirate", "dragon", "gorgon", "wicked fairie"]
    house_owner = random.choice(monsters)
    intro(house_owner)
    choice(house_owner, items)


play_game()
