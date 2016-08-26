from django.shortcuts import render, HttpResponse, redirect, reverse
import random
# Create your views here.
def index(request):
    return render(request, "harry_app/index.html")

# Create your views here.
def lockhart(request):
    if "userhp" not in request.session:
        request.session["userhp"] = 100

    if "enemyhp" not in request.session:
        request.session["enemyhp"] = 100

    if "log" not in request.session:
        request.session["log"] = []
    return render(request, "harry_app/lockhart.html")

def potter(request):
    if "userhp" not in request.session:
        request.session["userhp"] = 100
    if "enemyhp" not in request.session:
        request.session["enemyhp"] = 100
    if "log" not in request.session:
        request.session["log"] = []
    return render(request, "harry_app/potter.html")

def process_potter(request):
    potterattack = random.randint(2, 5)
    userhp = request.session["userhp"]
    enemyhp = request.session["enemyhp"]

    if userhp <= 0:
        return redirect(reverse('duel:index'))
    elif enemyhp <= 0:
        return redirect(reverse('duel:index'))

    if request.method == "POST":
        if request.POST["spell"] == "flee":
            return redirect('duel:index')

        elif request.POST["spell"] == "heal":
            if request.session["userhp"] >= 95 and request.session["userhp"] < 100:
                healNum = 1
                request.session["userhp"] += healNum
                userhp += healNum
                request.session["log"].append("You healed " + str(healNum) + " to your total HP!")
            elif request.session["userhp"] == 100:
                healNum = 0
                request.session["userhp"] += healNum
                userhp += healNum
                request.session["log"].append("Max health")
            else:
                healNum = random.randint(2, 5)
                request.session["userhp"] += healNum
                userhp += healNum
                request.session["log"].append("You healed " + str(healNum) + " to your total HP!")

        elif request.POST["spell"] == "attack":
            attackNum = random.randint(2, 5)
            request.session["enemyhp"] -= attackNum
            request.session["log"].append("Expelliarmus hits for " + str(attackNum) + " damage!")
            request.session["userhp"] -= potterattack
            request.session["log"].append("Harry casts Obliviate on you for " + str(potterattack) + " damage!")

        elif request.POST["spell"] == "chance":
            chanceNum = random.randint(-10, 10)
            if chanceNum < 0:
                request.session["log"].append("Expulso blew up in your face! You lost " + str(chanceNum) + " hp!")
                request.session["userhp"] += chanceNum
            else:
                request.session["log"].append("Expulso was a success, " + " Harry takes " + str(chanceNum) + " damage")
                request.session["enemyhp"] -= chanceNum

    return redirect(reverse('duel:potter'))

def process(request):
    lockhartattack = random.randint(2, 5)
    userhp = request.session["userhp"]
    enemyhp = request.session["enemyhp"]

    if userhp <= 0:
        return redirect(reverse('duel:index'))
    elif enemyhp <= 0:
        return redirect(reverse('duel:index'))

    if request.method == "POST":
        if request.POST["spell"] == "flee":
            return redirect('duel:index')

        elif request.POST["spell"] == "heal":
            if request.session["userhp"] >= 95 and request.session["userhp"] < 100:
                healNum = 1
                request.session["userhp"] += healNum
                userhp += healNum
                request.session["log"].append("You healed " + str(healNum) + " to your total HP!")
            elif request.session["userhp"] == 100:
                healNum = 0
                request.session["userhp"] += healNum
                userhp += healNum
                request.session["log"].append("Max health")
            else:
                healNum = random.randint(2, 5)
                request.session["userhp"] += healNum
                userhp += healNum
                request.session["log"].append("You healed " + str(healNum) + " to your total HP!")

        elif request.POST["spell"] == "attack":
            attackNum = random.randint(2, 5)
            request.session["enemyhp"] -= attackNum
            request.session["log"].append("Expelliarmus hits for " + str(attackNum) + " damage!")
            request.session["userhp"] -= lockhartattack
            request.session["log"].append("Lockhart casts Obliviate on you for " + str(lockhartattack) + " damage!")

        elif request.POST["spell"] == "chance":
            chanceNum = random.randint(-10, 10)
            if chanceNum < 0:
                request.session["log"].append("Expulso blew up in your face! You lost " + str(chanceNum) + " hp!")
                request.session["userhp"] += chanceNum
            else:
                request.session["log"].append("Expulso was a success, " + " Lockhart takes " + str(chanceNum) + " damage")
                request.session["enemyhp"] -= chanceNum
    return redirect(reverse('duel:lockhart'))


def clear(request):
    request.session.clear()
    return redirect('duel:index')