def main():
    print("Welcome to the Hollywood Movie Rating Guide!")
    print("Rate the movie from 0 to 4 stars. Enter a negative number to quit.")

    total_stars = 0
    num_ratings = 0

    while True:
        try:
            rating = float(input("Enter your rating (0-4): "))
            if rating < 0:
                break
            elif 0 <= rating <= 4:
                total_stars += rating
                num_ratings += 1
            else:
                print("Invalid rating. Please enter a value between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if num_ratings > 0:
        average_rating = total_stars / num_ratings
        print(f"The average star rating for the movie is: {average_rating:.2f}")
    else:
        print("No ratings were entered.")

if __name__ == "__main__":
    main()