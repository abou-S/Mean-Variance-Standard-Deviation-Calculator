import mean_var_std

def test(liste) :
    try :
        res = mean_var_std.calculate(liste)
        print(res)
        print("TEST PASSED SUCCESSFULLY !")
    except ValueError as e:
        print(e)
    

    
    


