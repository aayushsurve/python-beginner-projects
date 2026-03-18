print("                             Maths Quiz")
print("                                                                                     ") 

score = 0


name = input("What's your name, genius?:     ")
print(f"Nice to meet you, {name}")
print("                                                                                               ")
q1 = "2*7:  "
q2 = "3*6: "
q3 = "4/2:  "
q4 = "5*8: "
q5 = "6*7:  "

print("                    Let's do a quiz, your score is 0 curently")
limit = int(input("How many questions do you wanna be asked?? (limit 5)"))
       
if limit <= 5:
    for i in range(1, limit+1):
          if i == 1:
            answer_1 = int(input(q1))
            if answer_1 == 14:
                print("Correct!")
                score += 1
            else: 
                print("Wrong!")
                
                
          elif i == 2:
              answer_2 = int(input(q2))
              if answer_2 == 18:
                  print("Correct!")
                  score += 1
              else:
                  print("Wrong!")
                  
             
          elif i == 3:
                  answer_3 = int(input(q3))
                  if answer_3 == 2:
                      print("Correct!")
                      score += 1
                  else:
                      print("Wrong!")
                      
               
          elif i == 4:
                  answer_4 = int(input(q4))    
                  if answer_4 == 40:
                      print("Correct!")
                      score += 1
                  else:
                      print("Wrong!")
                      
                      
          elif i == 5:
                  answer_5 = int(input(q5))
                  if answer_5 == 42:
                      print("Correct!")
                      score += 1
                  else:
                      print("Wrong!")
                      
else:
         print("I said the limit was 5!")                      

if limit <= 5:                                          
                   if score >= 4:
                        print("You did excellent!!!")    
                   elif score >=2 and score < 4:
                       print("You need to do better....")
                   else:
                      print("Study!!")
           
                      








if limit <= 5:
             print(f"Your final score is {score}")


  
  


                  
              
              
              
