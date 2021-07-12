from django.shortcuts import render


# Create your views here.
def homepage_view(request):
    return render(request,'demoapp/home.html')

def movie_view(request):
    news1="Hritik Roshan is look like hollywood actor"
    news2="Barun played very good role in asur series"
    news3="street Dancer is popular youth movie of year"
    my_dict={'N1':news1,'N2':news2,'N3':news3}

    return render(request,'demoapp/movie.html',my_dict)

def sports_view(request):
    news1="Every virat lover called virat king Kohali"
    news2="Virat is a run machine of cricket"
    news3="Dhoni is a great indian player"
    news4="Hitman Rohit sharma"
    my_dict={'N1':news1,'N2':news2,'N3':news3,'N4':news4}

    return render(request,'demoapp/sports.html',my_dict)

def Politics_view(request):
    news1="when did narendra modi start working"
    news2="Raj thackare is a great leader"
    news3="nitin gadkari great polition"

    my_dict={'N1':news1,'N2':news2,'N3':news3}

    return render(request,'demoapp/politics.html',my_dict)
