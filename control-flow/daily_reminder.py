task = input("Enter your task:")
priority = input("Priority(high/medium/low):")
time = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        print("reminder:" f"{task}, is a high priority task that requires immediate attention today!")
    case "medium":
        print("Note:" f"{task}, is a medium priority task. Try to complete it soon")
    case "low":
        print("Note:" f"{task}, is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered")
