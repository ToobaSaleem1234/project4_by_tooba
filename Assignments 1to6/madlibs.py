# MadLibs Game: Short Story

def madlibs_game():
    print("""
          Welcome to the MadLibs Game!
          """)
    print("Fill in the blanks to complete the story.\n")

    # User inputs
    name = input("Enter a name (person): ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective (day): ")
    noun = input("Enter a noun (person): ")
    verb = input("Enter a verb: ")
    person = input("Enter an name (person): ")

    # Story template
    story = f"""
    Once upon a time, {name} went to {place}. It was a very {adjective} day.
    Suddenly, {name} saw a {noun} that was trying to {verb}. 
    To their surprise, {person} appeared and joined them!
    It was the most unforgettable day for them.
    """

    # Display the completed story
    print("\nHere is your story:\n")
    print(story)

madlibs_game()