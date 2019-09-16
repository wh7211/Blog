from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse # django2.0已废弃
from django.urls import reverse
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'blogs/index.html')

def topics(request):
    """显示所有的主题"""
    topics = BlogPost.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blogs/topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = BlogPost.objects.get(id=topic_id)
    context = {'topic': topic}
    return render(request, 'blogs/topic.html', context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = BlogPostForm()
    else:
        # POST提交的数据,对数据进行处理
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:topics'))

    context = {'form': form}
    return render(request, 'blogs/new_topic.html', context)

def edit_topic(request, topic_id):
    """编辑既有条目"""
    topic = BlogPost.objects.get(id=topic_id)

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = BlogPostForm(instance=topic)
    else:
        # POST提交的数据，对数据进行处理
        form = BlogPostForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:topic',
                    args=[topic.id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'blogs/edit_topic.html', context)

