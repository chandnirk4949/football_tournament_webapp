# Flat Organizational Hierarchy Search

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-3.x-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-5.x-orange.svg)

This Django project allows users to search for employees within a flat organizational hierarchy and retrieve the leftmost/rightmost child of the searched employee.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Search](#search)
- [Database Setup](#database-setup)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Django 3.x installed
- MySQL server installed and configured

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chandnirk4949/flat_organization_hierarchy_search.git

2. Navigate to the project directory:
```bash
cd flat-organizational-hierarchy-search
```

3. Install the project dependencies:
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a '.env' file in the project root directory with the following environment variables:

```bash
    DATABASE_NAME=your-database-name
    DATABASE_USER=your_database_user
    DATABASE_PASS=your_database_password
    DB_PORT=your-port
    ALLOWED_IP=your-allowed-IP
    DATABASE_HOST=your_database_host
```

Replace the placeholders (your_database_name, your_database_user, your_database_password, etc.) with your actual database connection details.

## Usage
### Search
1. Run the Django development server:
```bash
python manage.py runserver
```

2. Access the web application in your browser at 'http://localhost:8000/search_employee/'.

3. Use the search form to search for an employee by name and select the direction (left or right).

4. The application will display the searched employee and the leftmost/rightmost child based on your selection.

## Database Setup
To set up the database and populate it with sample data, follow these steps:

1. Create a MySQL database:
```bash
CREATE DATABASE your_database_name;
```

Replace 'your_database_name' with your desired database name.

2. Update the database settings in settings.py to use the newly created database.

3. Apply migrations and insert data:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the project on GitHub.

2. Create a new branch with a descriptive name for your feature or bug fix.

3. Make your changes and test them thoroughly.

4. Create a pull request with a clear title and description.

5. Wait for your pull request to be reviewed and merged.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Remember to replace the placeholders (`your-username`, `your_database_name`, etc.) with your actual information. This `README.md` provides an overview of your project, instructions for installation and usage, and guidance for contributions. You can further enhance it with project-specific details and documentation as needed. With these additions, users will be informed about the `.env` file and how to set up their database connection details securely.


