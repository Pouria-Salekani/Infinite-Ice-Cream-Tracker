from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Special_Flavors
import datetime
import json

def grab_flavors(file):
    data = json.loads(file)
    new_data = False
    one_off = True

    flavor = Special_Flavors(name=flavor_name)
    
    # for item in data:
    #     #offset the error
    #     if item == 'special_flavors':
    #         for spc in data[item]:
    #             flavor_name = spc
    #             if not Special_Flavors.objects.filter(name=flavor_name).exists():
    #                 new_data = True
    #                 if one_off:
    #                     Special_Flavors.objects.all().delete()
    #                     one_off = False
    #                 flavor = Special_Flavors(name=flavor_name)
    #                 flavor.save()

    for item in data:
        #offset the error
        if item == 'special_flavors':
            for std in data[item]:
                flavor_name = std
                flavor = Special_Flavors(name=flavor_name)
                flavor.save()

    return new_data

@csrf_exempt
def show_flavor(request):
    #IDEA: since POSTS are automatic, if the POST is called, we can call the grab_flavors() func which will UPDATE EVERYTHING
    #then OUTSIDE the: if req.POST
    #we just grab the database and proceed
    #better this way since the values wont needed to be updated each time we click on a button

    if request.method == 'POST':

        print('WORKS FROM SPECIAL side')
        print(request.body)

        new_data = grab_flavors(request.body)

        #shows the updated today whenever Scrapy updates it
        date = str(datetime.date.today())
        date = date[date.find('-')+1:]

        flavors = Special_Flavors.objects.all()
        return render(request, 'special_flavors/special.html', {'flavors':flavors, 'new_data':new_data, 'date':date})

    else:
        flavors = Special_Flavors.objects.all()
        return render(request, 'special_flavors/special.html', {'flavors':flavors})