# task-1
Django project

1. Check for the python availability (python --version)
2. check for pip (pip --version)
3. we need to install django in this folder
    pip install django
4. create a basic project in folder -> 'sample'
    django-admin startproject sample

How to run our django project?
1. move the command to the project
    cd sample
2. write our run command of django to run our project
    python manage.py runserver

We are going to create a basic templates in our django project.
    -> first we need to create a app in our project
        django-admin startapp appname

    we need to create our html file for the webpage
        1. create a new folder with the name 'templates' inside demopage app.
        2. inside that templates folder, create a new file with the name as 'index.html'
        3. fill your html file with codes.
 
   Filling the html file,
        1. type ! symbol and press enter or tab key
            -> used to create the predefined templates for our html page.
        2. fill the html code
 
   we need to insert this html file to our views.py file, then only it will be visible to the users.
        1. create a function named 'home' with 'request' as argument
        def home(request):
        2. create the navigation command, we need to use the function as render function
            render(request,'index.html')
        3. we need to return this function to our manage.py
            return render(request,'index.html')

we need to add our 'demopage' app to our main project
    1. add the app name to our settings.py
        'demopage',
    2. create the url for our app.
        -> go to urls.py
        -> set the path for our new app
            path('name for our page',from where you are going to fetch the html page)
 
        path('',views.home,name='index')
    3 .to import the views.py to urls.py file
        from demopage import views
