import hashlib
import time
import os

def hash_sha1(inp):
    hash_value = hashlib.sha1(inp.encode())
    return hash_value.hexdigest()


def dictionary(dictionary_file, input_hash):
    with open(dictionary_file, 'r+') as f:  # opening the wordlist
        attempts = 0
        start = time.time()
        for line in f:
            attempts += 1
            line = line.rstrip('\n')    # removing the newline character
            #print('trying password', line)
            line1 = hash_sha1(line)  # hashing the password from the wordlist
            if line1 == input_hash:
                print('\n\n Password Found: {}. Found in {} guesses.'.format(line, attempts))
                end = time.time()   # calculating the time required for execution
                print('Time required in secs for cracking the password is', end - start)
                exit(0)
        print('\n\nNo matches found')
        end = time.time()
        print('time required in secs is', end - start)

def insertWord(wordlst,i):
        numlst = [0,1,2,3,4,5,6,7,8,9]
        wordlst.insert(0,numlst[i])
        string = ''.join(map(str,wordlst))
        guess = hashlib.sha1(string.encode('utf-8')).hexdigest()
        return guess,string


def appendWord(wordlst,i):
        numlst = [0,1,2,3,4,5,6,7,8,9]
        wordlst.append(numlst[i])
                       #print(wordlst)
        string = ''.join(map(str,wordlst))
        #print('Guessing the word with digit combination: ',string)
        guess = hashlib.sha1(string.encode('utf-8')).hexdigest()
        return guess,string
        
def GuessHash(string,guess,start):
        
        if guess == input_hash:
           print(f'Password found:{string} with hash: {guess} ')
           end = time.time()
           print('Time required in secs for cracking the password is', end - start)
           exit(0)
        #print(f'The word:{string} is incorrect with hash: {guess} ') 
        

def dictionary_hybrid(dictionary_file):
    with open(dictionary_file, 'r+') as f:  # opening the wordlist
        attempts = 0
        start = time.time()
        for line in f:
            attempts += 1
            line = line.rstrip('\n') # removing the newline character
            wordlst = list(line)   
            sizeoflst = len(wordlst)

            if sizeoflst == 5:
                    
                    #print('Test', wordlst)
                    
                    #print('Test2', wordlst)

                    for i in range(0,10):
                       
                       #insert(wordlst,i)
                       guess,string = insertWord(wordlst,i)
                       
                                          
                       GuessHash(string,guess,start)
                       

                       wordlst.pop(0) 
                       #print('After Pop: ', wordlst) 

                    for i in range(0,10):
                       guess,string = appendWord(wordlst,i)
                       GuessHash(string,guess,start)
                       #print(guess)
                       wordlst.pop(5)
                    
            if sizeoflst == 4:  

                     
                 for i in range(0,10): #DCCCC
                                           
                         guess,string = insertWord(wordlst,i)                                                           
                         GuessHash(string,guess,start)
                         wordlst.pop(0) 
                       

                 for i in range(0,10): #CCCCD
                         guess,string = appendWord(wordlst,i)
                         GuessHash(string,guess,start)
                         wordlst.pop(4)
                   
                 for i in range(0,10):  #DCCCCD
                                         
                    for j in range(0,10):
                        insertWord(wordlst,i)
                        guess,string = appendWord(wordlst,j)
                        GuessHash(string,guess,start)
                        wordlst.pop(0)
                        wordlst.pop(4)

                 for i in range(0,10): #DDCCCC

                    for j in range(0,10):
                        insertWord(wordlst,i)                      
                        guess,string = insertWord(wordlst,j)                                                           
                        GuessHash(string,guess,start)
                        wordlst.pop(0)
                        wordlst.pop(0)
                   
                 for i in range(0,10): #CCCCDD
                     
                      for j in range(0,10):
                          appendWord(wordlst,i)                      
                          guess,string = appendWord(wordlst,j)                                                           
                          GuessHash(string,guess,start)
                          wordlst.pop(5)
                          wordlst.pop(4)
                
            if sizeoflst == 3:
                  for i in range(0,10): #DCCC
                       
                       
                       guess,string = insertWord(wordlst,i)                                                           
                       GuessHash(string,guess,start)
                       wordlst.pop(0) 
                       

                  for i in range(0,10): #CCCD
                       guess,string = appendWord(wordlst,i)
                       GuessHash(string,guess,start)
                       #print(guess)
                       wordlst.pop(3)
                   
                  for i in range(0,10):  #DCCCD
                                         
                     for j in range(0,10):
                        insertWord(wordlst,i)
                        guess,string = appendWord(wordlst,j)
                        GuessHash(string,guess,start)
                        wordlst.pop(0)
                        wordlst.pop(3)
                         
                  for i in range(0,10):    #DDCCC    
                      for j in range(0,10):
                         insertWord(wordlst,i)
                         guess,string = insertWord(wordlst,j)
                         GuessHash(string,guess,start)
                         wordlst.pop(0)
                         wordlst.pop(0)  

                  for i in range(0,10):    #CCCDD    
                      for j in range(0,10):
                        appendWord(wordlst,i)
                        guess,string = appendWord(wordlst,j)
                        GuessHash(string,guess,start)
                        wordlst.pop(4)
                        wordlst.pop(3)   

                  for i in range(0,10):    #DDCCCD    
                      for j in range(0,10):
                        for k in range(0,10):
                            insertWord(wordlst,i)
                            insertWord(wordlst,j)
                            guess,string = appendWord(wordlst,k)

                            GuessHash(string,guess,start)
                            wordlst.pop(0)
                            wordlst.pop(0)
                            wordlst.pop(3) 

                  for i in range(0,10):    #DCCCDD    
                      for j in range(0,10):
                        for k in range(0,10):
                            insertWord(wordlst,i)
                            appendWord(wordlst,j)
                            guess,string = appendWord(wordlst,k)

                            GuessHash(string,guess,start)
                            wordlst.pop(0)
                            wordlst.pop(3)  
                            wordlst.pop(3)  
                  
                  for i in range(0,10):    #DDDCCC   
                      for j in range(0,10):
                        for k in range(0,10):
                            insertWord(wordlst,i)
                            insertWord(wordlst,j)
                            guess,string = insertWord(wordlst,k)

                            GuessHash(string,guess,start)
                            wordlst.pop(0)
                            wordlst.pop(0)  
                            wordlst.pop(0)
                  
                  for i in range(0,10):    #CCCDDD   
                      for j in range(0,10):
                        for k in range(0,10):
                            appendWord(wordlst,i)
                            appendWord(wordlst,j)
                            guess,string = appendWord(wordlst,k)

                            GuessHash(string,guess,start)
                            wordlst.pop(3)
                            wordlst.pop(3)  
                            wordlst.pop(3)
            
            if sizeoflst == 2:
                for i in range(0,10): #DCC
                       
                       
                       guess,string = insertWord(wordlst,i)                                                           
                       GuessHash(string,guess,start)
                       wordlst.pop(0)

                for i in range(0,10): #CCD
                       guess,string = appendWord(wordlst,i)
                       GuessHash(string,guess,start)
                       #print(guess)
                       wordlst.pop(2)

                for i in range(0,10):  #DCCD
                                         
                     for j in range(0,10):
                        insertWord(wordlst,i)
                        guess,string = appendWord(wordlst,j)
                        GuessHash(string,guess,start)
                        wordlst.pop(0)
                        wordlst.pop(2)

                for i in range(0,10):    #DDCC    
                      for j in range(0,10):
                         insertWord(wordlst,i)
                         guess,string = insertWord(wordlst,j)
                         GuessHash(string,guess,start)
                         wordlst.pop(0)
                         wordlst.pop(0)
                
                for i in range(0,10):    #CCDD    
                      for j in range(0,10):
                        appendWord(wordlst,i)
                        guess,string = appendWord(wordlst,j)
                        GuessHash(string,guess,start)
                        wordlst.pop(2)
                        wordlst.pop(2) 
                
                for i in range(0,10):    #DDCCDD    
                      for j in range(0,10):
                        for k in range (0,10):
                            for l in range (0,10):
                             appendWord(wordlst,k)
                             appendWord(wordlst,l)
                             insertWord(wordlst,j)
                             guess,string = insertWord(wordlst,i)
                             
                             GuessHash(string,guess,start)
                             wordlst.pop(4)
                             wordlst.pop(4)
                             wordlst.pop(0)
                             wordlst.pop(0) 

        
        print('\n\n No matches found')
        end = time.time()
        print('time required in secs is', end - start)
       

def combine(*args, **kwds):
    def generate(values, uppper):
        for init in uppper:       # move though all the first levels
            for present in values:   # again iterate through current level
                yield init + (present,)
    iter_list = iter(((),))
    for level in tuple(map(tuple, args)) * kwds.get('repeat', 1):   # generate tuples out of string of characters which are again converted back to tuples
        iter_list = generate(level, iter_list)  # build a list of base iterators over which other characters will iterate through
    return iter_list



def insertNum(code,i):
        numlst = [0,1,2,3,4,5,6,7,8,9]
        code.insert(0,numlst[i])
        
        return code
def combineCode(code):
    codestr = ''.join(map(str,code))
    
    return codestr

def bch(input_hash):
         
    start = time.time()
    code = []
    attempts = 0
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    for e in range(0,10):
                        for f in range(0,10):
                            insertNum(code,f)
                            insertNum(code,e)
                            insertNum(code,d)
                            insertNum(code,c)
                            insertNum(code,b)
                            code = insertNum(code,a)
                            #print('Code:', code)
                            password = ''.join(map(str,code))
                            

                            bch1 = (4*code[0] + 10*code[1] + 9*code[2] + 2*code[3] + code[4] + 7*code[5])%11

                            bch2 = (7*code[0]+8*code[1]+7*code[2]+code[3]+9*code[4]+6*code[5])%11

                            bch3 = (9*code[0] + code[1]+ 7*code[2] + 8*code[3]+ 7*code[4] + 7*code[5])%11

                            bch4 = (code[0]+2*code[1]+9*code[2]+10*code[3]+4*code[4]+ code[5])%11

                            if bch1 ==10 or bch2 ==10 or bch3 ==10 or bch4 ==10:
                                #Number unusable 
                                for i in range(1,7):
                                 code.pop(0)
                            else:
                               code.append(bch1)
                               code.append(bch2)
                               code.append(bch3)
                               code.append(bch4)
                               bch = combineCode(code) #DDDDDD XXXX
                               #print(bch)
                               test = hashlib.sha1(bch.encode('utf-8')).hexdigest()
                               if test == input_hash: #trying to match the hash of the generated password with the input hash
                                 end = time.time()
                                 
                                 print('Time required in secs for cracking the password is', end - start)
                                 print('Password Found: {}. Found in {} guesses.'.format(password, attempts))
                                 exit(0)
                               
                               for i in range(1,11):
                                 code.pop(0)
                            
                            attempts += 1
                            
    
    
              

def bruteforce(input_hash):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789' #string of all the characters that we are iterating over
    attempts = 0
    start = time.time()
    for i in range(1,7):
     for test in combine(chars, repeat=i):
            
            test = ''.join(test)  #combining two of more tuples to form a string
            #print('Guess the password: ', test)
            attempts += 1
            test1 = hash_sha1(test)
            if test1 == input_hash: #trying to match the hash of the generated password with the input hash
                end = time.time()
                print('Time required in secs for cracking the password is', end - start)
                return 'Password found: {}. Found in {} guesses.'.format(test, attempts)
#            print(guess, attempts)



if __name__ == '__main__':
    default_dictionary = os.path.join(os.getcwd(), "dict.txt")

    

    user_options = ['1', '2']
    user_input = input("Input 1 for crack a standard 6-length password, Input 2 for crack a BCH code:")
    while user_input not in user_options:
        print("Please try again")
        user_input = input("1 is for crack a standard password\n"
                            "2 is for crack a BCH code\n"
                            "Input your option: ")
    if user_input=='1':                       
     input_hash = input('Enter the SHA1 hash of the password to be cracked: \n')
     print('Trying to crack the password with dictionary...')
     dictionary(default_dictionary, input_hash)
     print('Word Not Found in the dictionary...')
     print('Trying to crack the password with hybrid dictionary...')
     dictionary_hybrid(default_dictionary)
     print('Trying to crack the password with brute force...')
     print(bruteforce(input_hash))
     exit(0)

    elif user_input == '2':
        input_hash = input('Enter the SHA1 hash of the password to be cracked: \n')
        print(bch(input_hash))
        print('Password not found!')