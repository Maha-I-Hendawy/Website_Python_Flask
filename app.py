from flask import Flask, render_template, url_for



app = Flask(__name__)



@app.route('/')
def home():
	return render_template("home.html")


@app.route('/about')
def about():
	return render_template("about.html", title="About Page")




@app.route('/contactus')
def contactus():
	return render_template("contactus.html", title="Contact Us Page")



if __name__ == '__main__':
	app.run(debug=True)