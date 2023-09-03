import sqlite3

# Database initialization and connection
conn = sqlite3.connect('fitness_tracker.db')
cursor = conn.cursor()

# Create the WorkoutLog table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS WorkoutLog (
        id INTEGER PRIMARY KEY,
        date DATE NOT NULL,
        exercise_type TEXT NOT NULL,
        duration INTEGER NOT NULL,
        calories_burned INTEGER NOT NULL
    )
''')
conn.commit()

# Close the connection when the script is done executing
conn.close()


import sqlite3
import datetime

def log_workout(date, exercise_type, duration, calories_burned):
    conn = sqlite3.connect('fitness_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO WorkoutLog (date, exercise_type, duration, calories_burned)
        VALUES (?, ?, ?, ?)
    ''', (date, exercise_type, duration, calories_burned))
    conn.commit()
    conn.close()



def view_workout_history():
    conn = sqlite3.connect('fitness_tracker.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM WorkoutLog ORDER BY date DESC')
    workout_history = cursor.fetchall()
    conn.close()
    return workout_history
def main():
    while True:
        print("\nFitness Tracker Menu:")
        print("1. Log Workout")
        print("2. View Workout History")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            date_str = input("Enter the workout date (YYYY-MM-DD): ")
            exercise_type = input("Enter the exercise type: ")
            duration = int(input("Enter the duration in minutes: "))
            calories_burned = int(input("Enter the calories burned: "))

            try:
                date = datetime.datetime.strptime(date_str, '%y-%m-%d').date()
                log_workout(date, exercise_type, duration, calories_burned)
                print("Workout logged successfully!")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

        elif choice == '2':
            workout_history = view_workout_history()
            print("\nWorkout History:")
            for workout in workout_history:
                print(
                    f"Date: {workout[1]}, Exercise Type: {workout[2]}, "
                    f"Duration: {workout[3]} minutes, Calories Burned: {workout[4]}"
                )

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
