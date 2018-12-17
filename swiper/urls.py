"""swiper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from user import api as user_api
from social import api as social_api
from vip import api as vip_api


urlpatterns = [
    url(r'^api/user/vcode$', user_api.get_verify_code),
    url(r'^api/user/login$', user_api.login),
    url(r'^api/user/user_back$', user_api.user_back),
    url(r'^api/user/profile/show$', user_api.show_profile),
    url(r'^api/user/profile/modify$', user_api.modify_profile),
    url(r'^api/user/avatar/upload$', user_api.upload_avatar),

    url(r'^api/social/rcmd_users$', social_api.get_rcmd_users),
    url(r'^api/social/new_rcmd_users$', social_api.new_rcmd_users),
    url(r'^api/social/like$', social_api.like),
    url(r'^api/social/superlike$', social_api.superlike),
    url(r'^api/social/dislike$', social_api.dislike),
    url(r'^api/social/rewind$', social_api.rewind),
    url(r'^api/social/liked_me$', social_api.show_liked_me),
    url(r'^api/social/friends$', social_api.get_friends),
    url(r'^api/social/hotrank$', social_api.hot_swiped),

    url(r'^api/vip/permissions$', vip_api.show_vip_permissions),
]
