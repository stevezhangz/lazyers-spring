# Encode 'utf-8'
# Time 2021/3/20
# Author stevezhangz
# Please use this program in accordance with the "robots" agreement of the website which you wanna visit. If you do not comply
# with the relevant agreement, I will not be responsible for any problems.
import requests
import os
import json
def menu():
    print("----------------------------------------------------")
    print("****\t\t\t\t\tMenu                    ****")
    print("----------------------------------------------------")
    print("****\t\t\t\t\t 1.Input a word\t\t\t****")
    print("****\t\t\t\t\t 0.quit \t\t\t\t****")
    print("----------------------------------------------------")
def print_json(data):
    for i in data:
        for j in i.items():
            print(j[0],":",j[1])
def translation():
    kw = input("Input:")
    param = {
        'kw': kw
    }
    response = requests.post(url=post_url, data=param, headers=headers)
    ajax_json = response.json()
    print("********************************************")
    print("Response:")
    print_json(ajax_json['data'])
    print("********************************************")

def choice():
    while(1):
        ch = input("Input or just quit 1 or 0:")
        if int(ch)==1 or int(ch)==0:
            break
    if int(ch)==1:
        translation()
    else:
        print("Good bye")
        return 1

if __name__=="__main__":
    print("\n")
    print("warning:")
    print("Please use this program in accordance with the robots agreement of the website in this program. "
          "If you do not comply with the relevant agreement, I will not be responsible for any problems.")
    if os.path.exists("web_info.text"):
        with open("web_info.text", "r") as fp:
            info=eval(fp.readline())
            post_url=info["post_url"]
            headers=info["headers"]
            fp.close()
    else:
        post_url=input("post url:")
        headers = input("header:")
    with open("web_info.text","w") as fp:
        fp.write(json.dumps({"post_url":post_url,"headers":headers}))
    headers={'User-Agent':headers}
    while (1):
        menu()
        end = choice()
        if end:
            break

