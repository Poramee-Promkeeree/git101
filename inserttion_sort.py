def insertion_sort(self, numbers):
    if (n := len( numbers)) <= 1:
      return
    for i in range(1, n):  
        key = numbers[i]
        j = i-1
        while j >=0 and key < numbers[j] :
                numbers[j+1] = numbers[j]
                j -= 1
        numbers[j+1] = key

if __name__== "  main  ":
    numbers = list(map(int, input("Enter integer number with space: "))) 
    sorted_numbers = insertion_sort(numbers)
    print("Sorted number is", sorted_numbers)