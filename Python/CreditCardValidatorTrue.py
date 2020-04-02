##collect card number from the user
card_number = int(input("Enter your credit card number (Only enter digits in this field!!): "));

##convert the number to a string
card_number_str = str(card_number);

##convert the card number back to an integer and add it to a list
card_number_list = [int(i) for i in card_number_str];

def getPrefix(number, k):
    ##convert the number to a string
    number_str = str(number);

    ##convert the number back to an integer and add it to a list
    number_list = [int(i) for i in number_str];

    if len(number_list) > k:      
        k_number_list = number_list[:k];

        new_number_str = '';

        for i in k_number_list:
            new_number_str += str(i);
        
        return(int(new_number_str))

    else:
        return number

def getSize(number):
    ##convert the number to a string
    number_str = str(number);

    ##convert the number back to an integer and add it to a list
    number_list = [int(i) for i in number_str];

    return len(number_list)
