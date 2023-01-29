def selection_sort(numbers ,size ):
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            if numbers[j] < numbers[min_index]:
                min_index = j
        (numbers[ind], numbers[min_index]) = (numbers[min_index], numbers[ind])

if __name__== "  main  ":
    numbers = list(map(int, input("Enter integer number with space: "))) 
    size = len(numbers)
    sorted_numbers = selection_sort(numbers ,size )
    print("Sorted number is", sorted_numbers)