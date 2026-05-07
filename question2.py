# Question 2: Average Score Calculator
def calculate_average():
    try:
        # Accepting three test scores from the user
        score1 = float(input("Enter first test score: "))
        score2 = float(input("Enter second test score: "))
        score3 = float(input("Enter third test score: "))

        # Calculating the average
        average = (score1 + score2 + score3) / 3

        # Displaying the scores and the average
        print("\n--- Results ---")
        print(f"Score 1: {score1}")
        print(f"Score 2: {score2}")
        print(f"Score 3: {score3}")
        print(f"The average score is: {average:.2f}")

    except ValueError:
        # Error handling for invalid inputs
        print("Error: Invalid input. Please enter numerical values only.")

# Run the function
if __name__ == "__main__":
    calculate_average()
