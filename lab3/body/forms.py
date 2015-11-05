# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:57:27 2015

@author: asus-pc
"""
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label = '用户名',max_length = 100,error_messages = {'required':'请输入用户名'})    # max_length 数值
    password = forms.CharField(label = '密码',widget = forms.PasswordInput(),error_messages = {'required':'请输入密码'})