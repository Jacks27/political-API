

# Politico-API <a href="https://codeclimate.com/github/codeclimate/codeclimate/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage" /></a> <a href="https://codeclimate.com/github/codeclimate/codeclimate/maintainability"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" /></a>
Politico enables citizens to vote for candidates in different offices of the governmant.

## Getting Started

1) Clone the repository by doing: `git clone https://github.com/Jacks27/political-API`

2) Create a virtual environment: `virtualenv env`

3) Activate the virtual environment: `source venv/bin/activate` on Linux/Mac  or `source venv/Scripts/activate` on `workon venv`.

4) Install the requirements : `pip install -r requirements.txt`


## Running tests
Use pytest to run: `pytest --cov=app` 

### Prerequisites
-   python 3.6
-   virtual environment


## Running it on machine
- Create a .env file to store your environment variables: `touch .venv`
- In the `.venv` file add this line: `export SECRET=<your-secret-key-here`
- On terminal do: `source .venv`
- Run the application: `python run`
- The api endpoints can be consumed using postman.

## Endpoints
| Endpoint                                   | FUNCTIONALITY                      |
| ----------------------------------------   |:----------------------------------:|
| POST  /api/v1/party                        | CREATE political party             |
| GET  /api/v1/party                         | GET ALL political parties          |
| GET  /api/v1/party/<int:party_id>          | GET ONE political party            |
| DELETE  /api/v1/party                      | DELETE ONE political party         |
| PATCH /api/v1/party/<int:party_id>         | UPDATE ONE political party         |
| POST  /api/v1/office                       | CREATE government office           |
| GET  /api/v1/office/<int:office_id>        | GET ONE government office          |
| GET  /api/v1/office                        | GET ALL government offices         |

# Heroku host

## Built With
* [Flask-Api](http://flask.pocoo.org/docs/1.0/api/) -  The web framework used
* [Pip](https://pypi.python.org/pypi/pip) -  Dependency Management

## Authors
* **Jackson Kariuki** 

## License

This project is licensed under the MIT License
