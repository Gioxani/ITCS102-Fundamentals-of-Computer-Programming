movie = []

isContinue = True

while isContinue  == True:
    ans = input("do you know any movie?? (Yes/No) ").lower()

    if ans == "Yes":
        title = input(" What is the title of the movie --->")
        movie.append(title)
        ans = input("Do you Wish to continue (yes/no)").lower()
        if ans == "yes":
            print("continue")
            continue
    else:
        print(movie)
        break
