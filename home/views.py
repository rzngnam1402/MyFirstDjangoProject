# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):  # Viết hàm xử lý response
    response = HttpResponse()
    response.writelines("<h1> Hello</h1>")
    response.write("This is my app!")
    return response  # trả vể response cho máy người dùng
