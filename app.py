from flask import Flask, render_template, request, url_for, redirect, flash



app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')



@app.route('/')
def home():
	return render_template("home.html")


@app.route('/about')
def about():
	return render_template("about.html", title="About Page")




@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		msg = request.form.get('msg')
		print(f"Message: {msg}, From: {name} with Email: {email}")
		flash("Your message has been sent.")
		return redirect(request.url)

	return render_template("contactus.html", title="Contact Us Page")



