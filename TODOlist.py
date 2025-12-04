tasks=[]

while True:
  print("TODO list app")
  print("1. View the tasks")
  print("2. Add a task")
  print("3. Remove a task")
  print("4. Update a task")
  print("5. Stop")
  choice=input("Choose from 1 to 5: ")
  
  if choice=='1':
    for i in tasks:
      print(i)
  elif choice=='2':
    taskadd=input("What task?: ")
    tasks.append(taskadd)
  elif choice=='3':
    taskrem=input("Which one?: ")
    tasks.remove(taskrem)
  elif choice=='4':
    taskchange1=input("What do you want to change? ")
    taskchange2=input("What do you want to replace it by? ")
    taskfindindex=tasks.index(taskchange1)
    tasks[taskfindindex]=taskchange2
  elif choice=='5':
    print("ok, Bye!")
    break
  else:
    print("invalid")