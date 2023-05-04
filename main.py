# Flask Hello World
from flask import Flask

# Create the application object
app = Flask(__name__)

@app.route("/")
def test():
    return "Test"

# start the development server using the run() method
if __name__ == "__main__":
    app.run()