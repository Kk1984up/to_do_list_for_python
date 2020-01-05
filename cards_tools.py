# -*-coding=utf-8-*-
"""
created on 4,1,2020
anthor=libo
"""

card_list = []


def show_menu():
    print("*" * 50)
    print("welcome cards management system V1.0")
    print("1.add new cards")
    print("2.show all cards")
    print("3.search cards")
    print("")
    print("0.exit the system")


def add_cards():
    print("-" * 50)
    print("add new cards:")
    name_str = input("please input your name:")
    wechat_str = input("please input your wechat number:")
    email_str = input("please input your email number:")
    phone_str = input("please input your phone number: ")
    card_dict = {"name": name_str,
                 "wechat": wechat_str,
                 "email": email_str,
                 "phone": phone_str}

    card_list.append(card_dict)
    print(card_list)
    print("save %s card successfully" % card_dict["name"])


def show_cards():
    print("-" * 50)
    print("show all cards")
    if len(card_list) == 0:
        print("list in empty,please add cards")
        return
    for str in ['Name', 'Wechat', 'Email', 'Phone']:
        print(str, end="\t\t")
    print("")
    print("=" * 50)
    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card['name'],
                                        card['wechat'],
                                        card['email'],
                                        card['phone']))


def search_cards():
    print("-" * 50)
    print("search cards")
    find_name = input("plaese input who do yu want search for card:")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("find the card")
            for str in ['Name', 'Wechat', 'Email', 'Phone']:
                print(str, end="\t\t")

                print("")

            print("=" * 20)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["wechat"],
                                            card_dict["email"],
                                            card_dict["phone"]))
            deal_card(card_dict)

            break
    else:
        print("there is not %s card" % find_name)


def deal_card(card_dict):
    print(card_dict)
    print("[4]:change,[5]:delect,[0]:exit")
    action_str = input("please input which action do you want:")
    if action_str == "4":
        card_dict["name"] = input_card_info(card_dict["name"], "please input name:")
        card_dict["wechat"] = input_card_info(card_dict["wechat"], "please input wechat:")
        card_dict["email"] = input_card_info(card_dict["email"], "please input email:")
        card_dict["phone"] = input_card_info(card_dict["phone"], "please input phone:")

        print("change card successfully")

    elif action_str == "5":
        card_list.remove(card_dict)
        print("delect the card successfully")

    else:
        pass


def input_card_info(dict_value, tip_message):
    #input cards value
    """
    dict_value: the dict value
    tip_message: some tip about input message
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
