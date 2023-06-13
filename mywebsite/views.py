from django.http import HttpResponse
from django.shortcuts import render # it is imported to work with files like html


def index(request):
    return HttpResponse('<h1>Youkoso Otoko no Sekai ye</h1>') #without render



def forms(request):

    data = {'name': 'Jotaro', 'stand' : 'Star Platinum'}


    return render(request,'forms.html', data)

''' so render takes three arguments, one is request
, second is address or link of the page and third is the
 a variable that we can pass, here we have passed a dictionary '''




def data(requests):


    checkbox = requests.GET.get('rmp','OFF')

    #print statements are unnecessary they
    # are only used to prrint to the console
    # print(checkbox)

    checkbox1 = requests.GET.get('count',"OFF")

    checkbox2 = requests.GET.get('upr',"OFF")

    txt = requests.GET.get('txtardata',"Null")
    # print(txt)

    if checkbox == 'on':
        punctuations = """()-[]{}:;"'?/.,><|\*&^%$#@!~`"""

        analysed = ''

        for char in txt:
            if char not in punctuations:
                analysed += char

        datarp = {'purpose': 'Removed Punctuations', 'punc_removed': analysed}

        return render(requests, 'data.html', datarp)



    elif(checkbox1 == 'on'):
        analysed = 0
        b = ' '
        for i in txt:
            if i != b:
                analysed = analysed + 1

        datacount = {'purpose': 'Character Count; White space excluded', 'datacount': 'No. of letters = ',   'char_count': analysed}
        return render(requests, 'data.html', datacount)









    elif(checkbox2 == 'on'):
        a = ''
        for i in txt:
            a = a + i.upper()

        dataup = {'purpose': 'UpperCase ', 'upper': "Up Case : " ,'up_case':a}

        return render(requests,'data.html',dataup)


    else:
        nop = {'purpose': 'No Operation chosen', 'nop': txt}
        return render(requests,'data.html', nop)




