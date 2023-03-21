from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Special_Flavors
import datetime
import json

def grab_flavors(file):
    data = json.loads(file)
    new_data = False
    one_off = True
    
    for item in data:
        #offset the error
        if 'special_flavors' in item:
            flavor_name = item['special_flavors']
            if not Special_Flavors.objects.filter(name=flavor_name).exists():
                new_data = True
                if one_off:
                    Special_Flavors.objects.all().delete()
                    one_off = False
                flavor = Special_Flavors(name=flavor_name)
                flavor.save()

    return new_data

@csrf_exempt
def show_flavor(request):
    #IDEA: since POSTS are automatic, if the POST is called, we can call the grab_flavors() func which will UPDATE EVERYTHING
    #then OUTSIDE the: if req.POST
    #we just grab the database and proceed
    #better this way since the values wont needed to be updated each time we click on a button
    is_new = False

    if request.method == 'POST':
        new_data = grab_flavors(request.body)
        is_new = True

    #shows the updated today whenever Scrapy updates it
    date = str(datetime.date.today())
    date = date[date.find('-')+1:]

    flavors = Special_Flavors.objects.all()

    if is_new:
        return render(request, 'special_flavors/special.html', {'flavors':flavors, 'new_data':new_data, 'date':date})
    else:
        return render(request, 'special_flavors/special.html', {'flavors':flavors, 'date':date})