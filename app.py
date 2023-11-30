# import the Flask library
from flask import Flask, render_template, request


# Create the Flask instance and pass the Flask constructor the path of the correct module
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def squarenumber():
# If method is POST, get the query entered by user
# Use the ranker to get the top 10 documents and render the document names on the webpage
	if request.method == 'POST':
		if(request.form['query'] == ''):
			return "<html><body> <h1>Invalid number</h1></body></html>"
		else:
			# placeholder just multiplies the number for now
			number = request.form['query']
			sq = int(number) * int(number)
			return render_template('answer.html', 
							squareofnum=sq)
	# If the method is GET,render the HTML page to the user
	if request.method == 'GET':
		return render_template("home.html")


# Start with flask web app with debug as True only 
# if this is the starting page
if(__name__ == "__main__"):
	app.run(debug=True)
