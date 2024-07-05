from website import create_app

app = create_app()

if __name__ == '__main__':  #if main.py was imported from another file, and this line didn't exist then it would sitll run the webs server (wchich should only be ran if it was run directly by this file)
  app.run(debug=True)   #w this we dont havr to keep manually running the flask web server

