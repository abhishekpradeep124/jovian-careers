from flask import Flask, render_template

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },  
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs. 12,00,000' 
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'$ 120,000'
  },
  {
    'id':5,
    'title':'DevOps Engineer',
    'location':'New York, USA',
    'salary':'$ 150,000'
  }
]


@app.route('/home')
def hello_world(): 
  return render_template('home.html')

@app.route('/careers')
def careers():
  return render_template('careers.html', jobs=JOBS, company_name='KeyValue')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)