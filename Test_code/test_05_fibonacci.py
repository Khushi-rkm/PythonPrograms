def fibonacci(number):
    series = []
    a=0
    b=1
    for i in range(number):
        series.append(a)
        a,b=b,a+b
    return series
assert fibonacci(7)==[0,1,1,2,3,5,8]
assert fibonacci(5)==[0,1,1,2,3]
print("All test case passed")