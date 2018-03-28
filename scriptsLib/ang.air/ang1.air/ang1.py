# -*- encoding=utf-8 -*-

import os
import time


__author__ = r"叶新铭"
__title__ = r"阿牛哥功能测试"
__desc__ = """
1.0版本，未审核
"""
def wechatButtonFailed():
    snapshot(r"微信登录按钮显示超时")

connect_device("android:///")

clear_app("com.you9.klqp.ang1")
#stop_app("com.you9.klqp.ang1")

start_app("com.you9.klqp.ang1")



assert_exists(Template(r"tpl1522220935050.png", record_pos=(-0.006, 0.141), resolution=(2560, 1440)), "检查资源")

assert_exists(Template(r"tpl1522220524854.png", record_pos=(0.006, -0.101), resolution=(2560, 1440)), "阿牛哥logo")


try:
    assert_exists(Template(r"tpl1522220465886.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(-0.004, 0.14), resolution=(2560, 1440)), "显示更新进度")
    assert_not_exists(Template(r"tpl1522220830256.png", record_pos=(-0.001, 0.08), resolution=(2560, 1440)), "隐藏微信登陆按钮")
    
    assert_exists(Template(r"tpl1522220474659.png", record_pos=(0.002, 0.168), resolution=(2560, 1440)), "进度条")

    wait(Template(r"tpl1522220819444.png", record_pos=(-0.002, 0.081), resolution=(2560, 1440)),timeout = 600,interval = 2,intervalfunc = None)
    touch(Template(r"tpl1522229339044.png", record_pos=(0.004, 0.081), resolution=(2560, 1440)))

except:
    touch(Template(r"tpl1522229339044.png", record_pos=(0.004, 0.081), resolution=(2560, 1440)))

wait(Template(r"tpl1522232023099.png", record_pos=(-0.352, -0.004), resolution=(2560, 1440)))


touch(Template(r"tpl1522240492966.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.429, -0.232), resolution=(2560, 1440)))

touch(Template(r"tpl1522240534924.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(0.067, -0.066), resolution=(2560, 1440)))



stop_app("com.you9.klqp.ang1")

start_app("com.you9.klqp.ang1")










