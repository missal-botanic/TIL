def hello(request):
    name = "희경",
    tags = ["python", "django", "html", "css"]
    books = ["해변의 카프카", "코스모스", "백설공주", "어린왕자"]


    context = {
        "name" : name,
        "tags" : tags,
        "books" : books,

       
    }
    return render(request, "hello.html", context)