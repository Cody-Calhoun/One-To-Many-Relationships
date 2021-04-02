from django.shortcuts import render, redirect
from .models import Team, Player

# Create your views here.
def index(request):
    team1 = Team.objects.get(id=1)
    context = {
        'all_teams' : Team.objects.all(), 
        'all_players' : Player.objects.all()

    }
    return render(request, 'index.html', context)


def new_team(request):
    new_team = Team.objects.create(
        name = request.POST['name'],
        wins = request.POST['wins'],
        location = request.POST['location'],
        mascot = request.POST['mascot']
    )
    return redirect('/')


def new_player(request):
    new_player = Player.objects.create(
        name = request.POST['name'],
        jersey_number = request.POST['jersey'],
        position = request.POST['position'],
        batting_avg = request.POST['bat_avg'],
        current_team = Team.objects.get(id=request.POST['curr_team'])
    )
    return redirect('/')