from flask import Flask,render_template,request

app=Flask(__name__)



@app.route('/')
def homepage():
    return render_template('form.html')


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='get':
        #it is a get method 
        #that means we will get data in form of queries that will append to url
        #based on queries we have to retrieve data from database 
        
        user_name=request.args.get('name')
        email=request.args.get('password')
        password=request.args.get('password')

        return render_template('details.html',name=user_name,email=email)
    
    #that means it is post request
    #we have to create that provided data in database

    user_name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    return render_template('details.html',name=user_name,email=email)


    






if __name__=='__main__':
    app.run(debug=True)

