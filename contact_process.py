from flask import Flask, request, render_template,jsonify,redirect
from datetime import datetime
import mysql.connector
import os
import subprocess
import requests

import signal
sig = getattr(signal, "SIGKILL", signal.SIGTERM)

app = Flask(__name__)
@app.route('/hello', methods=['GET', 'POST'])
def index2():

    mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mahadi#96",
                database="polin_demo_db"
    )
    mycursor = mydb.cursor()
    name = str(request.form['name'])
    email = str(request.form['email'])
    subject = str(request.form['subject'])
    message = str(request.form['message'])
    today = datetime.today()
    TIME = today.strftime("%d-%m-%Y_%H.%M.%S")
    data = "Hi boss.\nYou have a new review\n\nName: "+name+" \nEmail: "+email+" \nSubject: "+subject+" \nMessage: "+message+" \n\nTime: "+TIME
    print(data)
    mycursor = mydb.cursor()
    sql = "INSERT INTO `contact_data` (NAME, email, SUBJECT, message,TIME) VALUES (%s, %s,%s, %s, %s)"
    val = (name, email, subject, message,TIME)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    
    url = f"https://api.telegram.org/bot6144791187:AAHRTw6JoOEAel8G14vPCvMRsbhnhSxPsqw/sendMessage?chat_id=-703960512&text={data}"
    reder_url = f"http://m4h4d1.tech/contact.html"
    reder = requests.get(reder_url)
    print(requests.get(url).json()) # this sends the message
    with open('Templates\\Syslog\\'+'contact_process_'+TIME+'.txt', 'w') as f:
        f.write(data)
    return redirect(reder_url)


@app.route('/log_mod', methods=['GET', 'POST'])
def index():
    mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mahadi#96",
                database="polin_demo_db"
    )
    mycursor = mydb.cursor()
    if request.method == 'POST' and 'Request' in request.form:
        today = datetime.today()
        Request = str(request.form['Request'])
        Response = request.form['Response']
        now = today.strftime("%d-%m-%Y_%H-%M-%S")
        sql = "SELECT gpurl FROM telco_log WHERE msisdn = %s and hittime = %s"
        val = (Request,Response,)
        mycursor.execute(sql, val)
        Log=str(mycursor.fetchone())
        temp_url=Log.split("?")
        url2 = temp_url[0]
        url3 = url2.replace("('", "")
        url = url3.replace("',)", "")
        temp_msisdn=Log.split('msisdn=')[-1]
        msisdn=temp_msisdn.split("&")
        f_msisdn = msisdn[0]
        sql = "SELECT response_time FROM telco_log WHERE msisdn = %s and hittime = %s"
        val = (Request,Response,)
        mycursor.execute(sql, val)
        res1=str(mycursor.fetchone())
        res2 = res1.replace("('", "")
        res_time = res2.replace("',)", "")
        sql = "SELECT finalstatus FROM telco_log WHERE msisdn = %s and hittime = %s"
        val = (Request,Response,)
        mycursor.execute(sql, val)
        stt1=str(mycursor.fetchone())
        ct='Current Time: '+now
        m='msisdn: '+Request
        rq='Request Time: '+Response
        rs='Response Time: ' + res_time
        ru='Request URL: ' + url+"?"
        if stt1 == "('',)":
            fs='Response: Connection Timed out'
        else:
            stt2 = stt1.replace("('", "")
            stat = stt2.replace("',)", "")
            fs='Response: ' + stat
        data = m+'\n'+rq+'\n' + rs +'\n' + ru+'\n'+fs
        with open('Templates\\Syslog\\'+'log_mod_'+now+'.txt', 'w') as f:
            f.write(data)
        list_data = [ct,m,rq,rs,ru,fs]
        return redirect(reder_url)


@app.route('/demo', methods=['GET', 'POST'])
def demo():
    battery = psutil.sensors_battery()

    return x





if __name__ == '__main__':
    app.run(debug=False,host ='0.0.0.0',port='82')
    