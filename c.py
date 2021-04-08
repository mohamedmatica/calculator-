##### importing rand
from random import randint 
print(" \033[1;33min anny place you can use clear to clear screen by inputing clear, but if you should enter numbers enter 0")
from time import sleep
from math import sqrt
### os
import os
###### functions#####
def sum ( a , b) :
	return a+b;
def mul ( a , b) :
	return a*b
def div ( a , b) :
	return a/b
def pow ( a , b) :
	return a**b
def rofdiv ( a , b) :
	return a%b
def sou(a,b):
	return a-b
def fact(a):
	return factorial(a)
def divmo(a,b):
	return a/b,a%b
def sqrti(a):
	return sqrt(a )

##### i used a loop for looping this things
###### hello what's your name ####
hello=str(input("\033[1;30m hello what's your name:  "))
if hello=="clear":
	os.system('clear')
	hello=str(input("\033[1;30m hello what's your name:  "))
print("hello ",hello.upper(),"we are glad by you using this script , i made the letters of your name capital for making you bigger")
time=int(input("\033[0;96m  please enter the hour that you are in , by by a condition , without minutes :  "))
if time==0:
	os.system('clear')
	time=int(input("\033[0;96m  please enter the hour that you are in , by by a condition , without minutes :  "))
if 3<time<13:
	print('''\033[1;93m 
	^v^  ^v^  ^v^  ^v^  ^v^  ^v^  ^v^  ^v^  ^v^  ^v^
┈┈┈┈┈╭̸╮̸┈┈┈┈┈╱▔▔▔╲
┈┈┈▕▔▔▔▔▔▏╱╲╱┈Good`  ▕
┈┈┈┏▏▉▕▊┓▔╲╱'Morning'╱
┈┈┈┗▏▅▅▕┛┈┈┈┈▔▔┈
┈╱▔▔▔▔▔▔▔▔╲┈     ▕  ▏┈
╱╱▔▏┏┳┳┓▕▔╲╲╱╱┈┈
╲╲▕┓┗▅▅┛┏▏┈╲╱┈┈┈

----------------
	''')
elif 19<time<23:
	print('''\033[1;93m 
	░╔╗╔╗╔╗╦╗░╦╗╗╦╔╗╗╔╔╦╗░*
░║╦║║║║║║░║║║║║╦╠╣░║░░⋮
░╚╝╚╝╚╝╩╝░╩╚╝╩╚╝╝╚░╩░░*
----------------

----------------
 ''')
elif 13<= time<=19:   
	print('''    \033[1;93m                 __                                                                            
                            /\ \                                                  __                       
    __       ___     ___    \_\ \                 __    __  __     __     ___    /\_\     ___       __     
  /'_ `\    / __`\  / __`\  /'_` \              /'__`\ /\ \/\ \  /'__`\ /' _ `\  \/\ \  /' _ `\   /'_ `\   
 /\ \L\ \  /\ \L\ \/\ \L\ \/\ \L\ \            /\  __/ \ \ \_/ |/\  __/ /\ \/\ \  \ \ \ /\ \/\ \ /\ \L\ \  
 \ \____ \ \ \____/\ \____/\ \___,_\           \ \____\ \ \___/ \ \____\\ \_\ \_\  \ \_\\ \_\ \_\\ \____ \ 
  \/___L\ \ \/___/  \/___/  \/__,_ /            \/____/  \/__/   \/____/ \/_/\/_/   \/_/ \/_/\/_/ \/___L\ \
    /\____/                                                                                         /\____/
    \_/__/                                                                                          \_/__/ 


	''')
y="y"
while y=="y":
	#### the function of program ###
	print('''   \033[47m      \033[1;30m 
	        _.--.._ ..----.. _..--.
        ,'      `'        `'  _  `.
       :   ,';               `.`.  :
       |  : /                  \ ) |
       :  `:    __        __    :  ;
        `-.|   (o_)  __  (o_)   |-'
           :        ___         ;
      __    \      (:::)       /    __
    ,'  `.   `.     `-'      ,'   ,'  `.
   :      `-._.`.. `---' _..'._.-'      :
   :      ) /     \`---''/     \'    ,  ;
    `._ .  /       `.   /       \  -'_.'
       :-,'          `.'         `.-:
       `'-._;           SSt    :_.-`'
           /                    \
         _:__                  __:_
       ,' _  `.              ,' _  `.
      / ,' `.  \            / ,' `.  \
     : :     :  :          : :     :  :
     | |     |  |::..____.:| |     |  |
     : :.    ;  ;          : :.    ;  ;
      \ `::.' ,'            \ `::.'  /
       `-...-'               `-....-'

----------------
hello i am jack and i am a bear , and i love math , so that i am  good at been a calculator 
----------------
  \033[1;92m  \033[40m  
	_            _       _
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
	''')
	##### the main page ########
	print("1) calculator\n2) play\n3 )exit\n4)find the solution of an equation(searching for the value of x) ")
	#### choosing something #######
	g=int(input("    choose:     "))
	######exiting####
	if g==0:
		os.system('clear')
		g=int(input("    choose:     "))
	if g==3:
		print('''\033[1;36m 
		_ _
  _____  _(_) |_
 / _ \ \/ / | __|
|  __/>  <| | |_
 \___/_/\_\_|\__|
		''')
		t=int(input(" \033[4;36m  thanks for using our app , don't forget us , rate us how many starts we deserve ?   "))
		if g==0:
			os.system('clear')
			t=int(input(" thanks for using our app , don't forget us , rate us how many starts we deserve ?   "))
		if t==0:
			print("you are so so so so evil , you hate us")
		elif t==1:
			print("you are so so evil")
		elif t==2:
			print("i am crying")
		elif t==3:
			print(" at least bigger than 2.5")
		elif t==4:
			print("great thank you very much ")
		elif t==5:
			print("thank you very  very much , you're the first one is gonna know our apps ")
		break
	##### execute calculator #######
	if g==1:
		print('''\033[0;92m 
		_            _ _
  ___ __ _| | ___ _   _| (_)_ __   __ _
 / __/ _` | |/ __| | | | | | '_ \ / _` |
| (_| (_| | | (__| |_| | | | | | | (_| |
 \___\__,_|_|\___|\__,_|_|_|_| |_|\__, |
                                  |___/
		''')
		### page of operations
		print("\033[1;36m   1)sum \n2 )mutiplication \n3) division \n4) power \n5) rest of division \n6 )soustraction\n7)factorial\n8)rest and result of division\n9)square root\n10)all numbers from 0 to (you choose) power 2")
		### choosing an operation ####
		h=int(input("  \033[1;32m choose:      "))
		if h==0:
			os.system('clear')
			h=int(input("  \033[1;32m  choose:      "))
		### the fact need only one num so i need conditions if fact is choosed by user 
		if h==7:
			a=float(input(" enter a num :    "))
			if a==0:
				os.system('clear')
				a=float(input(" enter a num :    "))
		elif h==9:
			a=float(input(" enter a num :    "))
			if a==0:
				os.system('clear')
				a=float(input(" enter a num :    "))
		elif h==10:
			pass
		else:
			a=float(input(" enter num 1:   "))
			b=float(input(" enter num 2:   "))
		#### working on the result #####
		res=0
		if h==1:
			res=sum(a,b)
		elif h==2:
			res=mul(a,b)
		elif h==3:
			res=div(a,b)
		elif h==4:
			res=pow(a,b)
		elif h==5:
			res=rofdiv(a,b)
		elif h==6:
			res=sou(a,b)
		elif h==7:
			res=fact(a)
		elif h==8:
			div,mod=divmo(a,b)
		elif h==9:
			res=sqrti(a)
		else :
			print("error , operation not found .....")
		if h==8:
			print("\033[1;33mdivsion:  ",div,",                      rest of division:  ",mod)
		elif h==10:
			num=int(input("from 0 to .... ?: "))
			list=[x**2 for x in range(num+1)]
			for b in list:
				print(b)
		else:
			print("\033[1;33mthe result is :",res)
		
		##### working on a game ########
	if g==4:
		print("\033[1;33mworking on")
	if g==2:
		print("\033[1;33mhello ",hello,'here i want to play with you ',''' \033[1;32m  
		                 dMP         dMP    .aMMMb   dMP dMP     dMMMMMP      dMMMMMMP     dMP dMP     dMP    .dMMMb 
                amr         dMP    dMP"dMP  dMP dMP     dMP             dMP       dMP dMP     amr    dMP" VP 
               dMP         dMP    dMP dMP  dMP dMP     dMMMP           dMP       dMMMMMP     dMP     VMMMb   
              dMP         dMP    dMP.aMP   YMvAP"     dMP             dMP       dMP dMP     dMP    dP .dMP   
             dMP         dMMMMMP VMMMP"     VP"      dMMMMMP         dMP       dMP dMP     dMP     VMMMP"    
                                                                                                             
                                       .aMMMMP     .aMMMb     dMMMMMMMMb     dMMMMMP 
                                      dMP"        dMP"dMP    dMP"dMP"dMP    dMP      
                                     dMP MMP"    dMMMMMP    dMP dMP dMP    dMMMP     
                                    dMP.dMP     dMP dMP    dMP dMP dMP    dMP        
                                    VMMMP"     dMP dMP    dMP dMP dMP    dMMMMMP     
                                                                                     

		''')
		print(''' 
	_   _ ___  ___   _   _  ___  _   _ _ __   _ __ ___ (_)_ __   __| |
	| | | / __|/ _ \ | | | |/ _ \| | | | '__| | '_ ` _ \| | '_ \ / _` |
	| |_| \__ \  __/ | |_| | (_) | |_| | |    | | | | | | | | | | (_| |
	\__,_|___/\___|  \__, |\___/ \__,_|_|    |_| |_| |_|_|_| |_|\__,_|
             	  |___/
		''')
		print("\033[1;35m  here is a game , that i think of a number between 0and 10  and you try to know what's this number for 3 times , if you didn't get it so you lost if true you win,")
		b=randint(0,10)
		d=2
		print("i think ")
		sleep(5)
		print("i got a num")
		while bool(5):
			e=int(input("think of the number that i think of :    "))
			if e==b:
				print("   \033[4;34m  you win , oh i am win the next time , i am weak this time , don't smile , i am gonna win the next time")
				break
			if e>b:
				print("   \033[4;34m  bigger")
			elif e<b:
				print("   \033[4;34m  lower")
			if d==0:
				print("   \033[4;34m  you lost , game over , i am stronger than you ")
				break
			d-=1
			#### wprking on exiting and rating####
	y=input("   \033[4;34m  do you want to do that more :??: y/n:   ")
	if y=='y':
		poi=str(input("   \033[4;34m  do you wanna clear screen ? y/n:  "))
		if poi=='y':
			os.system('   \033[4;34m  clear')
	if y=="n":
		t=int(input("       \033[0;37m  thanks for using our app , don't forget us , rate us how many starts we deserve ?   "))
		if t==0:
			print("   you are so so so so evil , you hate us")
		elif t==1:
			print("    you are so so evil")
		elif t==2:
			print("   i am crying")
		elif t==3:
			print("   at least bigger than 2.5")
		elif t==4:
			print("    great thank you very much ")
		elif t==5:
			print("    thank you very  very much , you're the first one is gonna know our apps ")
	
