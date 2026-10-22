def check_number(number):
    if number>0:
        return"positive"
    elif number<0:
        return"negative"
    else:
        return"zero"
print(check_number(13))