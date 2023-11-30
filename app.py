# import the Flask library
from flask import Flask, render_template, request
import ranking_function


# Create the Flask instance and pass the Flask constructor the path of the correct module
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def runApp():
	file_name_map, documents, bm25 = ranking_function.startup()
# If method is POST, get the query entered by user
# Use the ranker to get the top 10 documents and render the document names on the webpage
	if request.method == 'POST':
		if(request.form['query'] == ''):
			return "<html><body> <h1>Invalid number</h1></body></html>"
		else:
			# placeholder just multiplies the number for now
			query = request.form['query']
			results = ranking_function.search(query, file_name_map, bm25)
			return render_template('answer.html', 
							result1=results[0],
							result2=results[1],
							result3=results[2],
							result4=results[3],
							result5=results[4],
							result6=results[5],
							result7=results[6],
							result8=results[7],
							result9=results[8],
							result10=results[9])
	# If the method is GET,render the HTML page to the user
	if request.method == 'GET':
		return render_template("home.html")


# Start with flask web app with debug as True only 
# if this is the starting page
if(__name__ == "__main__"):
	app.run(debug=True)
