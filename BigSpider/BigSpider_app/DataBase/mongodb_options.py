#! /usr/bin/env python
# coding=utf-8

from pymongo import *
import bson

client = MongoClient('127.0.0.1', 27017)


# 连接网页系统数据库
def mongodb_init_spider_ms():

    db = client.spider_ms

    if not client:
        print '[INFO]: MongoDB can not be connected, please check !'
    else:
        print '[INFO]: MongoDB is connected !'
    return db


# 连接爬虫系统数据库
def mongodb_init_uestc():

    client=MongoClient('127.0.0.1', 27017)
    uestc = client.zzh_data

    if not client:
        print '[INFO]: MongoDB can not be connected, please check !'
    else:
        print '[INFO]: MongoDB is connected !'
    return uestc


# 系统运行数据
def insert_user(db, userid, username, password, email, phone_num):
    db.users.insert({'userid': userid, 'username': username, 'password': password, 'email': email, 'phone_num': phone_num, 'remark':''})


def find_user_by_username(db, username):
    user = db.users.find_one({'username': username})    
    return user


def find_user_by_username_password(db, username, password):
    user = db.users.find_one({'username': username, 'password': password})   
    return user


# 管理员账户在mongodb中手动添加find_admin_by_name_psd
def find_admin_by_name_psd(db, admin_name, admin_psd):
    admin = db.admin.find_one({'admin_name': admin_name, 'admin_psd': admin_psd})
    return admin


def admin_find_all_users(db):
    users = db.users.find()
    return users


def admin_delete_user(db, userid):
    db.users.remove({'userid': userid})


def admin_update_user(db, userid, username, email, phone_num, remark):
    db.users.update({'userid': userid},{
        '$set':{'username': username,'email': email,'phone_num': phone_num,'remark':  remark}})


# db.commoditys.update({'c_id': uid}, {
#     '$set': {'c_name': c_name, 'c_price': c_price, 'c_description': c_description, 'c_postage': c_postage,
#              'c_num': c_num, 'class_name': class_name, 'c_brand': c_brand, 'class_style': class_style,
#              'hotpoint': hotpoint, 'albums': albums, 'specs': specs}})


def admin_find_one_user_byuserid(db, userid):
    user = db.users.find_one({'userid': userid})
    return user


def admin_find_all(db):
    admin_list = db.admin.find()
    return admin_list


# 爬虫数据
# 成功抓取数
def crawling_succeed_num(uestc):
    crawling_succeed_num = uestc.news.find().count()
    return crawling_succeed_num


# 爬取的网页信息
def crawling_web_info(uestc):
    crawling_web_info = uestc.news.find()
    return crawling_web_info