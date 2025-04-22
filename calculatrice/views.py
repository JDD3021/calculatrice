from django.shortcuts import render
from .forms import CalculForm
import re, math

def calculatrice(request):
    return render(request, 'calculatrice.html')

def index(request):
    ecran = ''
    if request.method == 'POST':
        if 'clear' in request.POST:
            ecran = ''
        elif 'delete' in request.POST:
            ecran = request.POST.get('ecran', '')
            ecran = ecran[:-1]
        else:
            ecran = request.POST.get('ecran', '')
            btn = request.POST.get('btn')
            if btn:
                ecran += btn
            elif request.POST.get('submit') == "=":
                ecran = ecran.replace('√', 'math.sqrt')
                if re.fullmatch(r"[0-9+\-*/().√a-z ]+", ecran):
                    try:
                        ecran = str(eval(ecran, {"__builtins__": None, "math": math}))
                    except:
                        ecran = 'Erreur'
                else:
                    ecran = "Expression non valide"
            elif request.POST.get('clear') == "ok":
                ecran =''  
        
    return render(request, "index.html", {"ecran":ecran})
