# import the Flask library
from flask import Flask, render_template, request
import os
import io
import ranking_function


# Create the Flask instance and pass the Flask constructor the path of the correct module
app = Flask(__name__)

def generateBlurbs(results):
	slides = "lecture_slides_extractions"
	transcripts = "lecture_transcripts"
	blurblist = []
	for r in results:
		if len(r) > 15:
			#transcript
			fp = os.path.join(transcripts, r)
			in_f = open(fp)
			countline = 0
			curchar = 0
			blurb = ""
			for line in in_f:	
				if countline < 20:
					countline += 1
				else:
					for c in line:
						if curchar < 150:
							curchar+=1
							blurb+= c
			blurblist.append(blurb)
					
					
		else:
			#slide
			fp = os.path.join(slides, r)
			in_f = io.open(fp, encoding='UTF-16')
			countline = 0
			curchar = 0
			blurb = ""
			for line in in_f:	
				if countline < 20:
					countline += 1
				else:
					for c in line:
						if curchar < 150:
							curchar+=1
							blurb+= c
			blurblist.append(blurb)
	return blurblist 


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
			descriptions = generateBlurbs(results)
			return render_template('answer.html', 
							result1=results[0],
							description1 =descriptions[0],
							result2=results[1],
							description2 = descriptions[1],
							result3=results[2],
							description3 = descriptions[2],
							result4=results[3],
							description4 = descriptions[3],
							result5=results[4],
							description5 = descriptions[4],
							result6=results[5],
							description6 = descriptions[5],
							result7=results[6],
							description7 = descriptions[6],
							result8=results[7],
							description8 = descriptions[7],
							result9=results[8],
							description9 = descriptions[8],
							result10=results[9],
							description10 = descriptions[9])
	# If the method is GET,render the HTML page to the user
	if request.method == 'GET':
		return render_template("home.html")


# Start with flask web app with debug as True only 
# if this is the starting page
if(__name__ == "__main__"):
	app.run(debug=True)
