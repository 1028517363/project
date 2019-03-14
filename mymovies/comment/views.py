from django.shortcuts import render
from django.http import HttpResponse
from comment.forms import UserMovieCommentForm
# Create your views here.


def user_movie_comment(request):
    '''
    1.对电影的评论信息
    2.谁来评论
    3.评论哪一个电影
    4.评论信息
    5.评论时间》》》自动生成
    :param request:
    :return:
    '''
    pass
    x = request
    user = request.POST['user']
    res = UserMovieCommentForm(request.POST)
    if res.is_valid():
        res.save()
    return HttpResponse('sds')