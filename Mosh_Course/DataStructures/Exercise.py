# To find the most repeated character in the string below

sentence = "This is a common interview question"
# # To convert the string into a list of characters
# sent = list(sentence)

# # To remove the white spaces from tbe sentence char list
# for x in sent:
#     if x==" ":
#         sent.remove(" ")


# print(sent)
# print(type(str(sent)))
# newSent = str(sent)
# print(newSent)

dict1 = {ch:sentence.count(ch) for ch in sentence if ch!=" "}
print(dict1)