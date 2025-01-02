def Test(x,output):
    B = x%8
    B = B^4
    B = B^(x//2**B)
    B = B^4
    if (B%8) != output:
        return -1
    x = x // 8
    return x

def Trial(x,n,i,Inputs):
    if i >= len(Inputs):
        return x,True
    found = False
    while not(found):
        case = Test(n,Inputs[i])
        if case == x and n != 0:
            n,possible = Trial(n,n*8,i+1,Inputs)
            if possible:
                return n,True
        elif case > x:
            return x+1,False
        else:
            n += 1

Inputs = [2,4,1,4,7,5,4,1,1,4,5,5,0,3,3,0]
Inputs.reverse()
##num = Trial(0,1,0,Inputs)
##print(num)
print(Test(38326496880,7))
