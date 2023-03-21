from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Standard_Flavors
import json

# Create your views here.

#better for it to be here, will be executed after each file click
def grab_flavors(file):
    data = json.loads(file)
    one_off = True
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
        grab_flavors(request.body)

    flavors = Standard_Flavors.objects.all()
    return render(request, 'standard_flavors/standard.html', {'flavors':flavors})



