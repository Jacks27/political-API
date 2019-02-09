Politicov1 involves endpoints to add,edit,delete and update political parties and officess.

Getting Started
Clone the repository by doing: git clone https://github.com/Jacks27/political-API.git

Git checkout develop

Create a virtual environment: virtualenv -p python3 venv

Activate the virtual environment: source env/bin/activate on Linux/Mac or source env/Scripts/activate on windows.

Install the requirements : pip install -r requirements.txt

Prerequisites
python 3.6
virtual environment
Running it on machine
Create a .env file to store your environment variables: touch .venv
In the .venv file add this line: export SECRET=<your-secret-key-here
On terminal do: source .venv
Run the application: python run
The api endpoints can be consumed using postman.
Endpoints
Endpoint	FUNCTIONALITY
POST /api/v1/add_party	CREATE political party
GET /api/v1/get_parties	GET ALL political parties
GET /api/v1/get_party/int:party_id	GET ONE political party
DELETE /api/v1/delete_party	DELETE ONE political party
PATCH /api/v1/update_party/int:party_id	UPDATE ONE political party
POST /api/v1/add_office	CREATE government office
GET /api/v1/get_office/int:office_id	GET ONE government office
GET /api/v1/get_offices	GET ALL government offices
Built With
Flask-Api - The web framework used
Pip - Dependency Management
Authors
Jackson Kariuki
License
This project is licensed under the MIT License
