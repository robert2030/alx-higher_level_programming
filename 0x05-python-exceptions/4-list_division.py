#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        switch = 0
        try:
            x = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
            switch = 1
        except TypeError:
            print("wrong type")
            switch = 1
        except IndexError:
            print("out of range")
            switch = 1
        finally:
            if switch:
                switch = 0
                result.append(0)
            else:
                result.append(x)
    return result
