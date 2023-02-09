from django.http import HttpResponse
from django.shortcuts import render

def secondView(request):
    return HttpResponse('''
        <html>
            <h1>View in second app</h1>
        </html>''')
    
