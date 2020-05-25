Hi guys,

This is an implementation of Graphql using Ariadne, and Flask with for wsgi, and that can be hosted on heroku.

Graphql consults via query, github users. Lists user repositories, and also queries that user's information.

For local execution, 
basically you just need to create your "venv" and run "pip install -r requirements.txt"

To run on heroku, 
pay attention to "Procfile",
because if you change the script app of the flask it is necessary to change the name of the script in "Procfile" too,
as it is what heroku reads to execute.

Next steps are to create mutations to use the API's Auth and create repositories, via mutation.

It is also necessary to warn that, 
due to the api_github usage guidelines, 
we have a limit of 60 requests without authentication, 
so the next steps are to implement this and have numerous requests.
In this sense, I used try, to generalize errors in requests

and here's the implementation on heroku, https://flask-ariadne-graphql.herokuapp.com/graphql
