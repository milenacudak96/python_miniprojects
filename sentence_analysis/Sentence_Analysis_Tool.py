'''
Write a script that takes a sentence from the user and returns:

the number of lower case letters
the number of uppercase letters
the number of punctuations characters
the total number of characters
Use a dictionary to store the count of each of the above.
'''

sentence = input('tell me your sentence: ')

count = 0
for letter in sentence:
    if letter.islower():
        count = count + 1
print('the number of lower case letters is: ' + str(count))


counter = 0
for letter in sentence:
    if letter.isupper():
        counter = counter + 1
print('the number of upper case letters is: ' + str(counter))

counter1 = 0
for letter in sentence:
    if letter in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):
        counter1 = counter1 + 1
print('the number of punctuations is: ' + str(counter1))

counter2 = 0
for letter in sentence:
        counter2 = counter2 + 1
print('the number of characters is: ' + str(counter2))

