power_on = True

user_menu_choice = 0

sub_menu_choice = 0

#while power_on != True:

print ('\t Welcome To Nokia 3310 🤝 ')

print ("1. Phone book");
print ("2. Messages");
print ("3. Chat");
print ("4. Call register");
print ("5. Tones");
print ("6. Settings");
print ("7. Call divert");
print ("8. Games");
print ("9. Calculator");
print ("10.Reminders");
print ("11.Clock");
print ("12.Profiles");
print ("13.SIM services");
print ("0. Exit");
print ("Enter choice: ");

user_menu_choice = int(input())

match user_menu_choice:
    case 1 :
        print("\t ==== PHONE BOOK ☎️ ==== \n")
        print("1. Search")
        print("2. Service Nos.")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign tone")
        print("7. Send b'card")
        print("8. Options")
        print("9. Speed dials")
        print("10.Voice tags")
        print("Enter choice: ")

sub_menu_choice = int(input())
        
