#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from book.models import Book

def search_form(request):
    return render_to_response('search_form.html')
# Create your views here.
def search(request):
    error = False
    if 'q' in request.GET :
        q = request.GET['q']
        if not q:
            error = True
            return render_to_response('search_form.html',{'error': error})
        else:
            query_list = Book.objects.filter(AuthorID__icontains=q)
            if not query_list:
                return render_to_response('search_form.html',{'error': error})
            else:
                return render_to_response ('search_results_.html',{'query_list':query_list})
    else:
        error = True
        return render_to_response('search_form.html', {'error': error})
def view_all(request):
    all_objects = Book.objects.all()
    return render_to_response('view_all.html',{'all_objects':all_objects})

def post(request):
    if request.GET:
        l = request.GET
        ADD = Book(Title=l['Title'],
                             ISBN=l['ISBN'],
                             AuthorID=l['AuthorID'],
                             Publisher=l['Publisher'],
                             PublishDate=l['PublishDate'],
                             Price=l['Price'])
        ADD.save()
        return render_to_response('choose.html',{'right':True})
    else:
        return render_to_response('post1.html',{'right':True})
        
def delete(request):
    id1 = request.GET["id"] 
    Book.objects.filter(Title__icontains=id1).delete()
    all_objects = Book.objects.all()
    return render_to_response('view_all.html',{'all_objects':all_objects})


flag=True
def change(request):
    global flag,book
    if flag:
        id1 = request.GET["id"]
        book = Book.objects.get(Title__icontains=id1)
        flag=False
        return render_to_response('change1.html',{'people':book})
    else:
        l = request.GET
        book.Title = l['Title']
        book.ISBN=l['ISBN']
        book.AuthorID=l['AuthorID']
        book.Publisher=l['Publisher']
        book.PublishDate=l['PublishDate']
        book.Price=l['Price']
        book.save()
        flag=True
        return render_to_response('choose.html',{'right':True}) 