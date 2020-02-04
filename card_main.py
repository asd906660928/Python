#! /usr/bin/python3

import card_tools

# 无限循环
while True:

    # TODO 显示功能菜单
    card_tools.show_menu()

    action_str = input("请选择您要执行的操作：")
    print("您的选择是 %s" % action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            card_tools.new_card()

        # 显示全部
        elif action_str == "2":
            card_tools.show_all()

        # 查询名片
        elif action_str == "3":
            card_tools.search_card()

        # 如果在开发过程中，不希望马上编写分之内部代码，可以使用pass
        # pass表示一个占位符，能保证程序代码结构正确
        # 运行时，pass关键字不会执行任何操作
    # 0退出系统
    elif action_str == "0":
        break
    # 其他输入错误
    else:
        print("输入错误，请重新输入")
