from utils.mailSender import mailSender
from flask import Flask, request, abort, url_for, redirect, render_template
import json, time, threading, datetime

class Application:
    def __init__(self):
        self.loadConfig()
        self.app = Flask(__name__)

        # Rotas da API
        @self.app.route('/', methods=['GET','POST'])
        def root():
            return redirect(url_for('.home'))

        @self.app.route('/home', methods=['GET'])
        def home():
            return render_template('home.html')

        @self.app.route('/help', methods=['GET','POST'])
        def help():
            return render_template('help.html')

        @self.app.route('/mail', methods=['GET','POST'])
        def mail():
            if request.method == 'POST':
                # Exemplo de utilização de thread
                # newthread = threading.Thread(target=self.notify, args=([self.loadTemplate('email'),request.form['addr'],'{{cookiecutter.api_name}} | EMAIL TESTE']))
                # newthread.start()
                try:
                    template = self.loadTemplate('email')
                    template = template.replace("!!TITULO!!",'{{cookiecutter.api_name}} | EMAIL TESTE')
                    template = template.replace("!!CORPO!!","Esse é um email de teste!")
                    self.notify(template,request.form['email'],"{{cookiecutter.api_name}} | EMAIL TESTE")
                except Exception as e:
                    errorcode, errortext = e.args
                    return render_template('error.html', error = 'Error {}: {}'.format(errorcode,errortext.decode("utf-8")))
                return render_template('success.html')
            else:
                return render_template('mail.html')
        pass

    def loadConfig(self):
        try:
            self.configuration = json.loads(open('config.json','r').read())
        except Exception as e:
            print(e)
            exit(1)
        pass

    def loadTemplate(self,name):
        template = open('templates/'+name+'_template.html','r').read()
        return template

    def notify(self,template,recipient,title):
        mailsender = mailSender(self.configuration["gmail"])
        mailsender.setBody(template)
        mailsender.setSubject(title)
        mailsender.sendEmail(recipient)
        pass

    def run(self):
        self.app.run(host='0.0.0.0')
        pass    