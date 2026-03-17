# create a program capable of displaying questions to the users of KBC

# use list data type to store questions and their correct answers

# display the final amount the person is taking home after playing the game

dict_question = {
    1:"Who is the current Prime Minister of India",
    2:"Is Rahul Gandhi is a ??",
    3:"Who is the current President of America?"
}

dict_Options = {
    1:["Modi", "Rahul", "Neharu", "Manmohan"],
    2:["member of opposion party", "Member of legislative assembly", "member of congress", "All of the above"],
    3:["Donald Trump", "Obama", "Biden", "fcc-bin-lagging"]
}

dict_AnsKey = {
    1:"Modi",
    2:"All of the above",
    3:"Donald Trump"
}

score = 0

for key,question in dict_question.items():
    print("\nQuestions", key,":",question)

    options = dict_Options[key]

    # print options with number
    
    for i in range(len(options)):
        print(i+1, ".", options[i])

    # user answer
    user_ans = int(input("Enter the option number:" ))

    selected_option = options[user_ans - 1]

    #check answer
    if selected_option == dict_AnsKey[key]:
        print("Correct Answer")
        score += 5
    else:
        print("Wrong Answer!")
        print("Correct answer was:", dict_AnsKey[key])

    print("\nCurrent score:",score)

print("Final score:", score)




