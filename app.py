from flask import Flask, render_template
from serpapi import GoogleSearch

app = Flask(__name__)

@app.route('/')
def index():
    # Perform the Google Lens search
    params = {
      "api_key": "21ead71b458d051c367a569ed84627ed80300e1a006d88582330eaacf8c48c99",
      "engine": "google_lens",
      "url": "https://www.decornation.in/wp-content/uploads/2020/07/modern-dining-table-chairs-800x800.jpg",
             "country": "in"

    }
    search = GoogleSearch(params)
    results = search.get_dict()

    # Render the HTML template with the search results
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
