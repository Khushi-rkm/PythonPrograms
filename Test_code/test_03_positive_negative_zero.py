def check_number(number):
    if number>0:
        return"positive"
    elif number<0:
        return"negative"
    else:
        return"zero"
    assert check_number(10)=="positive"
    assert check_number(-5)=="negative"
    assert check_number(0)=="zero"
print("All test case passed")