import smtplib

shovel=[]
i=1
hello=int(1)
upto=int(input("How many emails would you like to send? "))
while i<upto+1:
   number=int(1)
   hello=int(hello+1)
   while number<=hello:
      if hello%number==0:
         shovel.append(number)
         number+=1
      else:
         number+=1
   if len(shovel)==2:
      fromaddrs = 'put your email here'
      toaddrs  = 'put the email you want to spam here'
            
      msg = str(hello)
      username = 'put your email here'
      password = 'put your password for email here'
      server = smtplib.SMTP("smtp.gmail.com:587")
      server.starttls()
      server.login(username,password)
      server.sendmail(fromaddrs, toaddrs, msg)
      print("You have sent "+str(i)+" emails so far")
      server.quit()            
      i+=1
      del shovel[:]
   
   else:
      hun=1
      del shovel[:]
