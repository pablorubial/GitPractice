def sparta():
    """
    SpartaFun function
    This function prints numbers from 1 to 100, replacing multiples of 3 with "Sparta", multiples of 5 with "Fun", and multiples of both with "SpartaFun".
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("SpartaFun")
        elif i % 3 == 0:
            print("Sparta")
        elif i % 5 == 0:
            print("Fun")
        else:
            print(i)
# This function prints numbers from 1 to 100, replacing multiples of 3 with "Sparta", multiples of 5 with "Fun", and multiples of both with "SpartaFun".
