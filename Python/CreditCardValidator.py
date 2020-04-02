##collect card number from the user
card_number = int(input("Enter your credit card number (Only enter digits in this field!!): "));

##convert the number to a string
card_number_str = str(card_number);

##convert the card number back to an integer and add it to a list
card_number_list = [int(i) for i in card_number_str];

##loop through the list from right to left

##initialize sum_even
sum_even = 0

for i in range(len(card_number_list)-1, -1, -1):
##    to get digits the digits in even positions
##    print(i)
    if i % 2 == 0:
##        print(i)
##        multiply the digit by 2
        double_digit = card_number_list[i] * 2;

##        convert it to a str
        double_digit_str = str(double_digit);

        list_double_digit_str = [int(i) for i in double_digit_str];

        if len(list_double_digit_str) == 2:
            new_digit = list_double_digit_str[0] + list_double_digit_str[1];
        else:
            new_digit = double_digit;

        sum_even += new_digit

print(sum_even)
print(' ')

##initialize sum_odd
sum_odd = 0

for i in range(len(card_number_list)-1, -1, -1):
    if i % 2:
##        print(i)
        sum_odd += card_number_list[i];

print(sum_odd)
print(' ')

total_sum = sum_even + sum_odd;
print(total_sum)
print(' ')


if total_sum % 10 == 0:
    print('Your card is valid')
else:
    print('Your card is invalid')
