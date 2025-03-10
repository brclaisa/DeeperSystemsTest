# Flask MongoDB Application

This project is a simple web application built using Flask and MongoDB. It demonstrates how to set up a Flask application with MongoDB as the database using Flask-PyMongo.

## Project Structure

```
flask-mongo-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates
│       └── index.html
├── config.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd flask-mongo-app
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

5. Set up your MongoDB database and update the `config.py` file with your MongoDB URI.

## Usage

1. Run the application:

   ```
   flask run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.