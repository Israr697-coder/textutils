# I have created this file - Dumbheads
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def home(request):
    return HttpResponse('''Home <br> <a href=/removepunc> Go to Remove Punctiuation</a> <br> <a href=/capfirst> Go to Capatlize Leter</a> <br>
     <a href=/newlineremove> Go to New Line REmover</a> <br> <hr>
     <a href=/spaceremove> Go to Space Remover</a> <br>
     <a href=/charcount> Go to Character Count</a> <br>''')


def analyze(request):
    djtext = request.POST.get('text', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')




    if removepunc == "on" and (len(djtext) >7):
        punctuations = ''',.,<>;';[]!?/>.,:;\|}]{['''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                params = {'purpose': 'Removed_punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose': 'Make Capital', 'analyzed_text': analyzed}

        djtext = analyzed

        #render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.strip("/n/n")
            params = {'purpose': 'Remove New line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + " " .join(char.split(" ,"))
            params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (removepunc != "on" and  fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" ):
        return HttpResponse('please Select any option ')

    # else:
    #
    #     return HttpResponse('Please select Removed Punctuations box and enter text')

    return render(request, 'analyze.html', params)

