stack = []
stack_max, flag = [], False

for i in range(int(input())):
    command = input().split()
    if command[0] == "push":
        stack.append(int(command[1]))
        if flag:
            if int(command[1]) > stack_max[-1]:
                stack_max.append(int(command[1]))
            else:
                stack_max.append(stack_max[-1])
        else:
            flag = True
            stack_max.append(int(command[1]))
    elif command[0] == "pop":
        stack.pop()
        stack_max.pop()
    elif command[0] == "max":
        print(stack_max[-1])