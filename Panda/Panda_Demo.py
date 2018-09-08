#!/usr/bin/env python 
# -*- coding: UTF-8 -*- 
#---------------------------------------
# Project Name: Panda 
# Version:      Demo 
# Date:         2018/9/7
# Author:       SongXiaochun 
# Contact:      xiaochunsong92@163.com 
#---------------------------------------
import xlrd 
import re 
A_data = 'A_data.xls'
B_data = 'B_data.xls'
S_data = 'S_data.xls'

def read_S_data(S_file):
    print('you are now reading S_data')
    S_dict = {}
    S_data_read = xlrd.open_workbook(S_file)
    S_sheet = S_data_read.sheet_by_index(0) 
    S_name = S_sheet.col_values(0) 
    S_value = S_sheet.col_values(1) 
    #print('S name is: ', S_name) 
    #print('S value is: ', S_value)
    for i in range(len(S_name)):
        S_dict[S_name[i]] = S_value[i] 
    print('S dict is:', S_dict)
    return S_dict

def read_B_data(B_file):
    print('you are now reading B_data')
    B_value_cal = []
    B_dict = {}
    B_name_list = []
    B_name_list_tol = []
    B_name_dict = {}
    B_data_read = xlrd.open_workbook(B_file)
    B_sheet = B_data_read.sheet_by_index(0)
    B_name = B_sheet.col_values(0)
    B_value = B_sheet.col_values(1) 
    #print('B name is: ', B_name)
    #print('B value is: ', B_value) 
    for i in range(len(B_value)):
        B_value_formula = B_value[i]
        B_value_re = re.match(r'(\w*?):(.*?)\s(\w*?):(.*)', B_value_formula) 
        if B_value_re:
            S_1_name = B_value_re.group(1)
            S_1_value = B_value_re.group(2)
            S_2_name = B_value_re.group(3)
            S_2_value = B_value_re.group(4)
            #print('S_dict value is ', S_dict[S_1_name])
            #print('S_1_value is ', S_1_value)
            B_name_list.append(S_1_name)
            B_name_list.append(S_2_name)
            #print('B_name_list is ', B_name_list)
            B_value_cal.append(S_dict[S_1_name]*float(S_1_value) + S_dict[S_2_name]*float(S_2_value)) 
        B_name_list_tol.append(B_name_list) 
        B_name_list = []
        #print('B_name_list_tol is: ', B_name_list_tol)
    #print('B value calculated: ', B_value_cal)  
    for i in range(len(B_name)):
        B_dict[B_name[i]] = B_value_cal[i]
        B_name_dict[B_name[i]] = B_name_list_tol[i]
    print('B_dict is: ', B_dict)
    print('B_name_dict is: ', B_name_dict) 
    return B_dict, B_name_dict

def read_A_data(A_file):
    print('you are now reading A_data')
    A_dict = {}
    A_value_cal = []
    A_name_list = []
    A_name_list_tol = []
    A_name_dict = {}
    A_data_read = xlrd.open_workbook(A_file)
    A_sheet = A_data_read.sheet_by_index(0)
    A_name = A_sheet.col_values(0)
    A_value = A_sheet.col_values(1) 
    #print('A name is: ', A_name)
    #print('A value is: ', A_value)
    for i in range(len(A_value)):
        A_value_formula = A_value[i]
        A_value_re = re.match(r'(\w*?):(.*?)\s(\w*?):(.*)', A_value_formula)
        A_value_re_1 = re.match(r'(\w*?):(.*)', A_value_formula)
        if A_value_re:
            B_or_S_1_name = A_value_re.group(1)
            #print('B_or_S_1_name is ', B_or_S_1_name)
            Is_B_1 = re.match(r'B\d', B_or_S_1_name)
            if Is_B_1:
                B_or_S_dict_value_1 = B_dict[B_or_S_1_name] 
            else:
                B_or_S_dict_value_1 = S_dict[B_or_S_1_name] 
            B_or_S_1_value = A_value_re.group(2)
            B_or_S_2_name = A_value_re.group(3)
            Is_B_2 = re.match(r'B\d', B_or_S_2_name)
            if Is_B_2:
                B_or_S_dict_value_2 = B_dict[B_or_S_2_name] 
            else:
                B_or_S_dict_value_2 = S_dict[B_or_S_2_name] 
            B_or_S_2_value = A_value_re.group(4)
            A_name_list.append(B_or_S_1_name)
            A_name_list.append(B_or_S_2_name)
            A_value_cal.append(B_or_S_dict_value_1*float(B_or_S_1_value) + B_or_S_dict_value_2*float(B_or_S_2_value)) 
        elif A_value_re_1:
            B_or_S_1_name = A_value_re_1.group(1)
            Is_B_1 = re.match(r'B\d', B_or_S_1_name)
            if Is_B_1:
                B_or_S_dict_value_1 = B_dict[B_or_S_1_name] 
            else:
                B_or_S_dict_value_1 = S_dict[B_or_S_1_name] 
            B_or_S_1_value = A_value_re_1.group(2) 
            A_name_list.append(B_or_S_1_name)
            A_value_cal.append(B_or_S_dict_value_1*float(B_or_S_1_value))
        A_name_list_tol.append(A_name_list)
        A_name_list = []
    #print('A_value_cal is ', A_value_cal)
    for i in range(len(A_name)):
        A_dict[A_name[i]] = A_value_cal[i] 
        A_name_dict[A_name[i]] = A_name_list_tol[i]
    print('A_dict is ', A_dict)
    #print('A_name_dict is ', A_dict)
    return A_dict, A_name_dict 

def select_S_to_show():
    S_choosed = input("Please choose a Stock you intersted:")
    Related_B = []
    Related_A = []
    #print('S_choosed is ', S_choosed)
    print('-------------------------')
    print('Selected Stock is %s Value is %s' %(S_choosed, S_dict[S_choosed]))
    print('-------------------------')
    for key,value in B_name_dict.items():
        if S_choosed in value: 
            #print('B key is ', key)
            Related_B.append(key)
            print('Related Fund B are: %s Value is %s ' %(key, B_dict[key])) 
    print('-------------------------')
    for key,value in A_name_dict.items():
        if S_choosed in value: 
            Related_A.append(key) 
            #print('Related Fund A are: %s Value is %s ' %(key, A_dict[key])) 
        for i in range(len(Related_B)): 
            if Related_B[i] in value: 
                Related_A.append(key) 
                #print('Related Fund A are: %s Value is %s ' %(key, A_dict[key])) 
    Related_A = list(set(Related_A))
    for i in range(len(Related_A)):
        print('Related Fund A are: %s Value is %s ' %(Related_A[i], A_dict[Related_A[i]])) 

    return 

if __name__=='__main__':
    print('-------------------------')
    print('Panda Demo Version')
    print('-------------------------')
    print('you are now in main function')
    S_dict = read_S_data(S_data) 
    B_dict, B_name_dict = read_B_data(B_data)
    A_dict, A_name_dict = read_A_data(A_data)
    print('-------------------------')
    select_S_to_show() 
