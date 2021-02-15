
from math import * 

def ArrangeIT(inputlst):
    inputlst.sort()
    inputlst.reverse()
    outputList=[]
    for i in range(len(inputlst)): 
        ele = inputlst[i]
        if (i==0):
            outputList.append(ele)  
        else:
            compareele =ele
            for j in range(len(outputList)):
                temp= outputList[j]
                newtemp =int(str(temp)+ str(compareele))
                newele =int(str(compareele)+ str(temp))
                if(  newele>=newtemp):
                    tempswap = temp
                    outputList[j]=compareele
                    compareele= tempswap                 
            outputList.append(compareele)
    result= ''
    for element in outputList:
        result += str(element)
    return result
def main():
    # creating an empty list 
    inputlst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
    for i in range(0, n): 
            number = int(input()) 
            inputlst.append(round(number))
    # Ans=ArrangeDigits(inputlst)
    outputlist= ArrangeIT(inputlst)
    print(outputlist)
    # print(Ans)

main()
