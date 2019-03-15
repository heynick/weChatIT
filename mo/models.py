from django.db import models
from system.storage import ImageStorage


# 用户信息
class t_user_info(models.Model):
    # 用户id
    user_id = models.CharField(max_length=50)
    # 用户姓名
    user_name = models.CharField(max_length=50)
    # 用户部门id
    user_dept_id = models.CharField(max_length=100)
    # 用户岗位
    user_position = models.CharField(max_length=50)
    # 用户手机
    user_mobile = models.CharField(max_length=20)
    # 用户性别。0表示未定义，1表示男性，2表示女性。
    user_gender = models.CharField(max_length=1)
    # 用户邮箱
    user_email = models.CharField(max_length=100)
    # 用户头像url
    user_avatar = models.CharField(max_length=500)
    # 用户状态
    user_status = models.CharField(max_length=1)
    # 是否领导
    isleader = models.CharField(max_length=1)
    # 扩展属性
    extattr = models.CharField(max_length=500)
    # 用户英文名
    user_eng_name = models.CharField(max_length=50)
    # 用户座机
    user_tel = models.CharField(max_length=20)
    # 是否激活
    enable = models.CharField(max_length=1)
    # 用户隐藏电话
    hide_mobile = models.CharField(max_length=20)
    # 部门内的排序值，默认为0。数量必须和department一致，数值越大排序越前面。值范围是[0, 2^32)。
    order = models.CharField(max_length=100)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)


# 部门信息
class t_dept_info(models.Model):
    # 部门id
    dept_id = models.CharField(max_length=10)
    # 部门名称
    dept_name = models.CharField(max_length=50)
    # 父部门
    parent_dept_id = models.CharField(max_length=10)
    # 在父部门中的次序值。order值大的排序靠前。值范围是[0, 2^32)。
    order = models.CharField(max_length=10)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)


# 事件信息
class t_event_info(models.Model):
    # 事件ID 时间戳|事件代码|申报人userid
    event_id = models.CharField(max_length=50)
    # 事件时间
    event_date = models.DateField(max_length=10)
    # 事件代码
    event_code = models.CharField(max_length=10)
    # 事件等级代码 [1-普通,2-紧急,3-特急]
    event_level_code = models.CharField(max_length=10)
    # 事件状态代码 [1-已申报,2-处理中,3-已处理,4-已关闭]
    event_state_code = models.CharField(max_length=10)
    # 事件描述
    event_desc = models.CharField(max_length=500)
    # 申报人id
    user_id = models.CharField(max_length=20)
    # 联系人
    contact_name = models.CharField(max_length=20)
    # 联系电话
    contact_mobile = models.CharField(max_length=20)
    # 处理人id
    processor_id = models.CharField(max_length=20)
    # 处理描述
    process_desc = models.CharField(max_length=500)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)


# 附件信息
class t_attach_info(models.Model):
    # 文件名称
    image_name = models.CharField(max_length=500)
    # 文件路径
    image_url = models.ImageField(upload_to='img/%Y/%m', storage=ImageStorage())
    # 事件id
    event_id = models.CharField(max_length=50)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)


# 事件分类
class t_event_type(models.Model):
    # 事件代码
    event_code = models.CharField(max_length=10)
    # 事件名称
    event_name = models.CharField(max_length=50)
    # 事件代码状态[1-正常，0-停用]
    event_code_state = models.CharField(max_length=1)
    # 受理部门id
    department_id = models.CharField(max_length=20)
    # 受理人id
    user_id = user_id = models.CharField(max_length=20)
    # 上级事件代码
    parent_event_code = models.CharField(max_length=10)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)


# 系统参数
class t_sys_param(models.Model):
    # 参数名称
    param_name = models.CharField(max_length=50)
    # 参数键
    param_key = models.CharField(max_length=50)
    # 参数值
    param_value = models.CharField(max_length=500)
    # 参数描述
    param_desc = models.CharField(max_length=100)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)


# 公告信息
class t_notice_info(models.Model):
    # 公告id
    notice_id = models.CharField(max_length=50)
    # 公告标题
    notice_title = models.CharField(max_length=50)
    # 公告摘要
    notice_summary = models.CharField(max_length=100)
    # 公告作者
    notice_author = models.CharField(max_length=20)
    # 公告内容
    notice_content = models.CharField(max_length=2000)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)


# 常见问题
class t_common_qu(models.Model):
    # 问题id
    qu_id = models.CharField(max_length=50)
    # 问题标题
    qu_title = models.CharField(max_length=50)
    # 问题描述
    qu_desc = models.CharField(max_length=500)
    # 解决方案
    solution = models.CharField(max_length=2000)
    # 事件代码
    event_code = models.CharField(max_length=10)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)
