#Common imports might want to look into a template for these. 
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse #reverse allows you to look for a path by name rather than hard coding it into the project. 
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Take A walk",
    "february": "Take A hike",
    "march": "Take A trip",
    "april": "Take A chill pill",
    "may": "Take A nap",
    "june": "Take A drive",
    "july": "Take A flight",
    "august": "Take A drink",
    "september": "Take A sip",
    "october": "Take A puff",
    "november": None,
    "december": "You're off for your birthday"
}
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "month": months
    })

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        #HTLM code that returns a list object with anchor tabs/ hyperlinks to the corresponding response data
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        response_data = f"<ul>{list_items}</ul>" #The response data listed on the opening page since index is listed under the blank challenges path
    return HttpResponse(response_data)



def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Come on man!!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])#/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        }) #short hand for the two commented line below
    
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
    except:
        raise Http404()