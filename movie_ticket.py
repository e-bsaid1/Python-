movie_ticket = "Welcome to the movie theater !"
movie_ticket += "Before buy the ticket, tell us how old are you. "

#response = True

#while response:
    
    #age_response = input(movie_ticket)
    #age_int = int(age_response)
    
    #if age_int < 3:
        #print("The ticket is free.")
        #break
        
    #if age_int >= 3 and age_int < 15:
        #print("The ticket is 10$")
        #break
    
    #else:
        #print("The ticket is 15$")
        #break

answer = ''
answer = input(movie_ticket)
answer_activation = True


        

while answer != 'quit' and answer_activation != False: 
    
    if answer == 'quit':
        break
    
    age_int = int(answer) 
    
    if age_int < 3:
        print("The ticket is free.")
        answer_activation = False
        
    if age_int >= 3 and age_int < 15:
        print("The ticket is 10$")
        answer_activation = False
    
    if age_int >= 15:
         print("The ticket is 15$")
         answer_activation = False

    
    
