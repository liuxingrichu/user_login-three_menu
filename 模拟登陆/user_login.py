#!/urs/bin/env python
# -*- coding:utf-8 -*-


lock_users = []
f0 = open("lock_users.db", encoding="utf-8")
for line in f0.readlines():
    line = line.strip()
    lock_users.append(line)
f0.close()


users_list = []
f1 = open("users.db", "r",  encoding="utf-8")
for line in f1.readlines():
    line = line.strip().split()
    users_list.append(line[0])
    users_list.append(line[1])
f1.close()


times = 3


for i in range(times):
    username = input("Enter your name:")
    password = input("Enter your password:")

    if username in lock_users:
        print("\tSorry, you're locked now. Please contact administrators.")
        break

    if username in users_list and password == users_list[users_list.index(username) + 1]:
        print("\tWelcome %s login !" % username)
        break
    else:
        print("\tusername or password is wrong.")

    if i == times-1:
        f2 = open("lock_users.db", "a+", encoding="utf-8")
        f2.write("\n")
        f2.write(username)
        f2.close()
        print("\t{}, you're locked!".format(username))