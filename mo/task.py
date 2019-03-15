from mo.wechat_sdk import *
from mo import models


def update_user_and_dept_info():
    we = WeChatEnterprise()
    # 同步部门信息
    dept = we.get_department_list()[1].get('department')
    for i in range(0, len(dept)):
        dept_id = dept[i].get('id')
        dept_name = dept[i].get('name')
        parent_dept_id = dept[i].get('parentid')
        order = dept[i].get('order')
        models.t_dept_info.objects.update_or_create\
            (dept_id=dept_id, defaults={'dept_name': dept_name, 'parent_dept_id': parent_dept_id, 'order': order})
    # 同步用户信息，根部门不能删除且ID为1
    users_id = we.get_users_in_department(1, 1, 0)[1].get('userlist')
    for i in range(0, len(users_id)):
        userid = users_id[i].get('userid')
        user_info = we.get_user(userid)[1]
        user_name = user_info.get('name')
        user_dept_id = user_info.get('department')
        user_position = user_info.get('position')
        user_mobile = user_info.get('mobile')
        user_gender = user_info.get('gender')
        user_email = user_info.get('email')
        user_avatar = user_info.get('avatar')
        user_status = user_info.get('status')
        isleader = user_info.get('isleader')
        extattr = user_info.get('extattr')
        user_eng_name = user_info.get('english_name')
        user_tel = user_info.get('telephone')
        enable = user_info.get('enable')
        hide_mobile = user_info.get('hide_mobile')
        order = user_info.get('order')
        models.t_user_info.objects.update_or_create\
            (user_id=userid, defaults={'user_name': user_name, 'user_dept_id': user_dept_id, \
                                       'user_position': user_position, 'user_mobile': user_mobile, \
                                       'user_gender': user_gender, 'user_email': user_email, 'user_avatar': user_avatar, \
                                       'user_status': user_status, 'isleader': isleader, 'extattr': extattr, \
                                       'user_eng_name': user_eng_name, 'user_tel': user_tel, 'enable': enable, \
                                       'hide_mobile': hide_mobile, 'order': order})
    # 初始化系统参数
    models.t_sys_param.objects.update_or_create(param_key='A1', defaults={'param_name': '紧急程度', 'param_desc': '普通', 'param_value': '1'})
    models.t_sys_param.objects.update_or_create(param_key='A2', defaults={'param_name': '紧急程度', 'param_desc': '紧急', 'param_value': '2'})
    models.t_sys_param.objects.update_or_create(param_key='A3', defaults={'param_name': '紧急程度', 'param_desc': '特急', 'param_value': '3'})
    models.t_sys_param.objects.update_or_create(param_key='B0', defaults={'param_name': '用户性别', 'param_desc': '未选择', 'param_value': '0'})
    models.t_sys_param.objects.update_or_create(param_key='B1', defaults={'param_name': '用户性别', 'param_desc': '男', 'param_value': '1'})
    models.t_sys_param.objects.update_or_create(param_key='B2', defaults={'param_name': '用户性别', 'param_desc': '女', 'param_value': '2'})
    models.t_sys_param.objects.update_or_create(param_key='C1', defaults={'param_name': '用户状态', 'param_desc': '已激活', 'param_value': '1'})
    models.t_sys_param.objects.update_or_create(param_key='C2', defaults={'param_name': '用户状态', 'param_desc': '已禁用', 'param_value': '2'})
    models.t_sys_param.objects.update_or_create(param_key='C4', defaults={'param_name': '用户状态', 'param_desc': '未激活', 'param_value': '4'})
    models.t_sys_param.objects.update_or_create(param_key='D0', defaults={'param_name': '是否上级', 'param_desc': '否', 'param_value': '0'})
    models.t_sys_param.objects.update_or_create(param_key='D1', defaults={'param_name': '是否上级', 'param_desc': '是', 'param_value': '1'})
    models.t_sys_param.objects.update_or_create(param_key='E1', defaults={'param_name': '事件状态', 'param_desc': '已申报', 'param_value': '1'})
    models.t_sys_param.objects.update_or_create(param_key='E2', defaults={'param_name': '事件状态', 'param_desc': '处理中', 'param_value': '2'})
    models.t_sys_param.objects.update_or_create(param_key='E3', defaults={'param_name': '事件状态', 'param_desc': '已处理', 'param_value': '3'})
    models.t_sys_param.objects.update_or_create(param_key='E4', defaults={'param_name': '事件状态', 'param_desc': '已关闭', 'param_value': '4'})

    models.t_event_type.objects.update_or_create(event_code='001', defaults={'event_name': '业务系统故障'})
    models.t_event_type.objects.update_or_create(event_code='002', defaults={'event_name': '办公设备故障'})
    models.t_event_type.objects.update_or_create(event_code='003', defaults={'event_name': '网络故障'})
    models.t_event_type.objects.update_or_create(event_code='004', defaults={'event_name': '后台查账需求'})
    models.t_event_type.objects.update_or_create(event_code='005', defaults={'event_name': '系统使用咨询'})
    models.t_event_type.objects.update_or_create(event_code='006', defaults={'event_name': '业务问题咨询'})
