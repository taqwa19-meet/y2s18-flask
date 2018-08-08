from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	#return"gymnastics""
	players = ["cristiano ronaldo", "gareth bale", "Antoine Griezman"]

	return render_template(
		"index.html",
		players=players,
		likes_same_sport=False,
		)


    

if __name__ == '__main__':
   app.run(debug = True)