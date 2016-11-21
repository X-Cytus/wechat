# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
import re
from lxml import etree
 
class WeixinInterface:
 
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def token(requset):

		url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
		Config.AppID, Config.AppSecret)
		result = urllib2.urlopen(url).read()
		Config.access_token = json.loads(result).get('access_token')#获取access_token
		print 'access_token===%s' % Config.access_token
		return HttpResponse(result)
	def createMenu(request):#自定义菜单的实现
		url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % Config.access_token
		data = 
		   { 
				  "button": [
	         {
	            "name": "定制咨询", 

	            "sub_button": 
	        [
	                {
	                    "type": "view", 
	                    "name": "球鞋定制", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "2D/3D墙绘", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "人像彩铅素描", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "手工高级收藏盒", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "滑板/头盔等喷绘", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "个人旅拍视频/写真", 
	                    "url": "http://www.soso.com/"
	                }
	            ]
	       	  }, 
	          {
	            "name": "我要定制", 
	            "sub_button": [
	                {
	                    "type": "view", 
	                    "name": "球鞋", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "汽车/摩托/滑板/头盔/3D墙绘", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "高级盒子", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "人像彩铅绘画/2D墙绘", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "旅拍", 
	                    "url": "http://www.soso.com/"
	                }
	            ]
	          }, 
	          {
	            "name": "关于我们", 
	            "sub_button": [
	                {
	                    "type": "view", 
	                    "name": "CYL介绍", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "CYL签约", 
	                    "url": "http://www.soso.com/"
	                }, 
	                {
	                    "type": "view", 
	                    "name": "工作室介绍", 
	                    "url": "http://www.soso.com/"
	                }
	            ]
	           }
	        ]


		   }
  		req = urllib2.Request(url)
		req.add_header('Content-Type', 'application/json')
		req.add_header('encoding', 'utf-8')
		response = urllib2.urlopen(req, json.dumps(data,ensure_ascii=False))
		result = response.read()
		return HttpResponse(result)
 
    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="icereal" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法        
 
        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
    def POST(self):
         	str_xml = web.data()#获得post来的数据
         	xml = etree.fromstring(str_xml)#解析xml
         	content = xml.find("Content").txt#获得用户输入的内容
         	msgType = xml.find("MsgType").txt
         	fromUser = xml.find("FromUserName").txt
         	toUser = xml.find("ToUserName").txt
         	if msgType == "event":
         		mascontent = xml.find("Event").txt
         		if mascontent == "subscribe":
         			replyTxt == u"欢迎关注custom your life"
         			return self.render.reply_txt(fromUser,toUser,int(time,time()),replyTxt)#关注事件的实现
         		elif mascontent == "unsubscribe":
         			replyTxt == u"期待您的再次关注"
         			return self.render.reply_txt(fromUser,toUser,int(time,time()),replyTxt)#取关时间的实现
         	if msgType == "text":	
         		if content == "1":
         			return self.render.reply_txt(fromUser,toUser,int(time,time()),u"hello,world")#关键字回复
         		elif :
         			return self.render.reply_txt(fromUser,toUser,int(time,time()),u"input 1")

