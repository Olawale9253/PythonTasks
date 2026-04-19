power_on = True
user_menu_choice = 0

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

user_menu_choice = int(input('Select from Phone Menu'))

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

match sub_menu_choice:

    case 1 :
        print("Search: Find name and phone number")
    case 2:
        print("Service Nos.: Call service provider")
    case 3:
        print("Add name: Store name and phone number")
    case 4:
        print("Erase: Delete names and numbers")
    case 5:
        print("Edit: Modify stored names/numbers")
    case 6:
        print("Assign tone: Set ringing tone for caller")
    case 7:
        print("Send b'card: Send name/number to another phone")
    case 8:
        print("Options: Type of view / Memory status")
    case 9:
        print("Speed dials: Assign number keys for speed dialing")
    case 10:
        print("Voice tags: Record voice tags for dialing")
    
match user_menu_choice:

    case 2:

        print("\t ==== MESSAGES ✉️  ==== \n")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        print("8. Info service")
        print("9. Voice mailbox number")
        print("10. Service command editor")
        print("Enter choice: ")

sub_menu_choice = int(input())

match sub_menu_choice:

    case 1 :
        print("Write message (max 201 characters)")
    case 2:
        print("Inbox: Read received messages")
    case 3:
        print("Outbox: View saved messages")
    case 4:
        print("Picture messages: Send/receive picture messages")
    case 5:
        print("Templates: Use preset messages")
    case 6:
        print("Smileys: Edit smiley characters like :-)")
    case 7:
        print("Message settings: Set message centre number")
    case 8:
        print("Info service: Receive topic-based messages")
    case 9:
        print("Voice mailbox number: Store voice mail number")
    case 10:
        print("Service command editor: Send service requests")
    case _:
        print("Invalid option")

match user_menu_choice:

    case 3:

        print("\t ==== CHATS 💬 ==== \n")
        print("Start conversation using text messages")
        print("Enter phone number and nickname to begin")
        
match user_menu_choice:

    case 4:

        print("\t ==== CALL REGISTERS 📲 === \n")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("6. Show call costs")
        print("7. Call cost settings")
        print("8. Prepaid credit")
        print("Enter choice: ")

sub_menu_choice = int(input())

match sub_menu_choice:

    case 1:
        print("Missed calls: Last 10 unanswered calls")
    case 2:
        print("Received calls: Last 10 answered calls")
    case 3:
        print("Dialled numbers: Last 20 called numbers")
    case 4:
        print("Erase recent call lists")
    case 5:
        print("Show call duration: Last/All calls duration")
    case 6:
        print("Show call costs: Cost of calls")
    case 7:
        print("Call cost settings: Set cost limit")
    case 8:
        print("Prepaid credit: Check remaining credit")
    case 9:
        print("Voice mailbox number: Store voice mail number")
    case 10:
        print("Service command editor: Send service requests")
    case _:
        print("Invalid option")

match user_menu_choice:

    case 5:

        print("\t ==== TONES 🎶 ==== \n")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Composer")
        print("5. Message alert tone")
        print("6. Keypad tones")
        print("7. Warning and game tones")
        print("8. Vibrating alert")
        print("9. Screen saver")
        print("Enter choice: ") 
  
sub_menu_choice = int(input())

match sub_menu_choice:

    case 1:
        print("Ringing tone: Select ringtone")
    case 2:
        print("Ringing volume: Adjust volume")
    case 3:
        print("Incoming call alert: Set alert type")
    case 4:
        print("Composer: Create your own ringing tone")
    case 5:
        print("Message alert tone: Select message tone")
    case 6:
        print("Keypad tones: Turn keypad sounds on/off")
    case 7:
        print("Warning and game tones")
    case 8:
        print("Vibrating alert: Turn vibration on/off")
    case 9:
        print("Screen saver: Set screen saver")
    case _:
        print("Invalid option")






        
