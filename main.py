from website import create_app #website is a python package because of the __init__.py file inside it. when you import the name of the folder (website), it runs everything in the __init__.py file.

app = create_app()

if __name__=='__main__':
    app.run(debug='True') #this means this line will only be executed if you RUN main.py. debug=True means that everytime we make a change to the python file, it will rerun the web server.

