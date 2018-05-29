# Django Blog

### Sections
  * Main Features
  * Steps
  * Resources


## Main Features

## Steps
  1. Before you can add any features to a Python/Django project you must initialize several files, such as the main project and any apps you plan on using
  2. After you have created the app you want to use, make sure to add its ClassConfig(found in the apps.py file to the INSTALLED_APPS list in the settings.py file
  3. Then you want to create the relevant models to your app. Here you can also fill in any relationships for your models.
    The basic workflow for your models will go like this:
    1. Change/Create the model in models.py
    2. Run 'python manage.py makemigrations' to make the basic migrations
    3. Run 'python manage.py migrate' to add the model to your database.
  4. You then need to give Django Admin access to your models, for this blog, the Admin should not be able to change the date of when a Post was made, but they can change the title or body content.
  5. Add the view requests for your models. These include the index(search for all), the standard view, which will show a single object of that class.
  6. Define the URL's for your site, this uses RegExp's to define the wildcards in the url
  7. Once, your URL's are set up, you need the templates for the html they are pointing to. You want to use a template when an html page will vary it's content based on database data.
  8. Finally to run your website use the command "python manage.py runserver"

## Resources
These are the basic tutorials and guides I used while constructing this project. They are included for future reference.
  * [VirtualEnv Tutorial](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
    * To activate this project's virtualenv, run the following:
 $ pipenv shell
  * [Django Blog Tutorial](https://www.djangorocks.com/tutorials/how-to-create-a-basic-blog-in-django/starting-your-application.html)
  * [ManyToManyField Docs](https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/)
  * [Ordering Docs](https://docs.djangoproject.com/en/2.0/ref/models/options/#ordering)
  * [Template Docs](https://docs.djangoproject.com/en/1.7/topics/templates/)
  * [Materialize Docs](https://materializecss.com/getting-started.html)
