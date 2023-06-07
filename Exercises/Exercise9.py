sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

 
while True:
    user_input = input('Enter a word in English or EXIT: ')
    if user_input == 'EXIT':
        break
    if user_input in sample_dict:
        print ('Translation:', sample_dict[user_input])
    else:
        print('No match!')
 
print('Bye!')