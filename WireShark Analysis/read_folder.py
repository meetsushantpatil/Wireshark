'''
Created on Sep 23, 2016

@author: Sushant
'''

import os

def get_excel_file_names(location_dir_path):
    file_list = [];
    for file_name in os.listdir(location_dir_path):
        if file_name.endswith(".xlsx"):
            file_list.append(file_name);
    return file_list;

def get_folder_names(base_dir_path):
    folder_list = [];
    for folder_name in os.listdir(base_dir_path):
        if(folder_name != '.DS_Store'):
            folder_list.append(folder_name);
    return folder_list;

def get_all_excel_files_path(base_dir_path):
    all_paths = []
    folder_list = get_folder_names(base_dir_path);
    for folder in folder_list:
        file_list = get_excel_file_names(base_dir_path + '/'+ folder);
        for file_name in file_list:
            all_paths.append(base_dir_path + '/'+ folder + '/'+file_name);
    return all_paths;