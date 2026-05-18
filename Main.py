print("Welcome to YOUR ANIME FRIEND")

while True:
    choice = input("""
Select the function you want to use:
1 ) Search
2 ) Recommendation
3 ) Close

Please enter 1, 2, or 3 : """)

    if choice == "1":
        import search

    elif choice == "2":
        import recommendation

    elif choice == "3":
        print("\nProgram finished successfully")
        break

    else:
        print("Invalid input. Please enter 1, 2, or 3.")
