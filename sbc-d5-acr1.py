def wala():
    print(line)
    print("Remove from line:", line[-1])
    line.pop(-1)
    print(line)
#function for queue
def naa():
    print(line)
    print("Removed from line:", line[0])
    line.pop(0)
    print(line)

line = []
line_lenght = int(input("Enter the lenght of the line:"))

for l in range(1,line_lenght + 1):
        line.append(l)

print("Process Line:", line)

for c in range(len(line)):
    Boss_Status = input("Naa si boss wala? naa/wala:")
    Boss_Status.lower

    if Boss_Status == "wala":
         wala()

    elif Boss_Status == "naa":
         naa()

    else:
         print("Invalid input. Please enter 'naa' or 'wala'")
         break

    
