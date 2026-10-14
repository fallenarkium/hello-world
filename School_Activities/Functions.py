#Steven Herrera
#BSCpe 1A
#26-00320
#bad apple

health = 100
option = ""

def my_function(decision, current_health):
    if decision == 1:
        if current_health == 100:
            print("Full health")
        elif current_health < 100:
            current_health = current_health + 20
            print("Health +20")
    if decision == 2:
        current_health = current_health - 20
        if current_health == 0:
            print("You died")
        elif current_health > 0:
            print("Health -20")
    return current_health

while option != "x" and health != 0:
    print("Health =", health)
    print("Enter [1] = eat apple.")
    print("Enter [2] = eat bad apple.")
    print("Enter [x] = end program.")

    option = input("Enter your choice: ")
    print()

    if option == "1":
        health = my_function(int(option), health)
    elif option == "2":
        health = my_function(int(option), health)
