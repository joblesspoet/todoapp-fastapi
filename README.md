
#  FastAPI Todo App

  

This is a simple FastAPI project that implements a basic Todo application using an in-memory array to store the todos. It provides REST API endpoints for adding, updating, deleting, and listing todos.



##  Requirements



- Python 3.6+

- FastAPI

- Uvicorn



##  Installation



Clone the repository:

> git clone https://github.com/joblesspoet/todoapp-fastapi.git



2. Navigate to the project directory:

cd todo-app-fastapi



3. Create a virtual environment (optional but recommended):


    python -m venv my_todo_app

  

4. Activate the virtual environment:

	#### On Windows:


    my_todo_app\Scripts\activate
	
	### On macOS and Linux:

    source my_todo_app/bin/activate

5. Install project dependencies:
 
     pip install -r requirements.txt


# Usage


1. Run the FastAPI app using Uvicorn:

    uvicorn main:app --reload


Access the app's API documentation:


Open your web browser and navigate to: http://127.0.0.1:8000/docs


### API Endpoints

     1. GET /todos: Get a list of all todos.
     2. GET /todos/{todo_id}: Get details of a specific todo.
     3. POST /todos: Create a new todo.
     4. PUT /todos/{todo_id}: Update an existing todo.
     5. DELETE /todos/{todo_id}: Delete a todo.



### Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements, feel free to create an issue or submit a pull request.

#### License

This project is licensed under the MIT License - see the LICENSE file for details.