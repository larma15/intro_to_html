'''
this program calculates the students final coursework mark.


'''


def tests(test1, test2):
    #check if both test scores are the same
    if test1 == test2: 
        #if both test scores are equal return either one of them
        return test1
    else:
        #if the test scores are diferent return the test 2 
        return test2
#promt the user to enter the marks for test1 and 2
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
its a program that calculates the final courswork mark

'''
def courseWrk(cswork):
    #call the tests function to get the test marks
    testsMark = tests(test1,test2)
    #calculate the average of coursework and the either test mark 
    avgtestsCswork = (cswork + testsMark)/2
    #calculate 40% of the average coursework mark
    fnltestsCswork = avgtestsCswork * (40/100)
    #print a seperator line
    print('..............................')
    #display the final coursework mark
    print('your final coursework marks is: ', fnltestsCswork)
    print('..............................')
#prompt the user to enter the coursework mark
cswork = int(input('Please enter your course work Marks: '))
#call the coursework function to perform the final calculation
courseWrk(cswork)