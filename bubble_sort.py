def bubble_sort(self, numbers):
    n = len(numbers)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j + 1]:
                swapped = True
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        if not swapped:
            return


if __name__== "  main  ":
    numbers = list(map(int, input("Enter integer number with space: "))) 
    sorted_numbers = bubble_sort(numbers)
    print("Sorted number is", sorted_numbers)



