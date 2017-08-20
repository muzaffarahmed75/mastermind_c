while True:
  t=0
  nettim=0
  poss=[str(a*(10**4)+b*(10**3)+c*(10**2)+d*(10)+e).zfill(5) for a in range(8) for b in range(8) for c in range(8) for d in range(8) for e in range(8)]
  while True:
   purp=raw_input("\nDo you wish to be the codemaker or the codebreaker? (m/b/q): ")
   if purp=="m" or purp=="b" or purp=="q":
    break
   else:
    print("\nPlease enter y or n as your response.")
  if purp=="q":
   break
  while True:
   purp2=raw_input("\nReptitions allowed in code? (y/n): ")
   if purp2=="y" or purp2=="n":
    break
   else:
    print("\nPlease enter y or n as your response.")
  from time import time
  from random import randint as r, sample as s
  t1=time()
  if purp2=="n":
   for i in range(len(poss)):
    if len(set(poss[i]))!=5:
     trash.append(poss[i])
  def re(cod_s,att_s):
   cod=list(str(cod_s))
   att=list(str(att_s))
   resp=[]
   for i in range(5):
    ele=cod[i]
    if att[i]==ele:
     resp.append("1")
     cod[i]="69"
     att[i]="77"
   for i in range(5):
    e=att[i]
    if e in cod and e!=cod[i]:
     resp.append("0")
     att[i]="69"
     for t,x in enumerate(cod):
      if x==e:
       cod[t]="69"
       break
   return "".join(sorted(resp,reverse=True))
  def ma(inp):
   dic={}
   allres=['','0','1','00','10','11','000','100','110','111','0000','1000','1100','1110','1111','00000','10000','11000','11100']
   for prores in allres:
    trial=[]
    for i in range(len(poss)):
     if re(poss[i], inp)==prores:
      trial.append(poss[i])
    dic[prores]=len(trial)
   if len(poss)==1:
    return "11111"
   else:
    return max(dic.iterkeys(), key=(lambda key: dic[key]))
  if purp=="m":
    f=s([str(x) for x in range(8)],3)
    f.extend(s(f,2))
    f="".join(s(f,len(f)))
    trash=[]
    nettim+=time()-t1
    while True:
     t2=time()
     t+=1
     nettim+=time()-t2
     if t==1:
      pick=f
      print("\nAttempt no. 1: "+pick)
      t+=1
     while True:
      inres=raw_input("Enter response code: ")
      if inres=="pos":
       print poss
       continue
      if inres=="ok":
       inres="11111"
      if purp2=="y" and len(inres)==0:
       break
      try:
       dec=int(inres,2)
      except ValueError:
       print "\nInvalid response."
       continue
      break
     t1=time()
     prores="".join(sorted(list(inres),reverse=True))
     for i in range(len(poss)):
      if re(poss[i], pick)!=prores:
       trash.append(poss[i])
     poss=list(set(poss)-set(trash))
     pick=poss[r(0,len(poss)-1)]
     nettim+=time()-t1
     if prores=="11111":
      print("\nYour code is "+pick+"\nGuessed in "+str(t)+" attempts and "+str(round(nettim,3))+" seconds.")
      break
     elif len(poss)==1:
      print("\nYour code is "+poss[0]+"\nGuessed in "+str(t)+" attempts and "+str(round(nettim,3))+" seconds.")
      break
     if t>1:
      print("\nAttempt no. "+str(t)+": "+pick+", "+str(100/len(poss))+"%")
  if purp=="b":
    t=0
    while True:
     tria=[]
     while True:
      t+=1
      att=raw_input("\nEnter attempt: ")
      if att=="ft":
       print poss[r(0, len(poss))]
       break
      if len(att)!=5:
       print "\nInvalid attempt."
       continue 
      try:
       dec=int(att,8)
      except ValueError:
       t-=1
       print "\nInvalid attempt."
       continue
      break
     res=ma(att)
     if res=="11111":
      print "The code is "+att+". Guessed in "+str(t)+" attempts."
      if t<8:
       print "Congratulations! You've guessed the code in under 8 attempts! You are a true mastermind!"
     else:
      print "Response: "+res
     for i in range(len(poss)):
       if re(poss[i], att)==res:
        tria.append(poss[i])
     poss=tria
