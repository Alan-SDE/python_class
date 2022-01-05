def main():
    # simple calculator to transform number to letter grade

    # prompt for number score
    score = int(input("What is your score (1-100)"))

    # validate input
    if 1 > score or score > 100:
        print("Invalid number, has to be between 1 and 100")
    else:
        # print letter grade based on number
        if score > 90:
            print("you received an A")
        elif score > 80:
            print("you received a B")
        elif score > 70:
            print("you received a C")
        elif score > 70:
            print("you received a D")
        else:
            print("you received an F")


main()
