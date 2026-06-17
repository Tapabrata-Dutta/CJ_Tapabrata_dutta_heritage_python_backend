
def find_max(arr): 

    max_val = arr[0] 

    for num in arr:         

        if num > max_val: 

            max_val = num 

    return max_val 

  


def count_even(arr): 

    count = 0 

    for num in arr:          

        if num % 2 == 0: 

            count += 1 

    return count 


def copy_list(arr): 

    result = [] 

    for item in arr:       

        result.append(item) 

    return result 

  

def read_book(pages): 

    for page in pages:       

        process(page) 

