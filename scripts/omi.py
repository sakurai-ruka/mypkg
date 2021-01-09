#!/usr/bin/env python3

"""
BSD 3-Clause License
Copyright (c) 2020, Ruka Sakurai & Ryuichi Ueda.
All rights reserved.
"""

import rospy
import random
from std_msgs.msg import Int32 
from std_msgs.msg import String

rospy.init_node("omi")
pub = rospy.Publisher("kai",Int32,queue_size=1)
pub2 = rospy.Publisher("kai",Int32,queue_size=1)
pub3 = rospy.Publisher("kai",Int32,queue_size=1)
pub4 = rospy.Publisher("kai",Int32,queue_size=1) 
pub5 = rospy.Publisher("kai",Int32,queue_size=1)
pub6 = rospy.Publisher("kai",Int32,queue_size=1)
pub7 = rospy.Publisher("kai",Int32,queue_size=1)
pub8 = rospy.Publisher("kai",Int32,queue_size=1)
pub9 = rospy.Publisher("kai",Int32,queue_size=1)
rate =rospy.Rate(10)

a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8
j = 9
unsei = ['大大吉','大吉','向大吉','末大吉','吉凶未分末大吉','吉','中吉','小吉','後吉','末吉','吉凶不分末吉','吉凶相交末吉','吉凶相半','吉凶相央','小吉後吉','凶後吉','凶後大吉']

print('今年の運勢を占います')
rospy.sleep(2)
print('今年の運勢は........')
rospy.sleep(2)
u = random.choice(unsei)
print (u) 
rospy.sleep(2)

while True:
    print('今年の運勢の内容を占えます')
    a = input('占う場合は1を、終了する場合は２を押してください:')
    try:
        a = int(a)
    except ValueError:
        a = 0
    if int(a)==1:
        print('以下の内容を占えます')
        print('1:願事(ねがいごと)')
        print('2:待人(まちびと)')
        print('3:失物(うせもの)')
        print('4:旅行(りょこう)')
        print('5:商売(しょうばい)')
        print('6:学問(がくもん)')
        print('7:恋愛(れんあい)')
        print('8:健康(けんこう)')
        print('9:争事(あらそいごと)')
        while not rospy.is_shutdown():
            x = input('占いたい番号を押してください,終了する場合は0を押してください：')
            try:
                x = int(x)
            except ValueError:
                x = 0
            if int (x)==1:
                pub.publish(b)
                rate.sleep()
            elif int (x)==2:
                pub2.publish(c)
                rate.sleep()
            elif int (x)==3:
                pub3.publish(d)
                rate.sleep()
            elif int (x)==4:
                pub4.publish(e)
                rate.sleep()
            elif int (x)==5:
                pub5.publish(f)
                rate.sleep()
            elif int (x)==6:
                pub6.publish(g)
                rate.sleep()
            elif int (x)==7:
                pub7.publish(h)
                rate.sleep()
            elif int (x)==8:
                pub8.publish(i)
                rate.sleep()
            elif int (x)==9:
                pub9.publish(j)
                rate.sleep()
            elif int(x)==0:
                break
    elif int(a)==2:
        print('今年一年が良き一年となりますように')
        break
