from flask import Flask, render_template

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


@app.route('/ac-repair')
def ac_repair():
    return render_template('pages/ac_repair.html')


@app.route('/cassette-ac')
def cassette_ac():
    return render_template('pages/cassette_ac.html')


@app.route('/vrf-ac')
def vrf_ac():
    return render_template('pages/vrf_ac.html')


@app.route('/fridge-repair')
def fridge_repair():
    return render_template('pages/fridge_repair.html')


@app.route('/washing-machine')
def washing_machine():
    return render_template('pages/washing_machine.html')


@app.route('/geyser-repair')
def geyser_repair():
    return render_template('pages/geyser_repair.html')


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('pages/privacy_policy.html')


@app.route('/contact')
def contact():
    return render_template('pages/contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

