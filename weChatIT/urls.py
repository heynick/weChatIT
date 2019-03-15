"""weChatIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from mo import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # 管理界面
    path('admin/', admin.site.urls),
    # 故障申报
    path('report/', views.rep_event_info),
    # 故障申报跳转
    path('report/success/<str:param>', views.update_event_info),
    # 申报列表
    path('recordlist/', views.get_event_list),
    # 申报记录
    path('record/<str:param>', views.get_event_info),
    # 图片预览
    path('gallery/<str:param>', views.get_img_info),
    # 取消申报
    path('cancel/success/<str:param>', views.delete_event),
    # 关闭事件
    path('close/success/<str:param>', views.close_event),
    # 工单列表
    path('processlist/', views.process_event_list),
    # 处理工单
    path('process/<str:param>', views.process_event_info),
    # 处理工单跳转
    path('process/success/<str:param>', views.update_process),
    # 个人信息
    path('person/', views.get_user_info),
    # 事件公告
    path('noticelist/', views.get_notice_list),
    # 事件公告-查看更多
    path('noticelistall/', views.get_all_notice_list),
    # 事件公告-详细
    path('notice/<str:param>', views.get_notice_info),
    # 常见问题
    path('question/', views.get_question_info),
    # 常见问题-sec
    path('question/sec/', views.get_question_sec_info),
    # 常见问题-th
    path('question/th/', views.get_question_th_info),
    # 常见问题-sol
    path('question/sol/', views.get_question_sol_info),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
