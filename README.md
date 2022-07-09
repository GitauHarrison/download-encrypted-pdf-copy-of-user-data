# Encrypt Downloaded Copy of Users Data Using Python and Flask

Encryption is a key security feature that prevents unauthorized access to personal data. This project highlights how a user of an application can download their data and encrypt it.


![Encrypted pdf](app/static/images/password_protected_pdf.gif)


## Technologies Used

- Flask
- Python for programming
- Flask SQLAlchemy and Flask Migrate (for database management)
- Faker for generating fake data
- FPDF for generating PDFs
- PyPDF2 for encrypting PDFs
- Grid.js for table generation


## Features

- Generation of PDF file 
- Encryption of PDF file
- Autogeneration of users data


## Contributors

[![GitHub Contributors](https://img.shields.io/github/contributors/GitauHarrison/download-encrypted-pdf-copy-of-user-data)](https://github.com/GitauHarrison/download-encrypted-pdf-copy-of-user-data/graphs/contributors)


## Testing the Application Locally

1. Clone this repository

```python
git clone git@github.com:GitauHarrison/download-encrypted-pdf-copy-of-user-data.git
```

2. Go to the directory

```python
$ cd download-encrypted-pdf-copy-of-user-data
```

3. Create and activate a virtual environment

```python
$ mkvirtualenv venv
```

4. Install project dependancies

```python
(venv)$ pip3 install -r requirements.txt
```

5. Run the application

```python
(venv) flask run
```

6. Open the browser and navigate to http://localhost:5000/

## Learning

If you are curious about this feature, learn how you can incorporate it in your next flask application [here](https://github.com/GitauHarrison/notes/blob/master/download_encrypted_pdf.md).