# Write a FUNCTION for each day's puzzle
def day01():
    print("Day 01")
    # Set up empty lists
    left = []
    right = []
    # Read TXT file 
    file = open('day-1-input.txt', 'r')
    split = [line.strip() for line in file]
    for line in split:
        left.append(line.split('  ')[0])
        right.append(line.split('  ')[1])
    # Pair smallest number in LEFT with smallest number in RIGHT list
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    # Iterate from smallest in each to largest
    for (l, r) in zip(sorted_left, sorted_right ):
        print(l, r) # current pair
        # Follow procedure in puzzle instructions



def main():
    # UPDATE this function call for each puzzle
    day01()

if __name__ == "__main__":
    main()
