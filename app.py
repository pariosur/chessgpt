from flask import Flask, render_template, request, redirect, url_for
from chess_gpt import gpt_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the username from the form
        username = request.form['username']

        # Call the function from your_script_name with the username as an argument
        result = gpt_response(username)

        # Redirect to the response page with the result as a parameter
        return redirect(url_for('response', result=result))

    # If the request method is GET, render the homepage template
    return render_template('index.html')

@app.route('/response')
def response():
    # Get the result from the URL parameter
    result = request.args.get('result')

    # Join the result items into a single string with a space separator
    result = ' '.join(result.split(','))

    # Render the response template with the result
    return render_template('response.html', result=result)

if __name__ == '__main__':
    app.run()
