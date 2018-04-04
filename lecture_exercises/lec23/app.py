from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
	my_list = ['one', 'two', 'three']
	return render_template('list.html', title="Numbers", my_list=my_list)

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)


@app.route('/rhyme/<word>')
def find_rhymes(word):
    base_url = 'https://api.datamuse.com/words'
    params = { 'rel_rhy':word }
    results = requests.get(base_url, params).json()
    rhy_words = []
    for r in results:
        rhy_word = r['word']
        rhy_words.append(rhy_word)
    return render_template('list.html', 
        title="Rhymes with " + word, my_list=rhy_words[:10])

@app.route('/similar/<word>')
def similar_word(word):
	base_url = 'https://api.datamuse.com/words'
	params= {'rel_syn':word}
	results = requests.get(base_url, params).json()
	sim_words = []
	for r in results:
		sim_word = r['word']
		sim_words.append(sim_word)
		return render_template('list.html', 
        title="Similar to " + word, my_list=sim_words[:10])

if __name__ == '__main__':
    app.run(debug=True)