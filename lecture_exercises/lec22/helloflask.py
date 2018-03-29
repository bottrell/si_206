from flask import Flask
app = Flask(__name__)
    
@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/about')
def about():    
    html = '''        
      <h1>About this Site </h1>        
      <p> This is my first ever Flask website! </p>      
      <a href='/'> Go back home </a>    
      '''    
    return html

ctr = 0
@app.route('/counter')
def counter():    
  global ctr    
  ctr += 1    
  return '<h3>' + str(ctr) + '</h3>'

if __name__ == '__main__':
	print('starting Flask app', app.name)
	app.run(debug=True)
