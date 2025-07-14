Task = input("Enter your task: ").strip()
Priority = input("Priority (high/medium/low): ").strip().lower()
Time_Bound = input("Is it time-bound? (yes/no): ").strip().lower()

match Priority:
    case "high":
        message = f"Reminder: '{Task}' is a high priority task"
    case "medium" :
        message = f"Note: '{Task}' is a medium priority task"
    case "low" :
        message = f"Note: '{Task}' isa low priority task"   
    case _:
        message = f"{Task} has an unkown priority level"

if Time_Bound == "yes":
    message += " that requires immediate attention today!"
else:
    message +=". Consider completing it when you have free time."

print("\n" + message)        