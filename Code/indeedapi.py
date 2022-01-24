# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:47:51 2022

@author: lenovo
"""

from indeed import IndeedClient

client = IndeedClient(publisher = "YOUR_PUBLISHER_NUMBER")

params = {
    'q' : "python",
    'l' : "United States",
    'userip' : "1.2.3.4",
    'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
}

search_response = client.search(**params)
job_response = client.jobs(jobkeys = ("5898e9d8f5c0593f", "c2c41f024581eae5"))
