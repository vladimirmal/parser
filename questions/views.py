from django.shortcuts import render
from scrapy_project.spiders.stackoverflow import StackoverflowSpider
from django.http import HttpResponseRedirect,HttpResponse
from scrapy_project.pipelines import ScrapyProjectPipeline
from questions.models import Questions, Tasks
from questions.forms import PostForm
from scrapy_project.pipelines import ScrapyProjectPipeline
from twisted.internet import reactor

import requests

def list_view(request):
    items = Questions.objects.all()

    return render(request, 'questions/indes.html', {
        'title': ScrapyProjectPipeline.result,
        'keyword':ScrapyProjectPipeline.resultkey,
        'description':ScrapyProjectPipeline.resultdesc,
        'link':ScrapyProjectPipeline.resultlink,
        'h1':ScrapyProjectPipeline.resulth1,
        'text':ScrapyProjectPipeline.resulttext,
        'resultgoogl':ScrapyProjectPipeline.resultgoogl,
        'resultyandex':ScrapyProjectPipeline.resultyandex
    })

def contacts_view(request):
    return render(request, 'questions/contact.html', {

    })

def about_view(request):
    return render(request, 'questions/about.html', {

    })
def result_ruk(request):
    return render(request,'questions/result_ruk.html',{

    })

def result_ruk_seo(request):
    return render(request,'questions/result_ruk_seo.html',{
        'title': ScrapyProjectPipeline.result,
        'keyword': ScrapyProjectPipeline.resultkey,
        'description': ScrapyProjectPipeline.resultdesc,
        'link': ScrapyProjectPipeline.resultlink,
        'h1': ScrapyProjectPipeline.resulth1,
        'text': ScrapyProjectPipeline.resulttext,
        'resultgoogl': ScrapyProjectPipeline.resultgoogl,
        'resultyandex': ScrapyProjectPipeline.resultyandex

    })

def result_ruk_index(request):
    return render(request,'questions/result_ruk_index.html',{

    })
def exportdate(request):
    return render(request,'questions/exportdate.html',{

    })
def start_proccess(request):
        item = ScrapyProjectPipeline.process_item
        items = Questions.objects.all()

        # os.environ.setdefault("SCRAPY_SETTINGS_MODULE", "whereyourscrapysettingsare")
def send_form(request):
    if request.method == 'POST':
        url = request.POST['url']
        short_url = url.replace('http://', '')
        short_urls = short_url.replace('https://', '')

        try:
            requests.get(url)
        except Exception:
            return HttpResponse('Not right')
        else:
            task =Tasks(url=url, ip=request.META.get('REMOTE_ADDR'))
            task.save()

            s = StackoverflowSpider()
            s.start_spider(url, short_urls)
            return HttpResponseRedirect('/result/')

    else:
        form = PostForm()
        return render(request, 'questions/form.html', {
            'form': form
        })


def result_view(request):

    return render(request, 'questions/result.html', {
        'title': ScrapyProjectPipeline.result,
        'keyword': ScrapyProjectPipeline.resultkey,
        'description': ScrapyProjectPipeline.resultdesc,
        'link': ScrapyProjectPipeline.resultlink,
        'h1': ScrapyProjectPipeline.resulth1,
        'text': ScrapyProjectPipeline.resulttext,
        'resultgoogl': ScrapyProjectPipeline.resultgoogl,
        'resultyandex': ScrapyProjectPipeline.resultyandex
    })



    # Create your views here.
