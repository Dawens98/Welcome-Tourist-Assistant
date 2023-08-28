# Welcome to Haiti Script
# This Python script generates a personalized welcome message for visitors to Haiti.
# It collects information such as the visitor's name, duration of their visit, home country,
# and whether they need a translator. Based on this information, it generates a welcome
# message with relevant details. The script ensures a warm and informative welcome to Haiti.


#Create the visit country and language (s)
country = "Haiti"
languages = []
country_language = f"{'Creole'} and {'French'}"
#Create input questions for the user 
visitor_name = input("Please enter your full name: ")
visit_days = int(input("How many days will you be visiting the country?: "))
home_country = input("Where are you from?: ")
visitor_language = input("Which language (s) are you proficient in?: ")
ask_translator = input("Do you need a translator?: yes(Y) or no(N) ").lower()

 # Check if any of the entered languages are official languages in Haiti
if len(languages) == 1:
    language_description = languages[0]
    if language_description.lower() in ['creole', 'french']:
        message_language = f"{language_description} is one of the official languages spoken in Haiti."
    else:
        message_language = f"{language_description} is not an official language in Haiti."
else:
    official_languages = [lang for lang in languages if lang.lower() in ['creole', 'french']]
    if len(official_languages) > 0:
        language_description = ", ".join(official_languages)
        message_language = f"{language_description} is one of the official languages in Haiti."
    else:
        language_description = ", ".join(languages)
        message_language = f"{language_description} are not official languages in Haiti."


#Create welcome messages, with one of them displaying based on the user's information
message_welcome_inst1 = f"Welcome {visitor_name} to {country}! We are delighted to have you here for {visit_days} days. \
Before you arrive, it's important to note that {message_language} \
People here primarily speak languages such as {country_language}. However, to ensure our tourists have a special welcome, \
we have recently introduced AI software that can communicate in the local languages and provide translations for our visitors. \
As you mentioned needing a translator for your journey, we will gladly provide one for you. \
In conclusion, if you require assistance during your stay, please don't hesitate to contact us at this phone number: (+509) 00000000. \
We look forward to seeing you soon, as your return ticket to {home_country} is scheduled for {visit_days} days from now. We hope you have a pleasant stay."

message_welcome_inst2 = f"Welcome {visitor_name} to {country}! We are delighted to have you here for {visit_days} days. \
Before you arrive, it's important to note that {message_language} \
People here primarily speak languages such as {country_language}. However, to ensure our tourists have a special welcome, \
we have recently introduced AI software that can communicate in the local languages and provide translations for our visitors. \
Since you mentioned not needing a translator for your journey, we will not provide one for you. \
In conclusion, if you require assistance during your stay, please don't hesitate to contact us at this phone number: (+509) 00000000. \
We look forward to seeing you soon, as your return ticket to {home_country} is scheduled for {visit_days} days from now. We hope you have a pleasant stay."

#Control flow of ask_translator
if ask_translator == 'yes':
    print(message_welcome_inst1)
elif ask_translator == 'no':
    print(message_welcome_inst2)
else: 
    print("Invalid input. Please enter 'yes' or 'no'.")

