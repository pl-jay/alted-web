import requests
from django.shortcuts import render
from django.http import HttpResponse, response
from django.http import JsonResponse

from alteducation_web.settings import FILE_UPLOAD_API, WORD_PROCESSOR_API


def index(request):
    return render(request, 'index.html')


def wordprocessor_request(request):
    WORD_PR_API = WORD_PROCESSOR_API
    response = requests.get(WORD_PR_API)
    return JsonResponse({
        'response': response.text
    })


def login(request):
    return render(request, 'login.html')


def upload_page(request):
    context = {}
    context['file_upload_api'] = FILE_UPLOAD_API
    return render(request, 'uploadpage.html', context)


def word_processor(request):
    dict_file_path, doc_file_path = (1, 4)
    # sentence_freq_rank, kincaid_score, dict_file_path, doc_file_path = (
    #     1, 2, 3, 4)

    return JsonResponse({
        'doc_file_path': doc_file_path,
        'dict_file_path': dict_file_path})
