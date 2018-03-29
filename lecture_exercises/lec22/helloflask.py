from flask import Flask
app = Flask(__name__)
    
@app.route('/')
def index():
	html = '<h1>Jordan Bottrell</h1>'
	html += '<p> Hi my name is Jordan and I like to code</p>'
	html +='''<table>
	<tr> 
		<th>Stuff I know</th>
	</tr>
	<tr> 
		<td> How to eat</td> 
	</tr>
	<tr> 
		<td> How to read</td>
	</tr>
	<tr>
		<td> How to type quickly </td>
	</tr>
	</table>'''

	return html

@app.route('/about')
def about():    
    html = '''        
      <h1>About Jordan </h1>        
      <p> Jordan knows more stuff than the average toddler </p>      
      <a href='/'> Go back home </a>    
      '''    
    return html

ctr = 0
@app.route('/')
def counter():    
  global ctr    
  ctr += 1    
  return '<p> This site has been visited: </p> <h3>' + str(ctr) + '</h3>'

if __name__ == '__main__':
	print('starting Flask app', app.name)
	app.run(debug=True)
