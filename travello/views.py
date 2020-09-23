from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name= 'Kukatpally'
    dest1.img='destination_1.jpg'
    dest1.desc= 'The city of dreams'
    dest1.price= 1000
    dest1.offer=False

    dest2 = Destination()
    dest2.name= 'Secunderabad'
    dest2.img='destination_2.jpg'
    dest2.desc= 'The city of freedom'
    dest2.price= 2000
    dest2.offer=True
    
    dest3 = Destination()
    dest3.name= 'Gandipet'
    dest3.img='destination_3.jpg'
    dest3.desc= 'The city of the south'
    dest3.price= 600
    dest3.offer=False
    
    dest4 = Destination()
    dest4.name= 'Gachibowli'
    dest4.img='destination_4.jpg'
    dest4.desc= 'The city of the south'
    dest4.price= 600
    dest4.offer=False
    
    dest5 = Destination()
    dest5.name= 'Madhapur'
    dest5.img='destination_5.jpg'
    dest5.desc= 'The city of the south'
    dest5.price= 600
    dest5.offer=False
    
    dest6 = Destination()
    dest6.name= 'Kompally'
    dest6.img='destination_6.jpg'
    dest6.desc= 'The city of the south'
    dest6.price= 600
    dest6.offer=False

    dests= [dest1,dest2,dest3,dest4,dest5,dest6]

    return render(request,'index.html',{'dests': dests})