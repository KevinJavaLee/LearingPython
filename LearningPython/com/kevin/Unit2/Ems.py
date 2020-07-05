"""
@File    : Ems.py
@Time    : 2020/7/5 11:16
@Author  : KevinXiao
@Software: PyCharm
"""

# 员工管理系统
"""
- 做命令行版本的员工管理系统
- 功能：
    四个：
        1.查询
            - 显示当前系统当中的所有员工
        2.添加
            - 将员工添加到当前系统中
        3.删除
            - 将员工从系统当中删除
        4.退出
            - 退出系统
- 员工信息要保存到哪里？ 列表，在系统中应该有一个列表，专门用来保存所有员工信息的 
"""

print("*"*20,"欢迎来到员工管理系统","*"*20)
emps = ["小匡\t28\t\t男\t\t非洲","大匡\t29\t\t男\t\t非洲"]
while True :

    # 打印

    print("1.查询员工")
    print("2.添加员工")
    print("3.删除员工")
    print("4.退出系统")
    choice_num = input("请输入你要执行的操作：")
    # 查询员工的信息
    if choice_num == '1':
        print("\t序号\t姓名\t年龄\t性别\t地址\t")
        n = 1
        for e in emps:
            print(f'\t\t{n}\t{e}')
            n += 1
        print("*"*50)
    elif choice_num == '2':
        # 输入员工的信息
        emp_name = input("请输入员工的姓名：")
        emp_age = input("请输入员工的年龄：")
        emp_sex = input("请输入员工的性别：")
        emp_address = input("请输入员工的地址：")
        # 拼接字符串
        emp_info = f'{emp_name}\t{emp_age}\t\t{emp_sex}\t\t{emp_address}'
        print("是否添加？")
        print("\t序号\t姓名\t年龄\t性别\t地址\t")
        print(f'\t\t1\t{emp_info}')
        print("*"*50)
        isFlag = input("请输入YES/NO：")
        # 判断用户的输入
        if isFlag.upper() == 'YES' or isFlag.upper() == 'Y':
            emps.append(emp_info)
            print("已成功添加！")
        else:
            print("添加失败！")
        print("*"*50)
    elif choice_num == '3':
        # 先遍历输出员工的信息
        print("\t序号\t姓名\t年龄\t性别\t地址\t")
        n = 1
        for e in emps:
            print(f'\t\t{n}\t{e}')
            n += 1
        # 得到用户想要删除的员工序号
        del_num = input("请输入你要删除的员工序号：")
        del_index = int(del_num) - 1
        # 判断用户输入的序号是否正确
        if 0 <= del_index < len(emps):
            print("是否删除该员工？")
            print("\t序号\t姓名\t年龄\t性别\t地址\t")
            print(f'\t\t{del_num}\t{emps[del_index]}')
            print("*"*50)
            print("请输入Yes/NO确认是否删除该员工？")
            isDel = input()
            if isDel.upper() == 'YES' or isDel.upper() == 'Y':
                # 根据用户删除该员工
                emps.pop(del_index)
                print("已经删除该用户！")
            else:
                print("已取消删除！")
            print("*"*50)
        else:
            print("你的输入有误，不存在此序号的员工！")
            print("*"*50)
    elif choice_num == '4':
        print("*"*20,"已退出系统","*"*20)
        break
    else:
        print("*"*20,"你的输出错误,请重新输入！","*"*15)


