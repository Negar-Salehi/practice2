seconds = int(input("Enter Seconds:"))
hours = seconds // 3600
a = (seconds - hours*3600)
minutes = a // 60
second = (a - minutes*60)
print(f"{hours} : {minutes} : {second}")