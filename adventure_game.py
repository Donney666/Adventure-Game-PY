import time
import random


def print_with_delay(msg_to_print):
    # Prints a message with a delay
    print(msg_to_print)
    time.sleep(2)


def print_like_typewriter(message):
    # Prints characters one by one as if typed on a typewriter
    for character in message:
        print(character, end='', flush=True)
        time.sleep(0.1)
    print()


def clear_screen():
    # Clears the console screen.#
    print("\n" * 10)


def intro():
    # Prints the introduction of the game.
    statements = [
        "You find yourself standing in an open field filled"
        " with grass and yellow wildflowers.",
        "Rumor has it that a dangerous creature is somewhere"
        " around here, and has been terrifying the nearby village.",
        "In front of you is a house.",
        "To your right is a dark cave.",
        "In your hand you hold your trusty (but not very effective) dagger."
    ]
    for statement in statements:
        print_with_delay(statement + "\n")


def cave(item, option):
    # Handles the cave scenario.
    if "sword" in item:
        print_with_delay("You peer cautiously into the cave.")
        print_with_delay("You've been here before, and gotten"
                         " all the good stuff. It's just an empty cave now.")
    else:
        print_with_delay("You peer cautiously into the cave.")
        print_with_delay("It turns out to be only a very small cave.")
        print_with_delay("Your eye found something shining behind a rock.")
        print_with_delay("You have found the powerful Sword of Sky!")
        print_with_delay("You discard your silly old dagger"
                         " and equip the sword as your weapon.")
        item.append("sword")
    print_with_delay("You walk back to the field.\n")
    field(item, option)


def house(item, option):
    # Handles the house scenario.
    print_with_delay("You approach the door of the house.")
    print_with_delay("You are about to knock when the door opens and"
                     " out steps a " + option + "!")
    print_with_delay("Eep! This is the " + option + "'s house!")
    print_with_delay("The " + option + " attacks you!\n")
    if "sword" not in item:
        print_with_delay("You feel a bit under-prepared for this, "
                         "what with only having a small dagger.\n")

    while True:
        choice = input("Would you like to (1) fight or (2) run away? ")
        if choice == "1":
            if "sword" in item:
                print_with_delay("As the " + option + " moves to attack,"
                                 " you unsheath your new sword.")
                print_with_delay("The Sword of Sky shines brightly in your"
                                 " hand as you brace yourself for the attack.")
                print_with_delay("But the " + option +
                                 " takes one look at your" +
                                 " shiny new toy and runs away!")
                print_with_delay("You have saved the town" +
                                 " from the " + option +
                                 ". You are victorious!\n")
            else:
                print_with_delay("You have tried your best...")
                print_with_delay("but your dagger is"
                                 " no match for the " + option + ".")
                print_with_delay("YOU DIED!\n")
            play_again()
            break
        elif choice == "2":
            print_with_delay("You run back into the field. Luckily," +
                             " you don't seem to have been followed.\n")
            field(item, option)
            break


def field(item, option):
    # Presents choices to the player and handles their decisions.
    print_with_delay("Enter 1 to knock on the door of the house.")
    print_with_delay("Enter 2 to peer into the cave.")
    print_with_delay("What would you like to do?")

    while True:
        choice = input("(Please enter 1 or 2.) ")
        if choice == "1":
            house(item, option)
            break
        elif choice == "2":
            cave(item, option)
            break


def play_again():
    # Asks the player if they want to play again and handles their response
    while True:
        again = input("GAME OVER\n\nWould you"
                      " like to play again? (y/n) ").lower()
        if again == "y":
            clear_screen()
            play_game()
            break
        elif again == "n":
            print_with_delay("Thanks for playing! See you next time :)\n")
            break


def play_game():
    # Starts the game.
    item = []
    option = random.choice(["dragon", "ghost", "troll", "witch"])
    intro()
    field(item, option)


play_game()
