#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:08:51 2020

Combine pictures of models'temperature ,then make gif

@author: jmanning & Mingchao
"""
import os
import animating_models as am
from datetime import datetime,timedelta

#Hardcodes
area = 'NorthShore'#get different gbox
model_name = 'DOPPIO' # styles such as DOPPIO and GOMOFS
start_date='2020-02-16'
ndays=7
start_date_datetime=datetime(int(start_date[0:4]),int(start_date[5:7]),int(start_date[8:10]),0,0,0)
end_date_datetime=datetime(int(start_date[0:4]),int(start_date[5:7]),int(start_date[8:10]),0,0,0)+timedelta(days=ndays)
end_date=str(end_date_datetime.year)+'-'+str(end_date_datetime.month).zfill(2)+'-'+str(end_date_datetime.day).zfill(2)
realpath=os.path.dirname(os.path.abspath(__file__))
if model_name == 'DOPPIO':
    dpath=realpath[::-1].replace('py'[::-1],'result/Doppio'[::-1],1)[::-1]  # the directory of the result
elif model_name == 'GOMOFS':
    dpath=realpath[::-1].replace('py'[::-1],'result/Gomofs'[::-1],1)[::-1]
if not os.path.exists(dpath):
    os.makedirs(dpath)
dictionary=os.path.join(dpath,'dictionary_emolt.p')
gif_path=os.path.join(dpath,'gif')
map_save=os.path.join(dpath,'map')
gif_name = os.path.join(gif_path,start_date+area+'_'+model_name+'.gif')

#############################
 #run functions
am.seperate(filepathsave=dictionary)
#Get min/max temperature for color bar.Different models don't have same temperature range
Min_temp,Max_temp=am.temp_min_max(model_name,dt=start_date_datetime,interval=ndays,area=area)
#make images
am.make_images(model_name,dpath=dictionary,path=map_save,dt=start_date_datetime,interval=ndays,Min_temp=Min_temp,Max_temp=Max_temp,area=area)
#using images to make gif
am.make_gif(gif_name,map_save,start_time=start_date,end_time=end_date)
