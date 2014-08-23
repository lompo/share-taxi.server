import json
import webapp2
import cgi
import urllib
import urllib2
import jinja2
import os
import sys
import string
import traceback
import time
import logging
import datetime

from model_cabs_memory import *

class Test2Handler(webapp2.RequestHandler):

    def get(self):
 
        latlngs5 = [['32.076623', '34.774563'],['32.076814', '34.774509'],
                    ['32.076960', '34.774488'],['32.077105', '34.774434'],
                    ['32.077241', '34.774402'],['32.077405', '34.774370'],
                    ['32.077569', '34.774273'],['32.077832', '34.774231'],
                    ['32.078023', '34.774188'],['32.078014', '34.774198'],
                    ['32.078105', '34.774145'],['32.078260', '34.774102'],
                    ['32.078432', '34.774113'],['32.078680', '34.773984'],
                    ['32.078898', '34.774016'],['32.079089', '34.773941'],
                    ['32.079289', '34.773866'],['32.079580', '34.773909'],
                    ['32.079807', '34.773888'],['32.080016', '34.773888'],
                    ['32.080307', '34.773845'],['32.080534', '34.773834'],
                    ['32.080798', '34.773823'],['32.081043', '34.773845'],
                    ['32.081225', '34.773834'],['32.081461', '34.773802'],
                    ['32.081761', '34.773823'],['32.082052', '34.773845'],
                    ['32.082361', '34.773898'],['32.082661', '34.773931'],
                    ['32.082898', '34.773974'],['32.083270', '34.774027'],
                    ['32.083580', '34.774102'],['32.083907', '34.774210'],
                    ['32.084125', '34.774242'],['32.084516', '34.774328'],
                    ['32.084816', '34.774413'],['32.085107', '34.774478'],
                    ['32.085407', '34.774564'],['32.085716', '34.774639'],
                    ['32.085970', '34.774703'],['32.086325', '34.774778'],
                    ['32.086616', '34.774875'],['32.086888', '34.774939'],
                    ['32.087206', '34.775025'],['32.087488', '34.775089']]
#                    ['32.087888', '34.775186'],['32.088325', '34.775304']]

        latlngs4 = [['32.074135', '34.768137'],['32.074507', '34.768094'],
                    ['32.074944', '34.768083'],['32.075217', '34.768029'],
                    ['32.075526', '34.768051'],['32.075880', '34.768051'],
                    ['32.076162', '34.768083'],['32.076543', '34.768191'],
                    ['32.076907', '34.768266'],['32.077334', '34.768352'],
                    ['32.077634', '34.768405'],['32.077871', '34.768545'],
                    ['32.078134', '34.768673'],['32.078452', '34.768845'],
                    ['32.078825', '34.769070'],['32.079189', '34.769253'],
                    ['32.079452', '34.769457'],['32.079771', '34.769661'],
                    ['32.080137', '34.769924'],['32.080455', '34.770160'],
                    ['32.080810', '34.770353'],['32.081182', '34.770568'],
                    ['32.081628', '34.770750'],['32.081982', '34.770954'],
                    ['32.082246', '34.771050'],['32.082673', '34.771276'],
                    ['32.083073', '34.771490'],['32.083491', '34.771673'],
                    ['32.083864', '34.771941'],['32.084318', '34.772134'],
                    ['32.084673', '34.772295'],['32.085046', '34.772467'],
                    ['32.085455', '34.772617'],['32.085937', '34.772756'],
                    ['32.086300', '34.772885'],['32.086664', '34.772982'],
                    ['32.087227', '34.773132'],['32.087673', '34.773271'],
                    ['32.088154', '34.773389'],['32.088591', '34.773539'],
                    ['32.088963', '34.773679'],['32.089372', '34.773797'],
                    ['32.089700', '34.773894'],['32.090063', '34.774012'],
                    ['32.090500', '34.774119'],['32.090845', '34.774237']]
#                    ['32.091236', '34.774333'],['32.091490', '34.774398']]

        cab1_not_in_array = True
        cab2_not_in_array = True
        cab3_not_in_array = True
        cab4_not_in_array = True
        curr_date = datetime.datetime.now()

        for cab in cabs_memory_array:
            
            if (cab.androidID == '1234'):
                cab1_not_in_array = False
                temp1 = cab
                print('cab1 exists')
                if (temp1.date < curr_date):
                    temp1.update_cab(curr_date, '34.774563', '32.076623')

            if (cab.androidID == '4567'):
                cab2_not_in_array = False
                temp2 = cab
                print('cab2 exists')
                if (temp2.date < curr_date):
                    temp2.update_cab(curr_date, '34.775089', '32.087488')

            if (cab.androidID == '0000'):
                cab3_not_in_array = False
                temp3 = cab
                print('cab3 exists')
                if (temp3.date < curr_date):
                    temp3.update_cab(curr_date, '34.768137','32.074135')

            if (cab.androidID == '1111'):
                cab4_not_in_array = False
                temp4 = cab
                print('cab4 exists')
                if (temp4.date < curr_date):
                    temp4.update_cab(curr_date, '34.774237', '32.090845')

        if (cab1_not_in_array):
            temp1 = cabObject('1234',curr_date,'5','34.774563', '32.076623')
            cabs_memory_array.append(temp1)
            print('new cab1 added')

        if (cab2_not_in_array):
            temp2 = cabObject('4567',curr_date,'5','34.775089', '32.087488')
            cabs_memory_array.append(temp2)
            print('new cab2 added')

        if (cab3_not_in_array):
            temp3 = cabObject('0000',curr_date,'4','34.768137','32.074135')
            cabs_memory_array.append(temp3)
            print('new cab3 added')

        if (cab4_not_in_array):
            temp4 = cabObject('1111',curr_date,'4','34.774237', '32.090845')
            cabs_memory_array.append(temp4)
            print('new cab4 added')

        l = len(latlngs5)

        for i in range(l):
            curr_date = datetime.datetime.now()
            temp1.update_cab(curr_date, latlngs5[i][1],latlngs5[i][0])
            temp2.update_cab(curr_date, latlngs5[l-1-i][1],latlngs5[l-1-i][0])
            temp3.update_cab(curr_date, latlngs4[i][1],latlngs4[i][0])
            temp4.update_cab(curr_date, latlngs4[l-1-i][1],latlngs4[l-1-i][0])
            print('update',i)
            # update free-seats:
            temp1.update_freeSeats(i%2)
            temp2.update_freeSeats(i%3)
            temp3.update_freeSeats((i+1)%2)
            temp4.update_freeSeats((i+1)%3)
            time.sleep(1) # delay 2 seconds

        # delete test cab
        for cab in cabs_memory_array:
          if (cab.androidID == '1234' or cab.androidID == '4567' or cab.androidID == '0000' or cab.androidID == '1111'):
            cabs_memory_array.remove(cab)