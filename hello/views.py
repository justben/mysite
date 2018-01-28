import os
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, FileResponse

from pro import p
import time

# Create your views here.

def uploadFile(request):
	#print(request.POST.get('name'))
	#print(request.POST.get('firstname'))
	return render(request, 'de1.html')
	#return HttpResponse("upload")

def uploadFile_result(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:  
            return HttpResponse("no files for upload!")  
        files = str(myFile)
        #os.chdir("file")
        f = os.path.join("file/", myFile.name)
        destination = open(f,'wb+')    # 打开特定的文件进行二进制的写操作  
        for chunk in myFile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()  
        #os.chdir("..")
        #p.p("file/pipei.txt")
        #ff = "file/result.txt"
        print(f)
        ff = f
        response = file_down(ff)
        return response

def file_down(ff):  
    #file=open('file/test.txt','rb')  
    tempf = ff.split("/")[1]
    file = open(ff, 'rb')
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename='+tempf  
    #return HttpResponse("successful download!")
    return response
