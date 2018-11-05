import requests
from bs4 import BeautifulSoup
import re

# 基本用法
# html=requests.get('https://news.ycombinator.com/')
html=requests.get('https://www.baidu.com')
# 传入html.content而不是html对象
soup=BeautifulSoup(html.content,'lxml')
# 以正确缩进方式打印html内容
# print(soup.prettify())

# # 选择元素以内容
print(soup.title)
print(soup.head.title)
print("type ==>", type(soup.title))
# print(soup.title.string)
print(soup.p)
# print(soup.p.a)
# print(soup.p.a.string)
print(soup.title.name)    # 获取名称

# # 获取属性
print(soup.p.attrs)
print(soup.p.attrs['id']) # 方法1
print(soup.p['id']) # 方法2

# 获取所有直接子节点
print(soup.head.contents) # 获取list
print(soup.head.children) # 获取iterator
# for i, child in enumerate(soup.head.children):
for i, child in enumerate(soup.head.children):
    print(i, child)

# 获取所有子节点
print(soup.head.descendants)
for i, child in enumerate(soup.head.descendants):
    print(i, child)

# 获取直接父节点
print(soup.head.meta.parent)

# 获取所有祖先节点
print(soup.head.meta.parents)
for i, child in enumerate(soup.head.meta.parents):
    print(i, child)

print(soup.head.meta.parents)
for i, child in enumerate(soup.head.meta.parents):
    print(i, child)

print("=====获取siblings====")
print(soup.head.meta.next_sibling)
print(list(soup.head.meta.next_siblings))
print(soup.head.meta.previous_sibling)
print(list(soup.head.meta.previous_siblings))

print("=====提取信息==========")
print(soup.head.meta.next_sibling["http-equiv"])
print(list(soup.head.meta.next_siblings))
print(list(soup.head.meta.next_siblings)[2]["href"])

print("======方法选择器==========")
print(soup.find_all("a")) # 按照节点名
print(soup.find_all(attrs={'id':'u1'})) # 按照attrs
print(soup.find_all(text=re.compile("更多"))) # 按照text

print("======CSS选择器==========")
print(soup.select('head meta')) # 按照节点名
print(soup.select('.head_wrapper .s_form')) # 按照class
print(soup.select('#ftCon a')) # 按照id

print("======嵌套选择==========")
for i, div in list(enumerate(soup.select('div'))):
    print(i, div)
    print(i, div.select('a'), '\n')

# HTML content for this file
'''
DOCTYPE html>
<!--STATUS OK-->
<html>
 <head>
  <meta content="text/html;charset=utf-8" http-equiv="content-type"/>
  <meta content="IE=Edge" http-equiv="X-UA-Compatible"/>
  <meta content="always" name="referrer"/>
  <link href="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css"/>
  <title>
   百度一下，你就知道
  </title>
 </head>
 <body link="#0000cc">
  <div id="wrapper">
   <div id="head">
    <div class="head_wrapper">
     <div class="s_form">
      <div class="s_form_wrapper">
       <div id="lg">
        <img height="129" hidefocus="true" src="//www.baidu.com/img/bd_logo1.png" width="270"/>
       </div>
       <form action="//www.baidu.com/s" class="fm" id="form" name="f">
        <input name="bdorz_come" type="hidden" value="1"/>
        <input name="ie" type="hidden" value="utf-8"/>
        <input name="f" type="hidden" value="8"/>
        <input name="rsv_bp" type="hidden" value="1"/>
        <input name="rsv_idx" type="hidden" value="1"/>
        <input name="tn" type="hidden" value="baidu"/>
        <span class="bg s_ipt_wr">
         <input autocomplete="off" autofocus="autofocus" class="s_ipt" id="kw" maxlength="255" name="wd" value=""/>
        </span>
        <span class="bg s_btn_wr">
         <input autofocus="" class="bg s_btn" id="su" type="submit" value="百度一下"/>
        </span>
       </form>
      </div>
     </div>
     <div id="u1">
      <a class="mnav" href="http://news.baidu.com" name="tj_trnews">
       新闻
      </a>
      <a class="mnav" href="https://www.hao123.com" name="tj_trhao123">
       hao123
      </a>
      <a class="mnav" href="http://map.baidu.com" name="tj_trmap">
       地图
      </a>
      <a class="mnav" href="http://v.baidu.com" name="tj_trvideo">
       视频
      </a>
      <a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">
       贴吧
      </a>
      <noscript>
       <a class="lb" href="http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1" name="tj_login">
        登录
       </a>
      </noscript>
      <script>
       document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">登录</a>');
      </script>
      <a class="bri" href="//www.baidu.com/more/" name="tj_briicon" style="display: block;">
       更多产品
      </a>
     </div>
    </div>
   </div>
   <div id="ftCon">
    <div id="ftConw">
     <p id="lh">
      <a href="http://home.baidu.com">
       关于百度
      </a>
      <a href="http://ir.baidu.com">
       About Baidu
      </a>
     </p>
     <p id="cp">
      ©2017 Baidu
      <a href="http://www.baidu.com/duty/">
       使用百度前必读
      </a>
      <a class="cp-feedback" href="http://jianyi.baidu.com/">
       意见反馈
      </a>
      京ICP证030173号
      <img src="//www.baidu.com/img/gs.gif"/>
     </p>
    </div>
   </div>
  </div>
 </body>
</html>
'''
