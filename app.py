from flask import Flask

app = Flask(__name__)

def create_x_array(x: int) -> list:
    return [i for i in range(x)]


@app.route("/run-model")
def run_model():
    print("Heyy")
    return "Running model"



@app.route('/')
def main():
    x = 10_000_000
    x_array = create_x_array(x)
    print(x_array)
    
    return '<h1>Hello Data Team</h1>'
    
    
if __name__ == '__main__':
    app.run(debug=True)