import sqlite3

# Connect to the SQLite database
db = sqlite3.connect("app.db")
cr = db.cursor()

uid = 1

# Define the main menu message
hello_msg = """
Welcome! 
Enter 'a' to add a skill.
Enter 'u' to update the progress of a skill.
Enter 's' to show skills.
Enter 'd' to delete a skill.
Enter 'q' to quit from the app.

Choose from the options above:
"""

print(hello_msg)

# Get user input
user_input = input("Enter your choice: ").strip().lower()
print(user_input)

# List of valid choices
choices = ['a', 'u', 's', 'd', 'q']

# Define functions for each action


def close_app():
    """Close the database connection."""
    db.commit()
    db.close()
    print("The app is closed.")


def add_skill():
    """Add a new skill."""
    new_skill = input("Enter skill name: ").strip()
    cr.execute(f"SELECT name FROM skills WHERE name='{new_skill}' AND user_id='{uid}'")
    result = cr.fetchone()
    if result is None:
        prog = input("Enter the progress: ")
        cr.execute(f"INSERT INTO skills(name, progres, user_id) VALUES('{new_skill}', '{prog}', '{uid}')")
        print('Skill added successfully.')
    else:
        update_progress = input("You already have this skill. Do you want to update your progress? (y/n)").strip()
        if update_progress.lower() == 'y':
            prog = input("Enter your new progress: ")
            cr.execute(f"UPDATE skills SET progres='{prog}' WHERE name='{new_skill}' AND user_id='{uid}'")
            print("Skill progress updated.")
        else:
            print("No update.")
    close_app()


def update_skill():
    """Update the progress of a skill."""
    skill = input("Enter the skill name: ")
    prog = input("Enter the new progress: ")
    cr.execute(f"UPDATE skills SET progres='{prog}' WHERE name='{skill}' AND user_id='{uid}'")
    print('Skill progress updated.')
    close_app()


def show_skill():
    """Show all skills."""
    cr.execute(f"SELECT * FROM skills WHERE user_id={uid}")
    results = cr.fetchall()
    print(f"You have {len(results)} skills.")
    for row in results:
        print(f"Skill: {row[0]}, Progress: {row[1]}%")
    close_app()


def delete_skill():
    """Delete a skill."""
    skill_name = input("Enter the skill name to delete: ").strip()
    cr.execute(f"DELETE FROM skills WHERE name='{skill_name}' AND user_id={uid}")
    print('Skill deleted.')
    close_app()


# Process user input
if user_input in choices:
    if user_input == 'a':
        add_skill()
    elif user_input == 'u':
        update_skill()
    elif user_input == 's':
        show_skill()
    elif user_input == 'd':
        delete_skill()
    else:
        print("Exiting the program.")
        close_app()
else:
    print("Invalid choice. Please try again.")

