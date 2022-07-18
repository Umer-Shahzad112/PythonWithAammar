# def print_codanics():
#     text = "We are learning Python Aammar"
#     print(text)
#     print(text)
#     print(text)

# print_codanics()
# print_codanics()

#method 2

# def print_condanics(text):
#     print(text)
#     print(text)
#     print(text)

# print_condanics('hello')



def school_calculator(age,text ):
    text = text.capitalize() 
    if age >=15:
        print(text+"should go to high school")
    elif age >= 5:
        print(text+' can be admitted')
    else:
        print(text+"can't be admitted")

school_calculator(5,'ali')