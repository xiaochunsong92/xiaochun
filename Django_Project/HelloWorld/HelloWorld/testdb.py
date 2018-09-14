from django.http import HttpResponse 

from TestModel.models import Test 

def testdb(request):
    response = ""
    response1 = ""

    list = Test.objects.all()

    response2 = Test.objects.filter(id=1)

    response3 = Test.objects.get(id=1)

    Test.objects.order_by('name')[0:2] 

    Test.objects.order_by("id")

    Test.objects.filter(name="runoob").order_by("id")

    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>") 
    
    
    #test1 = Test(name='runoob')
    #test1.save()
    #return HttpResponse("<p>add successful</p>")
