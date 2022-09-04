# CINEMA BOOKING

films = {
    "Finding Nemo":[5,3],
    "Spiderman":[12,12],
    "Iron Man" :[16,10],
    "Thor Ragnarok": [18,12],
}

while True:
    choice = input("Which Movie do you want to watch?: ").strip().title()
    if choice in films:
        age = int(input("What is your age?: ").strip())
    
    # CHECK USER AGE
    
        if age >= films[choice][0]:
        
        # CHECK NO. OF SEATS
        
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy The Movie")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
                
        else:
            print("You are too young to see that movie...")
    else:
        print("We don't have that film , yet!")