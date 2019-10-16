from basic.practice.myCard import card_action

# 无限循环，由用户主动决定什么时候退出
while True:

    card_action.show_menu()

    action_str = input("请选择希望执行的操作: ")
    print("你选择的操作是 %s" % action_str)
    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            card_action.new_card()
        elif action_str == "2":
            card_action.show_all()
        elif action_str == "3":
            card_action.search_card()

    # 0退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】:")

        break
        # 如果在开发程序时，不希望立刻编写分支内部的代码
        # 可以使用pass关键字，表示一个占位符，能够保证程序的代码结构正确
        # 运行程序时，pass关键字不会执行任何操作
    else:
        print("输入错误，请重新输入:")
