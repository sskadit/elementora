from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from assign.settings import BASE_DIR
import json
from .models import Data




def simple_upload(request):
	if request.method == 'POST' and request.FILES['myfile']:
		query = Data.objects.all().delete()
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		module_dir = os.path.dirname(__file__)
		file_path = os.path.join(module_dir, uploaded_file_url)
		file_path_open  = os.path.join(BASE_DIR,file_path)
		new_path = BASE_DIR + file_path_open

		# print(file_path_open)	
		with open(new_path) as f:
			data1 = json.load(f)
			# data2 = json.dumps(f)
			# print(data1['messages']['id'])
			# new = data1.values()
			for i in data1['messages']:
				# print(i['text'])
				Data.objects.create(
					id_generated = i['id'],
					text = i['text'],
					number = i['number'],
					mms = i['mms'],
					sender = i['sender'],
					datetime = i['datetime'],
					timestamp_client = i['timestamp']
					)
			# print(new['sender'])
			
		# 		# do something with data
		return render(request, 'upload.html', {
			'uploaded_file_url': uploaded_file_url
		})
	return render(request, 'upload.html')

def analytics(request):
	query = Data.objects.all()
	if query:
		context = {
		"query":query
		}
	return render(request, 'display.html',context)



def display(request):
	query = Data.objects.all()
	if query:
		context = {
		"query":query
		}
	return render(request, 'display.html',context)