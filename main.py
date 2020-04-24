while(True):
    print("Welcome to THE BEST MOOD-CHECKER!")
    mood = input("How dou you feel today? ")
    if mood == "Happy":
        print("It is great to see you happy!")
    elif mood == "Nervous":
        print("Take a deep breath 3 times.")
    elif mood == "Sad":
        print("Cheer up and enjoy life!")
    elif mood == ("Excited"):
        print("Take it easy. come down!")
    elif mood == ("Relaxed"):
        print("Wake up, its a short day!")
    elif mood == ("EXIT"):
        print("Saliendo del programa......")
        break
    else:
        print("I do not reconize this Mood.")
        print("Try Happy, Nervous, Sad, Excited or Relaxed")
        print("To leave the program type 'EXIT' ")