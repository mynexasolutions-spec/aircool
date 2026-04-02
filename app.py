from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'aircool-dev-key-change-in-production'


@app.route('/')
def index():
    return render_template('pages/index.html')


@app.route('/services')
def services():
    return render_template('pages/services.html')


@app.route('/cities')
def cities():
    return render_template('pages/cities.html')


@app.route('/about')
def about():
    return render_template('pages/about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # In production: send email / save to DB here
        flash('Thank you! We will call you back within the hour.', 'success')
        return redirect(url_for('contact'))
    return render_template('pages/contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

