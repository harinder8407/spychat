from spydetails import spy, friends, Colors, Chatmessage, Spy
from steganography.steganography import Steganography
from datetime import datetime

print("Hello! Let\'s get started")

STATUS_MESSAGE = ['My name is bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up , Sir']


question = input('Do you want to continue as ' + spy.name + '!Y/N')


def average_chat(sel_friend, text):
    if len(text.split()) > 100:
        print("spy is speaking to much ")
        del friends[sel_friend]


# function for special secret world send by sender spy it will handle


def check_special_words(a):
    if a == "NEW":
        print(Colors.RED + "spy have new mission ")
    elif a == "SAVE ME":
        print(Colors.RED + "spy is in danger")
    elif a == "PROGRESS":
        print(Colors.RED + "spy's missing is in progress")
    elif a == "WORK":
        print(Colors.RED + "spy is working  on other mission")
    else:
        print(Colors.ORANGE + "no special word used by sender" + Colors.BLACK)


def send_message():
    friend_choice = select_friend()
    orignal_image = input('What is name of the image')
    output_path = 'output.jpg'
    text = input('Wha do you want to say')
    Steganography.encode(orignal_image, output_path, text)
    # call the chatmessage class by new_chat object
    new_chat = Chatmessage(text, True)
    # adding the text to selected friend in chats(in spy class)
    friends[friend_choice].chats.append(new_chat)
    print("your secret message is ready ")


def read_message():
    sender = select_friend()
    output_path = input('What is the name of file')
    secret_text = Steganography.decode(output_path)
    secret_text = secret_text.upper()
    # to handle no secret message
    if len(secret_text) == 0:
        print("there is no secret message")
    else:
        average_chat(sender, secret_text)
        # to print no of words split the secret_text then find lenght by len() && split() is important otherwise error
        print("he no of words in secret message :" + str(len(secret_text.split())))
        # calling check_special_words for checking special secret message in secre_ttext
        check_special_words(secret_text)
        print("the secret text is :" + secret_text)
        # calling chatmessage class by new_chat object
        new_chat = Chatmessage(secret_text, False)
        # appending the new_chat in chats for selcted friend
        friends[sender].chats.append(new_chat)
        print("your secret message has been saved ")


# function for reading chat history
def read_chat_history():
    read_for = select_friend()
    print("in the read chat")
    for i in friends[read_for].chats:
        if i.sent_by_me:
            print(Colors.BLUE + "Time:[%s]" % (
                i.time.strftime("%d %B %Y")) + Colors.RED + "you said:" + Colors.BLACK + "%s" % i.message)
        else:
            print(Colors.BLUE + "Time:[%s]" % (i.time.strftime("%d %B %Y")) + Colors.RED + "%s:" % friends[
                read_for].name + Colors.BLACK + "%s" % i.message)


def select_friend():
    item_position = 0
    # showing the all friends from friends dictionary
    for friend in friends:
        print("%d. %s age: %s with ratting %.2f is online" % (item_position, friend.name, friend.age, friend.rating))
        item_position = item_position + 1
    friend_choice = int(input("choose your friend"))
    return friend_choice


def age_val(spy_age):
    age_validation = True
    if 12 < spy_age <= 50:
        age_validation = True
        print("spy is of valid age")
    else:
        age_validation = False
        print("sorry!! you are not of a correct age to be a spy")
    return age_validation


# funtion for name validation
def name_vali(spy_name):
    # initialy we set validation as true if name is invalid we will set validation=False
    # when name is valid set validation to true
    validation = True
    if spy_name.isspace():
        validation = False
        print("Invalid! you enter space \n A spy need to have valid name ")
    elif spy_name.isdigit():
        validation = False
        print("Invalid! you enter digit \n A spy need to have valid name ")
    elif spy_name.isalpha():
        validation = True
    elif len(spy_name) == 0:
        validation = False
        print("A spy need to have valid name , please try again ")
    # returning  validation
    return validation


def add_friend():
    new_friend = Spy('', '', 0, 0.0)

    new_friend.name = input("please ! add your friends name ? ")
    name = new_friend.name
    new_friend.salutation = input("Are they MR OR MS")
    new_friend.name = new_friend.salutation + " " + name
    new_friend.age = int(input("enter age ?"))
    new_friend.rating = float(input("spy rating ?"))

    if len(new_friend.name) > 0:
        print("spy name is not empty")

        if (name_vali(name) is True) and age_val(new_friend.age):
            friends.append(new_friend)

    else:
        print("sorry invalid entry . we can't add spy with details you provided")
    # return the no of friends in dictionary
    return len(friends)


def add_status(current_status_message):
    new_status = None
    if current_status_message is not None:
        print('Your current status is:' + current_status_message)
    else:
        print('you don\'t have any status at this moment')

    default = input('Do you want to select status from old status? Y/N:')
    if default.upper() == 'N':
        new_status = input('Enter your new status')

        if len(new_status) > 0:
            STATUS_MESSAGE.append(new_status)
    else:
        for i in STATUS_MESSAGE:
            print(str(STATUS_MESSAGE.index(i)) + '.' + i)
        message_selection = int(input('which status update you want to update'))
        if len(STATUS_MESSAGE) > message_selection:
            new_status = STATUS_MESSAGE[message_selection - 1]
    return new_status


def start_chat(spy):
    current_status_message = None
    print("your current status is " + str(current_status_message))
    show_menu = True
    while show_menu:
        menu_choices = 'Do you want to do?\n1.Add a status update \n2. Close application'
        menu_choice = input(menu_choices)

        if menu_choice == 1:
            print('you chose to update status')
            current_status_messesge = str(add_status(current_status_message))
            print("Your selected status is:" + current_status_messesge)

        elif menu_choice == 2:
            number_of_friend = add_friend()
            print("You have %s friends" % number_of_friend)
        elif menu_choice == 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            read_chat_history()
        else:
            show_menu = False


if question.upper() == 'Y':
    start_chat(spy)
else:
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False,
    }
    # user wants new spy
    spy_name = input("welcome to spy chat, you must tell me your name first  ?")
    spy_name = spy_name.upper()

    if len(spy_name) > 0:
        print("validation is successful ! you enter valid name. ")
        print('Welcome ' + spy_name + ' glad to see u again')
        spy_salu = input('Should we call u? (Mr. or Ms.)')
        print(spy_salu + ' ' + spy_name)
        print("Okay" + spy_name + "i'd like to know a little bit more about you before we proceed")

        spy_rating = 0.0
        spy_status = False

        spy_age = int(input('Enter your age'))
        if age_val(spy_age):
            spy_rating = float(input('Enter your rating'))

            if spy_rating > 4.5:
                print('You are an ace!')
            elif 3.5 < spy_rating <= 4.5:
                print('you are one of the good ones')
            elif 2.5 <= spy_rating <= 3.5:
                print('you can do better')
            else:
                print('you can help others at office')

            spy_status = True

            print(Colors.GREEN + 'Authentication completed! welcome' + spy_name + ' age:' + str(
                spy_age) + ' rating:' + str(spy_rating))

            start_chat(spy)
        else:
            print('Sorry! you are not at the correct age to be spy')
