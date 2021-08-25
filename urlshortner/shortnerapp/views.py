from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pyshorteners
import json
import os
# Create your views here.
'''
this is api which will short the URL'''
@api_view(["POST"])
def home(request):
    if request.method == "POST":
        data = request.data
        link = data["url"]
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, "urlmap.json")
        with open(file_path, "r+") as f:
            d = json.load(f)
            cache_key = d.get(link)
            if cache_key:
                return Response(
                    {
                        "status": 200,
                        "shorturl": cache_key,
                        "message": "successfully short the url",
                    }
                )
            else:
                shortners = pyshorteners.Shortener()
                newData = shortners.tinyurl.short(link)
                d[link] = newData
                f.seek(0)
                json.dump(d, f)
                return Response(
                    {
                        "status": 200,
                        "shorturl": newData,
                        "message": "successfully short the url",
                    }
                )
