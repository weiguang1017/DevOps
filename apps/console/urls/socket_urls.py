# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-28
# Author Yo
# Email YoLoveLife@outlook.com
from console import consumers
from django.conf.urls import url
console_routing = [
    url(r'console/', consumers.ConsoleConsumer),
]