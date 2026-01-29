total_seconds = int(input("Enter the total seconds: "))
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
print(minutes, "minutes and", remaining_seconds, "remaining seconds")