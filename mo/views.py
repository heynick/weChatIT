from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core import serializers
from mo.wechat_sdk import *
from mo import models
import operator
import datetime


# 进行故障申报
def rep_event_info(request):
    we = WeChatEnterprise()
    user_id = we.land_web(request)[1].get("UserId")
    # db获取故障类型&紧急程度
    param_report_level = models.t_sys_param.objects.filter(param_name='紧急程度').values('param_desc')
    param_event_type = models.t_event_type.objects.all().values('event_name')
    try:
        contact_info = models.t_user_info.objects.get(user_id=user_id)
    except:
        contact_info = ''
    return render(request, "report.html", {"contact_info": contact_info, 'param_report_level': param_report_level,\
                                           'param_event_type': param_event_type})


# 新增事件信息
def update_event_info(request, param):
    # 获取事件信息
    if request.method == 'POST':
        reportTime_format = datetime.datetime.strptime(request.POST.get("reportTime"), "%Y/%m/%d")
        contactName = request.POST.get("contactName")
        contactMobile = request.POST.get("contactMobile")
        reportDesc = request.POST.get("reportDesc")
        # 获取事件代码
        event_code = models.t_event_type.objects.get(event_name=request.POST.get("reportType")).event_code
        # 事件等级代码
        event_level_code = models.t_sys_param.objects.get(param_name='紧急程度', param_desc=request.POST.get("reportLevel")).param_key
        # 事件状态代码
        event_state_code = models.t_sys_param.objects.get(param_name='事件状态', param_desc='已申报').param_key
        # 拼接事件ID
        t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        event_id = t + event_code + param
        # 新增事件信息
        models.t_event_info.objects.create(event_id=event_id, event_date=reportTime_format, event_code=event_code, \
                                           event_level_code=event_level_code, event_state_code=event_state_code, \
                                           event_desc=reportDesc, user_id=param, contact_name=contactName, \
                                           contact_mobile=contactMobile, processor_id='', \
                                           process_desc='')
        # 新增附件信息
        for i in range(1, 6):
            img = request.FILES.get('img' + str(i))
            if operator.ne(img, None):
                models.t_attach_info.objects.create(image_name=img, image_url=img, event_id=event_id)
    return render(request, "processsuccess.html")


# 获取申报列表
def get_event_list(request):
    we = WeChatEnterprise()
    user_id = we.land_web(request)[1].get("UserId")
    # 读取事件信息并返回
    event_overview = models.t_event_info.objects.filter(user_id=user_id).order_by('-create_time').values()
    # 事件名称 事件等级 事件状态
    for i in range(0, len(event_overview)):
        event_name = models.t_event_type.objects.get(event_code=event_overview[i].get('event_code'))
        level_name = models.t_sys_param.objects.get(param_key=event_overview[i].get('event_level_code'))
        state_name = models.t_sys_param.objects.get(param_key=event_overview[i].get('event_state_code'))
        event_overview[i]['event_name'] = event_name.event_name
        event_overview[i]['level_name'] = level_name.param_desc
        event_overview[i]['state_name'] = state_name.param_desc
    return render(request, "recordlist.html", {"event_overview": event_overview})


# 获取申报记录
def get_event_info(request, param):
    # 事件信息
    event_info = models.t_event_info.objects.filter(event_id=param).values()[0]
    # 事件名称 事件等级 事件状态 处理人
    event_name = models.t_event_type.objects.get(event_code=event_info.get('event_code'))
    level_name = models.t_sys_param.objects.get(param_key=event_info.get('event_level_code'))
    state_name = models.t_sys_param.objects.get(param_key=event_info.get('event_state_code'))
    try:
        process_name = models.t_user_info.objects.get(user_id=event_info.get('processor_id'))
    except:
        process_name = ''
    # 附件信息
    attach_info = models.t_attach_info.objects.filter(event_id=param)
    return render(request, "record.html", {"event_info": event_info, "attach_info": attach_info, \
                                           "event_name": event_name, "level_name": level_name, "state_name": state_name, \
                                           "process_name": process_name})


# 获取附件
def get_img_info(request, param):
    # 读取事件信息并返回
    img_info = models.t_attach_info.objects.get(id=param)
    return render(request, "gallery.html", {"img_info": img_info})


# 取消申报
def delete_event(request, param):
    models.t_event_info.objects.get(event_id=param).delete()
    models.t_attach_info.objects.filter(event_id=param).delete()
    return render(request, "success.html")


# 关闭事件
def close_event(request, param):
    event_state = models.t_sys_param.objects.get(param_name='事件状态', param_desc='已关闭')
    models.t_event_info.objects.filter(event_id=param).update(event_state_code=event_state.param_key)
    return render(request, "success.html")


# 获取工单列表
def process_event_list(request):
    we = WeChatEnterprise()
    user_id = we.land_web(request)[1].get("UserId")
    # 根据user_id获取个人信息
    user_info = models.t_user_info.objects.get(user_id=user_id)
    user_dept_info = models.t_dept_info.objects.filter(dept_id__in=user_info.user_dept_id).values('dept_name')
    role = 0
    for i in range(0, len(user_dept_info)):
        if operator.eq(user_dept_info[i].get('dept_name'), '运维中心'):
            role = 1
    # 针对运维中心人员，获取全部“已申报/处理中”工单，即用有分配权限
    event_state_code = models.t_sys_param.objects.filter(param_name='事件状态', param_desc__in=('已申报', '处理中', '已处理')).values('param_key')
    if operator.eq(role, 1):
        event_overview = models.t_event_info.objects.filter(event_state_code__in=event_state_code).values()
    # 非运维中心人员，获取“处理人为自己”的“已申报/处理中”并显示
    elif operator.eq(role, 0):
        event_overview = models.t_event_info.objects.filter(processor_id=user_id).filter(event_state_code__in=event_state_code).values()
    # 事件名称 事件等级 事件状态
    for i in range(0, len(event_overview)):
        event_name = models.t_event_type.objects.get(event_code=event_overview[i].get('event_code'))
        level_name = models.t_sys_param.objects.get(param_key=event_overview[i].get('event_level_code'))
        state_name = models.t_sys_param.objects.get(param_key=event_overview[i].get('event_state_code'))
        event_overview[i]['event_name'] = event_name.event_name
        event_overview[i]['level_name'] = level_name.param_desc
        event_overview[i]['state_name'] = state_name.param_desc
    return render(request, "processlist.html", {'event_overview': event_overview})


# 处理工单
def process_event_info(request, param):
    # 事件信息
    event_info = models.t_event_info.objects.filter(event_id=param).values()[0]
    # 事件名称 事件等级 事件状态
    event_name = models.t_event_type.objects.get(event_code=event_info.get('event_code'))
    level_name = models.t_sys_param.objects.get(param_key=event_info.get('event_level_code'))
    state_name = models.t_sys_param.objects.get(param_key=event_info.get('event_state_code'))
    # 附件信息
    attach_info = models.t_attach_info.objects.filter(event_id=param)
    # 处理人
    dept_id = models.t_dept_info.objects.get(dept_name='运维中心')
    processor = models.t_user_info.objects.filter(user_dept_id__contains=dept_id.dept_id).values()
    return render(request, "process.html", {"event_info": event_info, "attach_info": attach_info, \
                                            "event_name": event_name, "level_name": level_name, \
                                            "state_name": state_name, "processor": processor})


# 更新处理信息
def update_process(request, param):
    if request.method == 'POST':
        eventState = request.POST.get("eventState")
        processor_name = request.POST.get("processor_name")
        processDesc = request.POST.get("processDesc")
        state_id = models.t_sys_param.objects.get(param_desc=eventState)
        processor_id = models.t_user_info.objects.get(user_name=processor_name)
        # 更新事件信息表
        models.t_event_info.objects.filter(event_id=param).update(event_state_code=state_id.param_key, \
                                                                  processor_id=processor_id.user_id, process_desc=processDesc)
    return render(request, "processsuccess.html")


# 获取个人信息
def get_user_info(request):
    we = WeChatEnterprise()
    user_id = we.land_web(request)[1].get("UserId")
    # 根据user_id获取个人信息
    user_info = models.t_user_info.objects.get(user_id=user_id)
    user_dept_info = models.t_dept_info.objects.filter(dept_id__in=user_info.user_dept_id).values('dept_name')
    # 返回个人信息
    return render(request, "person.html", {"user_info": user_info, 'user_dept_info': user_dept_info})


# 获取事件公告
def get_notice_list(request):
    notice_list = models.t_notice_info.objects.all().values()
    for i in range(0, len(notice_list)):
        attach_info = models.t_attach_info.objects.get(event_id=notice_list[i].get('notice_id'))
        notice_list[i]['image_url'] = attach_info.image_url
    return render(request, "noticelist.html", {'notice_list': notice_list})


# 获取事件公告-查看更多
def get_all_notice_list(request):
    notice_list = models.t_notice_info.objects.all().values()
    for i in range(0, len(notice_list)):
        attach_info = models.t_attach_info.objects.get(event_id=notice_list[i].get('notice_id'))
        notice_list[i]['image_url'] = attach_info.image_url
    return render(request, "noticelistall.html", {'notice_list': notice_list})


# 获取事件公告-详细
def get_notice_info(request, param):
    notice_info = models.t_notice_info.objects.get(notice_id=param)
    update_time = datetime.datetime.strftime(notice_info.update_time, "%Y-%m-%d")
    attach_info = models.t_attach_info.objects.get(event_id=param)
    return render(request, "notice.html", {'notice_info': notice_info, 'update_time': update_time, 'attach_info': attach_info})


# 常见问题
def get_question_info(request):
    event_type = models.t_event_type.objects.filter(parent_event_code='0')
    return render(request, "question.html", {'event_type': event_type})


# 问题二级目录
def get_question_sec_info(request):
    main_type = request.POST.get("main_type")
    if operator.ne(main_type, None):
        event_main_type = models.t_event_type.objects.get(event_name=main_type)
        event_sec_type = models.t_event_type.objects.filter(parent_event_code=event_main_type.event_code)
        sec_type = []
        for i in range(0, len(event_sec_type)):
            sec_type.append(event_sec_type[i].event_name)
        data_sec_type = {'sec_type': sec_type}
        return HttpResponse(json.dumps(data_sec_type), content_type='application/json')


# 问题三级目录
def get_question_th_info(request):
    sec_type = request.POST.get("sec_type")
    if operator.ne(sec_type, None):
        event_sec_type = models.t_event_type.objects.get(event_name=sec_type)
        event_th_type = models.t_event_type.objects.filter(parent_event_code=event_sec_type.event_code)
        th_type = []
        for i in range(0, len(event_th_type)):
            th_type.append(event_th_type[i].event_name)
        data_th_type = {'th_type': th_type}
        return HttpResponse(json.dumps(data_th_type), content_type='application/json')

# 问题解决方案
def get_question_sol_info(request):
    th_type = request.POST.get("th_type")
    if operator.ne(th_type, None):
        sol = models.t_common_qu.objects.get(qu_title=th_type)
        data_sol = {'sol': sol.solution}
        return HttpResponse(json.dumps(data_sol), content_type='application/json')