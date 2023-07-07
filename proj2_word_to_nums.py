#TASK 1: converting num words to int

#function provided as "hint" in question itself
def word_to_number(word):
    if word == 'one':
        return(1)
    elif word == 'two':
        return(2)
    elif word == 'three':
        return(3)
    elif word == 'four':
        return(4)
    elif word == 'five':
        return(5)
    elif word == 'six':
        return(6)
    elif word == 'seven':
        return(7)
    elif word == 'eight':
        return(8)
    elif word == 'nine':
        return(9)
    elif word == 'ten':
        return(10)
    elif word == 'eleven':
        return(11)
    elif word == 'twelve':
        return(12)
    elif word == 'thirteen':
        return(13)
    elif word == 'fourteen':
        return(14)
    elif word == 'fifteen':
        return(15)
    elif word == 'sixteen':
        return(16)
    elif word == 'seventeen':
        return(17)
    elif word == 'eighteen':
        return(18)
    elif word == 'nineteen':
        return(19)
    elif word == 'twenty':
        return(20)
    elif word == 'thirty':
        return(30)
    elif word == 'forty':
        return(40)
    elif word == 'fifty':
        return(50)
    elif word == 'sixty':
        return(60)
    elif word == 'seventy':
        return(70)
    elif word == 'eighty':
        return(80)
    elif word == 'ninety':
        return(90)
    elif word == 'hundred':
        return(100)
    elif word == 'thousand':
        return(1000)
    elif word == 'million':
        return(1000000)
    elif word == 'billion':
        return(1000000000)

def standardize_input(words):
    new_list = []
    new_word_list = words.lower().split()
    for item in new_word_list:
        new_num = word_to_number(item)
        new_list.append(new_num)
    return new_list

# result = standardize_input("one two three")
# print(result)

def mult_under999(numbers):
    output = []
    hold = 0

    for i in range(len(numbers)):
        if numbers[i] >= 1000:
            if hold > 0:
                output.append(hold)
                hold = 0
            output.append(numbers[i])
        elif hold == 0:
            hold = numbers[i]
        elif numbers[i] > hold:
            hold *= numbers[i]
            if i == len(numbers) - 1:
                output.append(hold)
        else:
            output.append(hold)
            hold = numbers[i]
            if i == len(numbers) - 1:
                output.append(hold)
    return output


def combine_under999(numbers):
    # to use after mult_999 and add_under999
    hold = 0
    output = []
    for element in numbers:
        if element < 1000:
            hold += element
        else:
            output.append(hold)
            output.append(element)
            hold = 0
    if hold > 0:
        output.append(hold)
    return output



def mult_over999(numbers):
    hold=1
    output=[]
    for i in range(len(numbers)):
        if numbers[i] >=1000:
            hold*=(numbers[i])
            hold*=(numbers[i-1])
            output.append(hold)
            hold=1
        elif i < len(numbers)-1 and numbers[i+1] >= 1000:
            pass
        else:
            hold=numbers[i]
            output.append(hold)
            hold=1
            
    return output


def action(inputstr):
    final_output = 0
    start_list = standardize_input(inputstr)
    final_list = mult_under999(start_list)
    final_list = combine_under999(final_list)
    final_list = mult_over999(final_list)
    final_output = sum(final_list)
    return final_output

# Example usage
result = action('five thousand three hundred thirty three')
print(result)
