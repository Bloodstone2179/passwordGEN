def generate(arr, i, s, len):
    global pAmt
    # base case
    if (i == 0):
        # when len has
        # been reached
        with open("output_2.txt", "a") as file:
            file.write(s + "\n")
            pAmt +=1
            p = "{:,}".format(pAmt)
            print(s + " :" + p)
            
            file.close()     
        return

     
    # iterate through the array
    for j in range(0,len):
 
        # Create new string with
        # next character Call
        # generate again until
        # string has reached its len
        appended = arr[j] + s
        
        generate(arr, i - 1, appended, len)
 
    return
 
# function to generate
# all possible passwords
def crack(arr, len):
 
    # call for all required lengths
    for i in range(8 , 9):
        generate(arr, i, "", len)
pAmt = 0
# Driver Code
arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

len = len(arr)
crack(arr,len)





