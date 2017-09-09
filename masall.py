from time import time
from random import sample as s, choice as ch
allres=['','0','1','00','10','11','000','100','110','111','0000','1000','1100','1110','1111','00000','10000','11000','11100'] #list of all valid responses
poss=[str(a*(10**4)+b*(10**3)+c*(10**2)+d*(10)+e).zfill(5) for a in range(8) for b in range(8) for c in range(8) for d in range(8) for e in range(8)] #list of all possible codes

def re(cod_s,att_s): #function for generating response, inputs the secret code and attempt, returns response
 cod=list(str(cod_s)) #using list for mutability
 att=list(str(att_s))
 resp=[] #response will be stored in this
 for i in range(5):
  ele=cod[i] #ele = [i]th element of secret code
  if att[i]==ele:
   resp.append('1') #if position and number both match, 1 is appended to resp
   cod[i],att[i]='69','77' #change them to some random numbers because they already have been matched
 for i in range(5):
  e=att[i] #[i]th element of attmept
  if e in cod and e!=cod[i]: #must be in secret code but not at the same position
   resp.append('0') #0 is appended to response
   att[i]='69' #current element in attempt is replaced by a random number
   for t,x in enumerate(cod):
    if x==e: #if some other element of secret code matches, 
     cod[t]='69'
     break
 return "".join(sorted(resp,reverse=True)) #function end

def ma(inp): #the mastermind function, gives the worst-case response to the codebreaker
 dic={} #dic will be used to store response:possibilities pairs
 for prores in allres: #iteration through all_responses
  trial=[] #just a list to count
  for x in poss: #iteration thorough possible secret codes
   if re(x,inp)==prores: trial.append(x) #if respone(element_of_poss,func_inp) is equal to prores, the element is appended to trial
  dic[prores]=len(trial) #each response is associated with the number of secret codes it corresponds to
 if len(poss)==1: return "11111" #if there is no 
 else: return max(dic.iterkeys(), key=(lambda key: dic[key]))
 #the algorithm then returns the response with the maximum possibilities remaining, making it difficult for the codebreaker to guess the code
  
while 1:
  t,nettim,trash=0,0,[] #t is to count number of moves, nettim is to measure time, trash is an empty list which will be used to eliminate possibilites
  while 1:
   purp=raw_input("\nDo you wish to be the codemaker or the codebreaker? (m/b/q): ")
   if purp in ('m','b','q'): break
   else: print("\nPlease enter m, b or q as your response.")
  if purp=='q': break #exit
  while 1:
   purp2=raw_input("\nReptitions allowed in code? (y/n): ")
   if purp2 in ('y','n'): break
   else: print('\nPlease enter y or n as your response.')
  t1=time() #stores current time to t1
  if purp2=='n': #no repetitions allowed
   for x in poss: 
    if len(set(x))!=5: trash.append(x) #if an element in poss has repetitions, it is appended to trash

  if purp=='m': #codemaker
    f=s([str(x) for x in range(8)],3) #three random integers from 0-7 are picked, note that s() is the random.sample() function
    f.extend(s(f,2)) #two of them are picked again
    pick="".join(s(f,len(f))) #we have an attempt of format AABBC, most optimum for first move
    nettim+=time()-t1 #time added
    while 1:
     t+=1
     if t==1:
      print('\nAttempt no. 1: '+pick) #prints the first pick, keep track of the variable pick
      t+=1
     while 1:
      inres=raw_input('Enter response code: ')
      if inres=='pos': #if pos is input, prints all the possible codes at this turn
       print poss
       continue
      if inres not in allres: #allres is the list of all valid responses
       print '\nInvalid response.'
       continue
      break
     t1=time() #stores time
     prores=''.join(sorted(list(inres),reverse=True)) #prores means proper response, sorts the response code
     for x in poss: #iterates through all the possible codes
      if re(x,pick)!=prores: trash.append(x)#if response(selected_code, pick) is not equal to response received, the selected_code is appended to trash
     poss=list(set(poss)-set(trash)) #the trash elements are removed from poss
     pick=ch(poss) #a random code is picked from poss
     nettim+=time()-t1 #difference in time is added to nettim
     if prores=='11111': #correct guess
      print("\nYour code is "+pick+"\nGuessed in "+str(t)+" attempts and "+str(round(nettim,3))+" seconds.")
      break
     elif len(poss)==1: #only one code remaining in poss, that will obviously be the secret code
      print("\nYour code is "+poss[0]+"\nGuessed in "+str(t)+" attempts and "+str(round(nettim,3))+" seconds.")
      break
     if t>1: print("\nAttempt no. "+str(t)+": "+pick+", "+str(round(100.0/len(poss),1))+"%") #prints attempt, attempt number and probability of getting the attempt right
  if purp=='b': #codebreaker
    t=0 #move count
    poss=list(set(poss)-set(trash)) #remove the trash from poss if any
    while 1:
     tria=[] #an empty list to be used later
     while 1:
      t+=1 #increase move count
      att=raw_input("\nEnter attempt: ")
      if att=='ft': #forfeit
       print ch(poss) #a random (valid) code is printed
       break
      if len(att)!=5: #checks length of input attempt
       print "\nInvalid attempt."
       continue
      try: dec=int(att,8) #checks for validity of attempt, must contain only 0-7
      except ValueError:
       t-=1 #drops move count
       print "\nInvalid attempt."
       continue
      break
    
     res=ma(att) #worst-case function
     if res=='11111': #game over
      print "The code is "+att+". Guessed in "+str(t)+" attempts."
      if t<8: print "Congratulations! You've guessed the code in under 8 attempts! You are a true mastermind!"
     else: print "Response: "+res #if game is not over, prints response
     for x in poss: #iterates through poss and 
       if re(x,att)==res: tria.append(x)
     poss=tria
