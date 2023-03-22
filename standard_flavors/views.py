from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Standard_Flavors
import datetime
import json


def check_new_data(data):
    new_data = False
    for item in data:
        if item == 'standard_flavors':
            for std in data[item]:
                flavor_name = std
                if not Standard_Flavors.objects.filter(name=flavor_name).exists():
                     new_data = True

    return new_data

#better for it to be here, will be executed after each file click
def grab_flavors(file):
    data = json.loads(file)
    new_data = check_new_data(data)
    Standard_Flavors.objects.all().delete()

    # for item in data:
    #     #offset the error
    #     if item == 'standard_flavors':
    #         for std in data[item]:
    #             flavor_name = std
    #             if not Standard_Flavors.objects.filter(name=flavor_name).exists():
    #                 print(flavor_name, ' -----DOES NOT EXIST')
    #                 if one_off:
    #                     Standard_Flavors.objects.all().delete()
    #                     one_off = False
    #                 flavor = Standard_Flavors(name=flavor_name)
    #                 flavor.save()

    for item in data:
        #offset the error
        if item == 'standard_flavors':
            for std in data[item]:
                flavor_name = std
                flavor = Standard_Flavors(name=flavor_name)
                flavor.save()
    
    return new_data


    
                #flavor = Standard_Flavors.objects.get(name=flavor_name)
                #update the name
                #flavor.name = flavor_name

            # else:
            #     flavor = Standard_Flavors(name=flavor_name)
            #     flavor.save()

@csrf_exempt
def show_flavor(request):
    if request.method == 'POST':
        print('STANDARD SIDE YEE')
        print(request.body)

        new_data = grab_flavors(request.body)

        #shows the updated today whenever Scrapy updates it
        date = str(datetime.date.today())
        date = date[date.find('-')+1:]

        flavors = Standard_Flavors.objects.all()
        return render(request, 'standard_flavors/standard.html', {'flavors':flavors, 'new_data':new_data, 'date':date})

    else:
        flavors = Standard_Flavors.objects.all()
        return render(request, 'standard_flavors/standard.html', {'flavors':flavors})



