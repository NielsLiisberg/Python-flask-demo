# IBM i -Python flask demo
This microservice example are using Db2  and Flask, and gives the simple setup  

# Setup the environment

I always you bash as my default shell. You can set that once and for all from ACS Run SQL script with: 
```
CALL QSYS2.SET_PASE_SHELL_INFO('\*CURRENT', '/QOpenSys/pkgs/bin/bash');   
```

On IBM i you will need the open source in you path (and a nice prompt). So if you don't have a .profile yet, then:
```
ssh myibmi
echo 'PATH=/QOpenSys/pkgs/bin:$PATH' >> $HOME/.profile
echo 'PS1="\h-\$PWD:\n"' >> $HOME/.profile
exit 
```

For the shell you can aslo Click SSH Terminal in ACS or use a terminal like putty 

(or you can even use call qp2term – but I suggest that you get use to ssh)

From the terminal we need to install some open source tooling:

```
ssh myibmi
yum install git
```
And now in the same ssh session - clone the demo repo 
```
mkdir /prj
cd  /prj
git -c http.sslVerify=false clone https://github.com/NielsLiisberg/Python-flask-demo.git
```

This demo requires Python3 and the Flask framework
```
yum install python3-pip
pip3 install --upgrade pip

pip3 install virtualenv
pip3 install Flask
```
You can now test if the Python / Flask environment with the folloing application  

```
# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask 

# Flask constructor takes the name of 
# current module (__name__) as argument. 
app = Flask(__name__) 

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
@app.route('/') 
# ‘/’ URL is bound with hello_world() function. 
def hello_world(): 
  return 'Hello World'

# main driver function 
if __name__ == '__main__': 

  # run() method of Flask class runs the application 
  # on the local development server. 
  app.run(host='0.0.0.0')

```
You start the application 

```
ssh MyIbmI
python3 flasktest.py
```
Now open you browser:
```
http://myibmi:5000
```
If that says "hello world" - then you are golden. 
Stop the application from the ssh by CTRL-C
and we are ready for next step: Install  the database:

Open ACS -> Run SQL script

copy/paste or open the **demo.sql** file, and run each step. When the database is ready, jump back to your ssh session:

Now you can try the Db2 microservice 
```
python3 flaskdb2.py
```
You have two end points:
```
http://myibmi:5000/list_users_by_proc
http://myibmi:5000/list_users_by_view
```

... It is that easy

