def deco_result(result_func):
    def distinction(marks):
        for e in marks:
            if e >= 75:
                print("Distinction")
            else:
                result_func(marks)
    return distinction

@deco_result
def result(marks):
    for e in marks:
        if e >= 33:
            pass
        else:
            print("Fall")
            break
    else:
        print("Pass")

result([50,55,70,80,90])