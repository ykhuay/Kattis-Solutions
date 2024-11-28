def wordle(answer,guess):
    feedback_list = ['-'] * len(answer)
    answer_list = list(answer)
    
    for i in range(len(guess)):
        if guess[i] == answer_list[i]:
            feedback_list[i] = 'G'
            answer_list[i] = None
    
    for i in range(len(guess)):
        if feedback_list[i] == '-' and guess[i] in answer_list:
            feedback_list[i] = 'Y'
            answer_list[answer_list.index(guess[i])] = None
            
    return ''.join(feedback_list)

answer = input().strip()
guess = input().strip()

print(wordle(answer,guess))