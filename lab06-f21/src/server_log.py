# Use this script to solve the problem
# Start by writing comments for your initial design (and commit before coding)
# 1 How many unique IP addresses are there in data file?
# 2 How many unique subnets (first 3 numbers only in IP address) are there in data file?
# 3 How many unique web domain targets are there (at the example.net and example.com level)?
# 4 For each individual IP address (e.g. 137.155.0.225) what is the total number of bytes requested from each domain?
# 5 For each domain name, what is the total number of bytes requested from all IP addresses?
# 6 Which IP address requested the most total bytes from each domain name?

import os
import csv
from collections import Counter
import struct
import binascii


#opened file, placed all IP's into a list, Used Counter to count unique IP's.

def unique_ip(file_path):
    ip_address = []

    with open(file_path, 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            ip_address.append(str(line[1]))
        ip_amount = Counter(ip_address)
        for uni_count in range(0, len(ip_amount)-1):
            uni_count += 1

    return uni_count

def unique_sub(file_path):

    list2 = []
    sub_list = []
    sub_count = 0
    with open(file_path, 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            subnets = str(line[1])
            sub1 = subnets.split('.')
            list2.append(sub1[0])
        for val in list2[1:]:
            sub_list.append(val)
            sub_count += 1

    return sub_count

def unique_domain(file_path):
    uni_domain = []
    whole_string = ""
    raw_set = []
    whole_list = []
    char1 = []
    with open(file_path, 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            whole_string += line[2]
            uni_domain = whole_string.split('/')
        for url in uni_domain[1:]:
            whole_list.append(url[0])

        #for line in range(0, len(reader)-1):
            #whole_string = line[2]
            #full_str = str(line[2])
            #sub1 = full_str.split('/')
        #for domain in sub1[1:]:
            #uni_domain.append(domain[0][0])

    return whole_list




def domain_bytes(file_path):

    whole_string = []


    with open(file_path, 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            whole_string.append(line[2])
    return whole_string

'''def bytes_file(file_path):
    with open(file_path) as file:
        reader_data = csv.reader(file, delimiter=' ')
        bytes_list = []
        count = 0
        for bytes in reader_data:
            if count == 0:
                count = 1
                # print('i=0', date)
            else:
                other = bytes[1].split(',')
                # print('other', other)
                bytes_list.append(other[3])
    return bytes_list

    #compare ips, subnets, and web domains

def compare_ips():
    list_ips = ip_file(file_path)
    repeats = []
    list_no_repeats_ip = []
    count_ip = 0
    count_ip_no_repeats = 0
    count_repeats = 0
    for ip in list_ips:
        count_ip += 1
        # print(ip)
        if ip not in list_no_repeats_ip:
            list_no_repeats_ip.append(ip)
            count_ip_no_repeats +=1
        else:
            repeats.append(ip)
            count_repeats += 1
    # print('ip', count_ip)
    # print('no repeats', count_ip_no_repeats)
    # print('repeats', count_repeats)
    return count_ip_no_repeats


def compare_subnets():
    list_ips = ip_file(file_path)
    repeats = []
    list_no_repeats_sub = []
    count_sub_no_repeats = 0
    count_repeats = 0
    for ip in list_ips:
        print(ip)
        if ip[0:9] not in list_no_repeats_sub:
            list_no_repeats_sub.append(ip[0:9])
            count_sub_no_repeats += 1
        else:
            repeats.append(ip[0:9])
            count_repeats += 1

    # print(list_no_repeats_sub)
    # print('count no', count_sub_no_repeats)
    # print('repeats', count_repeats)
    return count_sub_no_repeats



def compare_web_domains():
    list_web = web_file(file_path)
    list_web_no_extra = []
    list_web_no_repeats = []
    repeats = []
    count_no_repeats = 0
    count_repeats = 0
    for website in list_web:
        website = website.split('//')[1]
        website = website.split('/')[0]
        website = website.split('.')
        if len(website) == 2:
            website = website[0] + '.' + website[1]
            list_web_no_extra.append(website)
        else:
            website = website[1] + '.' + website[2]
            list_web_no_extra.append(website)
    for no_extra_web in list_web_no_extra:
        if no_extra_web not in list_web_no_repeats:
            list_web_no_repeats.append(no_extra_web)
            count_no_repeats +=1
        else:
            repeats.append(no_extra_web)
            count_repeats += 1
    # print(count_no_repeats)
    return count_no_repeats


    #take compared ips and check how many bytes from each

def total_bytes_domain(file_path):
    ip_list = ip_file(file_path)
    bytes_list = bytes_file(file_path)
    list_web = web_file(file_path)
    list_web_no_extra = []
    list_web_no_repeats = []
    repeats = []
    for website in list_web:
        website = website.split('//')[1]
        website = website.split('/')[0]
        website = website.split('.')
        if len(website) == 2:
            website = website[0] + '.' + website[1]
            list_web_no_extra.append(website)
        else:
            website = website[1] + '.' + website[2]
            list_web_no_extra.append(website)
    for no_extra_web in list_web_no_extra:
        if no_extra_web not in list_web_no_repeats:
            list_web_no_repeats.append(no_extra_web)
        else:
            repeats.append(no_extra_web)
    print(list_web_no_repeats)

    list_ips = ip_file(file_path)
    list_no_repeats_ip = []
    count_ip = 0
    for ip in list_ips:
        count_ip += 1
        # print(ip)
        if ip not in list_no_repeats_ip:
            list_no_repeats_ip.append(ip)

    dictionary_ip_bytes ={}
    dictionary_ip_web = {}
    i= 0
    for ip in ip_list:
        dictionary_ip_bytes[ip] = bytes_list[i]
        dictionary_ip_web[ip] = list_web_no_extra[i]
        i += 1
    print('ip_bytes',dictionary_ip_bytes)
    print("ip_web",dictionary_ip_web)
    # bytes_for_domain = 0
    # bytes_for_ip = []
    # for ip in list_no_repeats_ip:
    #     if list_web_no_extra[0] == dictionary_ip_web[ip]:
    #         print('web', dictionary_ip_bytes[ip])
    #     print('ip_web dict',dictionary_ip_web[ip])
    #     print('ip_bytes dict', dictionary_ip_bytes[ip])

    #take compare ip output dictionary'''


if __name__=='__main__':
    file_path = os.path.join("data", "csdata_base_V1_08312021_0736am.csv")
    print("Unique IP addresses in the data file:", unique_ip(file_path))
    print("Unique subnets in the data file:", unique_sub(file_path))
    #print("Unique domains in data file:", unique_domain(file_path))
    print(domain_bytes(file_path))
    #print(compare_ips())
    #print(compare_subnets())
    #print(compare_web_domains())
    #print(total_bytes_domain(file_path))
