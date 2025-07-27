#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if index is within range for both lists
            elem1 = my_list_1[i]
            elem2 = my_list_2[i]
            
            # Attempt division only if both elements are int or float
            if not isinstance(elem1, (int, float)) or not isinstance(elem2, (int, float)):
                print("wrong type")
                result.append(0)
                continue
            # Avoid division by zero
            if elem2 == 0:
                print("division by 0")
                result.append(0)
                continue

            # Successful division
            result.append(elem1 / elem2)
        
        except IndexError:
            print("out of range")
            result.append(0)

        finally:
            pass  # You can leave this empty if no cleanup is needed
    
    return result
