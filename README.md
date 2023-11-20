# Student Registration System

The Student Registration System is a Python application that manages student records within a MySQL database. This system facilitates essential CRUD operations (Create, Read, Update, Delete) on student data efficiently.

## Features

- **Register New Students:** Add new students to the database with their relevant details.
- **View All Students:** Display a comprehensive list of all registered students.
- **Delete Students:** Remove specific students from the database using their unique IDs.
- **Update Student Information:** Modify existing student information such as name, trade, level, and email.

## Setup Instructions

### Prerequisites

- Python 3.x installed
- MySQL database running

### Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/lscblack/Student_Registration_System.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_repository
    ```

3. Configure MySQL Connection:

    - Set up your MySQL database.
    - Create a database named `test`.
    - Import the SQL file (`database.sql`) located in the `db` folder to set up the necessary tables.

4. Update MySQL Connection Details:

    - Configure the MySQL connection details in `connection.py`.

### Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. Choose the desired option from the menu to perform corresponding actions.

## Requirements

- Python 3.x
- MySQL database
- `mysql-connector-python` package (`pip install mysql-connector-python`)
- `prettytable` module (`pip install prettytable`)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


