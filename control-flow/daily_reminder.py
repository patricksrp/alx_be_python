Task = input("Enter your task: ").strip()
Priority = input("Priority (high/medium/low): ").strip().lower()
Time_Bound = input("Is it time-bound? (yes/no): ").strip().lower()

reminder = f"Reminder :'{Task}' is a "
match Priority:
    case "high":
        reminder += "high priority task"
    case "medium" :
        reminder += "medium priority task"
    case "low" :
        reminder += "low priority task" 
    case _:
        message = f"{Task} has an unkown priority level"

if Time_Bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if Priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ". Make sure to complete it soon."

print(reminder)