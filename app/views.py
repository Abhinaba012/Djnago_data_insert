from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from app.models import *

def insert_sport(request):
    sno = input('Enter The Sport Name : ')
    toj = Sport.objects.get_or_create(sport_name =  sno)
    if toj[1]:
        return HttpResponse('New Sport_name created')
    else:
        return HttpResponse('Given Sport is Already Present')
    
def insert_club(request):
    sn = input('Enter the sport name : ')
    cno = input('Enter the Club Name : ')
    url = input('Enter the Club url : ')
    date = input('Enter the Estd : ')
    email = input('Enter the Email : ')
    obj = Sport.objects.filter(sport_name = sn)
    if obj:
        clobj = Club.objects.get_or_create(sport_name = obj[0], club_name = cno, url = url, est_date = date, email = email)

        if clobj[1]:
            return HttpResponse('New Club is Created')
        else:
            return HttpResponse('Club is Already there')
    else:
        return HttpResponse('Sorry We can not find any match')
    
def insert_player(request):
    pk = int(input('Enter the pk of Club : '))
    pn = input('Enter the player name : ')
    age = int(input('Enter Age : '))
    trophies = int(input('Enter the number of trophies : '))
    height = int(input('Enter the height : '))
    obj = Club.objects.filter(pk = pk)
    if obj:
        plobj = Player.objects.get_or_create(club_name = obj[0], player_name = pn, age = age, trophies = trophies, height = height)

        if plobj[1]:
            return HttpResponse('New Player Record Created')
        else:
            return HttpResponse('player Details Already Exists')
    else:
        return HttpResponse('Sorry we do not have this records')




