from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    
    return render(req,'index.html')

def analyse(req):
    analysetxt= ''
    removePunc = req.GET.get('removePunc','off')
    space = req.GET.get('space','off')
    upper = req.GET.get('upper','off')
    txt = req.GET.get('text','default some random text')

    params={'purpose':'Punctuation Remover','analtxt':analysetxt} 
    # dictionary values need to updated completey as 
    # my_dict = {'count': 10, 'name': 'Alice'}
    # Reassigning an immutable value to a key
    # my_dict['count'] = 20  # Changes the value associated with 'count'

    print(removePunc)
    if(removePunc == 'on' or upper == 'on' or space == 'on'):
        if space == "on":
            analysetxt= ''
            for char in txt:
                if char != ' ':
                    analysetxt = analysetxt + char
                else:
                    analysetxt = analysetxt + '_'
            print("space is on")
            txt = analysetxt
            params['analtxt'] = analysetxt

        if removePunc == 'on':
            analysetxt= ''
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&~'''
            for char in txt:
                    if char not in punctuations:
                        analysetxt = analysetxt + char
                    else:
                        analysetxt = analysetxt+'*'
            print("remove is on")
            txt = analysetxt
            params['analtxt'] = analysetxt
        
        if upper == "on":
            analysetxt= ''
            for char in txt:
                analysetxt = analysetxt + char.upper()  
            print("upper is on")
            txt = analysetxt
            params['analtxt'] = analysetxt
        
        return render(req,'analyse.html',params)
    else:
        return HttpResponse('Error not defined check code')
    