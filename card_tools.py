card_list = []


def show_menu():
    """显示菜单"""

    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0 ")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)

    # 1.提示输入详细信息
    name_str = input("输入姓名：")
    phone_str = input("输入电话：")
    qq_str = input("输入qq：")
    email_str = input("输入email：")
    # 2.使用输入信息建立一个字典
    card_dict = {"name": name_str,
                 "qq": qq_str,
                 "phone": phone_str,
                 "email": email_str}
    # 3.将字典存入card_list中
    card_list.append(card_dict)
    # 4.提示新增成功
    print("添加 %s的名片成功" % name_str)


def show_all():
    """显示所有"""
    print("-" * 50)

    # 如果没有记录，要提示
    if len(card_list) == 0:
        print("没有数据")

        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")

    # 打印分割线
    print("=" * 50)

    # 遍历列表依次输出
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))


def search_card():
    """查找名片"""
    print("-" * 50)
    print("查找名片")

    # 提示用户输入要查找的姓名

    find_name = input("请输入要查找的人：")

    # 遍历字典查找相关数据，如果没有，要提示

    for card_dict in card_list:

        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))

            # 添加修改与删除
            deal_card(card_dict)

            break
    else:
        print("没找到")


def deal_card(find_dict):

    action_str = input("请输入要执行的操作 "
                       "【1】 修改 【2】删除 【0】返回主菜单")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "姓名：【回车不修改】")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：【回车不修改】")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：【回车不修改】")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：【回车不修改】")

        print("修改成功")

    elif action_str == "2":

        card_list.remove(find_dict)

        print("成功删除名片")


def input_card_info(dice_value, tip_message):
    """输入名片信息

    :param dice_value: 字典中原有信息
    :param tip_message: 输入的文字
    :return: 如果输入了内容就更改，如果没输入就返回原来信息
    """
    # 提示输入内容
    result_str = input(tip_message)
    # 针对输入的内容进行判断，如果输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 如果没输入内容，返回字典的原有值
    else:
        return dice_value
