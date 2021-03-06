#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-22 18:15:46
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import xadmin

from xadmin import views #添加Xadmin的主题功能

from .models import EmailVerifyRecord
from .models import Banner
#xadmin中这里是继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
	#显示EmailVerifyRecord中的列
	list_display=['code','email','send_type','send_time']
	#搜索的字段，不要添加时间搜索
	search_fields=['code','email','send_type']

	#过滤
	list_filter=['code','email','send_type','send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)


class BannerAdmin(object):
	#显示Banner中的字段
	list_display=['title','image','url','index','add_time']
	#搜索字段配置
	search_fields=['title','image','url','index']

	#过滤
	list_filter=['title','image','url','index','add_time']

xadmin.site.register(Banner,BannerAdmin)


#添加Xadmin的主题功能
# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
	#开启主题功能
	enable_themes=True
	use_bootswatch=True

xadmin.site.register(views.BaseAdminView,BaseSetting)

#全局修改，固定写法
class GlobalSettings(object):
	#修改title
	site_title='我的教育网站后台管理'
	#修改footer
	site_footer='时间轮回'
	#收起菜单
	# menu_style='accordion'

#将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)
