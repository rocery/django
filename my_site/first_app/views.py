from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def simple_view(request):
    return render(request, 'first_app/example.html') # .html 



# Uncomment code below 
# # Create your views here.
# articles = {
#     'sports':'Sports Page',
#     'finance':'Finance Page',
#     'politics':'Politics Page'
# }

# def news_view(request, topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(articles[topic])
#     except:
#         raise Http404("404 GENERIC ERROR")
    
# # domain.com/first_app/0 --> domain.com/first_app/sports
# def num_page_view(request, num_page):
    
#     topics_list = list(articles.keys()) # ['sports','finance','politics']
#     topic = topics_list[num_page]

#     return HttpResponseRedirect(reverse('topic-page', args=[topic]))