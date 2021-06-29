import os

# importing Flask and other modules
from flask import Flask, render_template 

# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods = ["POST", "GET"])
def pizza_recipe():
    return render_template('recipe.html')
if __name__=='__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)