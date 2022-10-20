import pandas as pd
import colorama
from colorama import Fore, Back, Style
import time

pd.set_option('display.max_columns', 1000, 'display.max_colwidth', 1000, 'display.max_rows',1000)

#importing profiles data base

sheet_name="Profiles"

profiles_df=pd.read_excel("costs_of_living.xlsx",sheet_name=sheet_name)
profiles_df.set_index("param",inplace=True)

#importing questions data base

sheet_name="Question"

questions_df=pd.read_excel("costs_of_living.xlsx",sheet_name=sheet_name)


#importing quantities data base

sheet_name="Quantities"

qtts_df=pd.read_excel("costs_of_living.xlsx",sheet_name=sheet_name)

## import housing dataframes

cities_list=["Lisbon","Barcelona"]

lx_houses=pd.read_csv("lx_houses_complete.csv")
bcn_houses=pd.read_csv("bcn_houses_complete.csv")

dict_city={"lisbon":lx_houses,"barcelona":bcn_houses}

### STARTING THE JOURNEY

budget = 0

print("\nWELCOME to our budget generator! \n\nExciting times ahead!! If you're here is because you're feeling your feet itchy and want to go abroad, are we right?! \n\nWe're here to help you make the best decision and give you an honest answer of how much you are expected to spend per month based on your profile. \nBut first we need to ask you a few questions.\n")
time.sleep(2)
name = input(Fore.GREEN + "What's your name? " + Fore.RESET)

print(f"Great to have you here, \033[1m{name}\033[0m!\n")
time.sleep(1)

input(Fore.GREEN + "What's your age? " + Fore.RESET)
time.sleep(1)
print(Fore.RESET + "\nThank you!\n")
time.sleep(1)
answer= input( Fore.GREEN + "What's the gender you indentify with? \033[1mF/M/Other\033[0m ")

if answer.upper() != "F" and answer.upper() != "M" and answer.upper() != "OTHER":
        answer=input("Sorry, I couldn't understand that. \nWhat's the gender you indentify with? \033[1mF/M/Other\033[0m ")
else: 
    pass
time.sleep(1)
print(f"Thank you, \033[1m{name}\033[0m! \n")
time.sleep(1)

## DEFINE CITY OF CHOICE

print("Now, from our city database, which we are continuously working to expand, which city would you like us to generate your monthly living budget to? \nCurrently our cities are: Lisbon or Barcelona.\n" )
answer=input(Fore.GREEN + "What's your choice? \033[1mLX\033[0m" + Fore.GREEN + " or \033[1mBCN\033[0m ")

if answer.upper()!= "LX" and answer.upper()!= "BCN":
    answer=input("Sorry, I couldn't understand that. \nWhat's your choice? \033[1mLX\033[0mL or \033[1mBCN\033[0m?")
else: 
    pass

if answer.upper()=="LX":
    city="Lisbon"
elif answer.upper()=="BCN":
    city="Barcelona"

print(f"Thank you, \033[1m{name}\033[0m!\n")
time.sleep(1)


## defining cities identifiers (for houses databases)

if city== "Lisbon":
    city_short="lx"
elif city=="Barcelona":
    city_short="bcn"

    #DEFINE THE PERSON'S PROFILE

print("\nGREAT!! " + city + ", here we go!\nNow, we need to know a bit more about you so we can give you the most personalised budget possible.\n" )

time.sleep(1)

print("What type of person are you? Are we talking to a party animal, foodie and restaurant top explorer or the chilled friend of the group that prefers to stay home? \n" + Fore.GREEN + "\nWould you say you like going out for drinks and dinner much? How much?")
time.sleep(3)

print(Fore.BLUE + "\nHmmm the normal amount I guess? \033[1m(A)\033[0m \n" + Fore.BLUE + "I can eat in and chill at home but I also love to explore a lot of the restaurantes and bars of the city! \033[1m(B)\033[0m \n" + Fore.BLUE + "C'mon, I'm moving to a new city, plus I'm not the best cook, I want to explore most of the bars and restaurants I can!! \033[1m(C)\033[0m")
answer=input("")

time.sleep(1)

if answer.upper()!= "A" and answer.upper()!= "B" and answer.upper()!= "C":
    answer=input("Hmmm the normal amount I guess? (\033[1mA\033[0m) \nI can eat in and chill at home but I also love to explore a lot of the restaurantes and bars of the city! (\033[1mB\033[0m) \nC'mon, I'm moving to a new city, plus I'm not the best cook, I want to explore most of the bars and restaurants I can!! (\033[1mC\033[0m)")
else: 
    pass

#answer = Profiles

if answer.upper()=="A":
    Profiles="Basic"
elif answer.upper()=="B":
    Profiles="Mid"
elif answer.upper()=="C":
    Profiles="Upper"

## UPDATING THE BUDGET BASED ON THE PROFILE
budget=0
budget= budget + profiles_df.loc[city,Profiles]

## sportif person??

#time.sleep(3)
print("\nThank you! That's great.\n")
time.sleep(1)

answer= input("\nNow, are you an active person?" + Fore.GREEN + " Are you planning on enrolling in a gym or paid sport activity? \033[1m(Y/N)\033[0m ")

time.sleep(1)

if answer.upper()!= "Y" and answer.upper()!= "N":
    answer=input("Sorry, I couldn't understand that. \n"+ Fore.GREEN + "Are you planning enrolling in a gym or paid sport activity? \033[1m(Y/N)\033[0m ")
else: 
    pass

if answer=="Y":
    budget= budget + questions_df.loc[0, city]
elif answer=="N":
    pass

### CULTURAL HABITS

print("\nThank you! We're nearly there!")
time.sleep(1)

print("\nNow, on your cultural habits... Do you like going to the cinema, theathers, museums,etc?\n")
answer= input(Fore.GREEN + "How many times would you say you go on a paid cultural activity per month? " + Fore.RESET)

if answer.isalnum():
    pass
else:
    answer=input("Sorry, I couldn't understand that. \n" + Fore.GREEN + "How many times would you say you go on a paid cultural activity per month?")

activity="Cinema, International Release, 1 Seat"

activity_index=1

activity_costs=qtts_df.loc[activity_index, city]

activity_costs=int(activity_costs)

budget=budget+activity_costs

## SMOKER

print("\nOne more question about your consumption habits...\n")
time.sleep(1)

answer= input(Fore.GREEN + "Are you a smoker? \033[1m(Y/N)\033[0m ")

time.sleep(1)

if answer.upper()!= "Y" and answer.upper()!= "N":
    answer=input("Sorry, I couldn't understand that. \n" + Fore.GREEN + "Are you a smoker? \033[1m(Y/N)\033[0m ")
else: 
    pass

## UPDATE BUDGET WITH CIGARETTES COUNT CIGARRETES


if answer.upper()=="N":
    cigarrete_cost=0
    pass

elif answer.upper()=="Y":
    sub_answer= input("OK, no judgment here. " + Fore.GREEN + "How many cigarettes would you say you smoke per day? " + Fore.RESET)

    if sub_answer.isalnum():
        cigarette_index=0

        cigarrete_cost=qtts_df.loc[cigarette_index, city]
    else:
        answer=input("Sorry, I couldn't understand that. \n" + Fore.GREEN + "How many cigarates would you say you smoke per day?")



## HOUSING CHOICE

print("\nGREAT! We're nearly there. Now you just need to tell us about your accomodation preferences.\n\n"+ Fore.GREEN + "Would you prefer to live:")
time.sleep(1)

answer= input(Fore.BLUE + "\nIn a room in a shared house \033[1m(A)\033[0m" + Fore.BLUE +"\nOn your own.\033[1m(B)\033[0m \n")

if answer.upper()!= "A" and answer.upper()!= "B":
    answer=input("Sorry, I couldn't understand that. \n"+ Fore.GREEN + "What do you prefer? \n Room in a house share \033[1m(A)\033[0m(R) \n Live on your own.\033[1m(B)\033[0m ")
else: 
    pass
time.sleep(1)


## RETRIEVEING THE LIST OF HOUSING OPTIONS

if answer.upper()=="A":
    acomm_type="Bedroom"
elif answer.upper()=="B":
    acomm_type="Place"


houses_df_in_use=dict_city[city.lower()]

houses_df_in_use["replaced_type"]=houses_df_in_use.apply(lambda row: row["typology"].replace("Entire ",""),axis=1)
houses_df_in_use

houses_df_in_use["Name"]=houses_df_in_use["replaced_type"] + " " + houses_df_in_use["Unnamed: 0"].astype(str)


houses_df_in_use=houses_df_in_use[houses_df_in_use["replaced_type"]==acomm_type]

houses_df_in_use= houses_df_in_use[["Name","cost_month","neighbourhood","distance","duration","url"]]

#houses_df_in_use.loc[1,"url"]

url_df=houses_df_in_use["url"].to_frame()


def make_clickable(val):
    return '<a href="{}">{}</a>'.format(val,val)

houses_to_display=houses_df_in_use.style.format({"url": make_clickable})

## USER TO CHOOSE SPECIFIC ACCOMOTADION

print("\nPerfect! Let's look at the options we have here for you!\n")
time.sleep(1)

#print(houses_to_display)
print(houses_df_in_use)


answer= input(Fore.GREEN +f"Please choose the place you would like to move in to ( {acomm_type}"+" + number)\n" + Fore.RESET)

time.sleep(1)

lst_accm=[i.lower() for i in list(houses_df_in_use["Name"])]

if answer.lower() not in lst_accm:
        answer=input("Sorry, I couldn't understand that. \n"+ Fore.GREEN +"Please choose the place you would like to move in to: \n")
else: 
    pass

#answer="Entire Place 0"
acc_index=houses_df_in_use.loc[houses_df_in_use["Name"]==answer.capitalize()].index[0]
accm_cost=houses_df_in_use.loc[acc_index,"cost_month"].replace("€","").replace(",","")



budget=int(budget+int(accm_cost))

print( Fore.RESET + "\nTHANK YOU! That was all. \n\nWe're now in position to give you an estimate of your cost of living in " + city + ". \n")
time.sleep(0.5)

print(f"\033[1m{name}\033[0m, based on your profile, taste and choices, you should expect to spend an average of \033[1m{budget}\033[0m € per month. \nYou can start packing now! \nHAVE FUN!")