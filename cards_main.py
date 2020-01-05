#!/home/libo/anaconda3/bin/python3
#-*-coding=utf-8-*-
"""
created on 4,1,2020
anthor=libo
"""
import cards_tools

while True:
    cards_tools.show_menu()
    action = input("please input your choice:")
    print("Your choice is [%s]"%action)
#TODO tool meun function

    if  action in ['1','2','3']:
        if action == "1":
            cards_tools.add_cards()
        elif action == "2":
            cards_tools.show_cards()
        else:
            cards_tools.search_cards()

    elif  action =="0":
        break
    else:
        print("input error,please input your choice again")





