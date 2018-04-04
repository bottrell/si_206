# everything that needs to be installed can be
# included in a requirements.txt
# to generate requirements.txt - use:
# pip3 freeze > requirements.txt

# in a new env, call pip install -r requirements.txt
# this will go through requirements file
# in order to install everything via pip

# beep boop

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)

if __name__ == '__main__':
    app.run(debug=True)

# This doesn't work because we never specified what
# the slash directory corresponds to
 
# In name.html we specified the /name/name path, where
# the second name corresponds to the users name

#------JINJA2 Templates ------
{% ... %} #is for control flow
{% if name == "Fred" %}
	<h1> Hi Fred </h1>
{% endif %}
#need to specify end of if/for/func
