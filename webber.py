import webbrowser

#Variable
score = 0
webopens = 0
websearches = 0
ytsearches = 0
is_vip = False

#Instruction
print("""
Funtions Supported ( Version 1.0 ):
    1) Type 'open-web' to open websites using thier url
    2) Type 'search-web' to search google
    3) Type 'search-youtube' to search youtube
    4) Type 'my-score' to check your current MSA Score
    5) Type 'my-webopens' to check all the number of websites you opened
    6) Type 'my-websearches' to check how many searches you did till now
    7) Type 'my-ytsearches' to check all youtube searches you did till now
    8) $Buy VIP$ :: Type "buy-vip" to Buy All VIP Stuff

    VIP ONLY
    --> Type 'play-games' to play games
    --> Type 'get-points-20' to get 20 points
    --> Type 'read-wiki' to read about someone from wikipedia
    
""")

#While Loop
while True:
    print("")
    usr_inp = input("Command: ")

    #Open Websites
    if usr_inp == "open-web":
        weburl = input("Enter Website URl: ")
        webbrowser.open(weburl)
        score = score+5
        webopens = webopens+1

    #search google
    elif usr_inp == "search-web":
        query = input("What Would you like to search: ")
        searchwebqueryurl = "https://www.google.com/search?q=" + query
        webbrowser.open(searchwebqueryurl)
        score= score + 10
        websearches = websearches+1


    #search youtube
    elif usr_inp == "search-youtube":
        query_yt = input("What Would you like to search: ")
        searchytqueryurl = "https://www.youtube.com/results?search_query=" + query_yt
        webbrowser.open(searchytqueryurl)
        score= score + 10
        ytsearches = ytsearches+1

    #check score
    elif usr_inp == "my-score":
        if score>0 and score<50:
            print("Your State is: Begineer")
            print("Your Current Score is: ",score)

        elif score>50 and score<300:
            print("Your State is: Intermadiate")
            print("Your Current Score is: ",score)

        elif score>300:
            print("Your State is: Pro")
            print("Your Current Score is: ",score)

    #Check Web Opens
    elif usr_inp == "my-webopens":
        if webopens>0 and webopens<5:
            print("Your State is: Begineer")
            print("Number of Websites you opened is: ",webopens)

        elif score>5 and score<30:
            print("Your State is: Intermadiate")
            print("Number of Websites you opened is: ",webopens)

        elif score>30:
            print("Your State is: Pro")
            print("Number of Websites you opened is: ",webopens)

    #Check Web Searches
    elif usr_inp == "my-websearches":
        if score>0 and score<50:
            print("Your State is: Begineer")
            print("Number of searchess you did is: ",websearches)

        elif score>50 and score<300:
            print("Your State is: Intermadiate")
            print("Number of searchess you did is: ",websearches)

        elif score>300:
            print("Your State is: Pro")
            print("Number of searchess you did is: ",websearches)

    #Check Youtube Searches
    elif usr_inp == "my-ytsearches":
        if score>0 and score<50:
            print("Your State is: Begineer")
            print("Number of searchess you did is: ",ytsearches)

        elif score>50 and score<300:
            print("Your State is: Intermadiate")
            print("Number of searchess you did is: ",ytsearches)

        elif score>300:
            print("Your State is: Pro")
            print("Number of searchess you did is: ",ytsearches)

    #Buy VIP
    elif usr_inp == "buy_vip":

        #If Score is More then 200
        if score >= 10:
            ask_issure = input("Are You Sure ( y/n ): ").lower()
            if ask_issure == "y":
                print("you are a VIP Now")
                is_vip = True
                score = score-0

            elif ask_issure == "n":
                pass

        elif score < 200:
            is_vip = False
            print("Sorry, to buy vip you must have a score of 200 or more")

    #Vip Command: Play Games
    elif usr_inp == "play-games":
        if is_vip == True:
            webbrowser.open("https://poki.com")

        else:
            webbrowser.open("https://www.google.com/search?q=sorry%2C+you+are+not+a+vip+member&rlz=1C1CHZN_enIN1027IN1027&sxsrf=ALiCzsbqG712_NmsbsTtQnMpfkkefQV5Hw%3A1666180520598&ei=qOVPY4uRJNTiseMP2dWvuAo&ved=0ahUKEwiLhb-Qnuz6AhVUcWwGHdnqC6cQ4dUDCA8&uact=5&oq=sorry%2C+you+are+not+a+vip+member&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIFCCEQoAE6BAgjECc6BAguEEM6BAgAEEM6BQgAEIAEOhAILhCxAxCDARDHARDRAxBDOgsIABCABBCxAxCDAToKCAAQsQMQgwEQQzoFCC4QgAQ6CQgjECcQRhD5AToKCC4QsQMQ1AIQQzoHCC4Q1AIQQzoICAAQgAQQsQM6CgguELEDEIMBEEM6BwguELEDEEM6BQgAEIYDOggILhCABBDUAjoGCAAQFhAeOggIABAWEB4QCjoKCCEQFhAeEA8QHToHCCEQoAEQCkoECE0YAUoECEEYAEoECEYYAFAAWKNIYKNUaABwAXgAgAHsAYgB9COSAQYwLjI4LjOYAQCgAQHAAQE&sclient=gws-wiz")

    #Vip Command: Get Points
    elif usr_inp == "get-points-20":
        if is_vip == True:
            score = score + 20
            print("20 Points have been added to your score")

        else:
            webbrowser.open("https://www.google.com/search?q=sorry%2C+you+are+not+a+vip+member&rlz=1C1CHZN_enIN1027IN1027&sxsrf=ALiCzsbqG712_NmsbsTtQnMpfkkefQV5Hw%3A1666180520598&ei=qOVPY4uRJNTiseMP2dWvuAo&ved=0ahUKEwiLhb-Qnuz6AhVUcWwGHdnqC6cQ4dUDCA8&uact=5&oq=sorry%2C+you+are+not+a+vip+member&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIFCCEQoAE6BAgjECc6BAguEEM6BAgAEEM6BQgAEIAEOhAILhCxAxCDARDHARDRAxBDOgsIABCABBCxAxCDAToKCAAQsQMQgwEQQzoFCC4QgAQ6CQgjECcQRhD5AToKCC4QsQMQ1AIQQzoHCC4Q1AIQQzoICAAQgAQQsQM6CgguELEDEIMBEEM6BwguELEDEEM6BQgAEIYDOggILhCABBDUAjoGCAAQFhAeOggIABAWEB4QCjoKCCEQFhAeEA8QHToHCCEQoAEQCkoECE0YAUoECEEYAEoECEYYAFAAWKNIYKNUaABwAXgAgAHsAYgB9COSAQYwLjI4LjOYAQCgAQHAAQE&sclient=gws-wiz")
         