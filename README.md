# College Event Management System


## DevOps Tools Used: Git & Docker

This project demonstrates the use of two DevOps tools:

**Git**: Used for version control. All source code changes are tracked, committed, and pushed to a remote repository. Collaboration and code history are managed using Git commands (`add`, `commit`, `push`, etc.).

**Docker**: Used for containerization. Docker packages the application and its dependencies into a single container, ensuring consistent setup and deployment across different environments.

See below for setup details for both tools.

This is a Django-based web application for managing college events, including organizers, events, and schedules. It features a desktop-focused frontend with HTML/CSS/JS, user authentication, and an admin panel.

## Local Setup and Run Steps

1. **Clone the Repository** (if not already local):
   ```bash
git clone <repository-url>
   cd <project-directory>
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser for Admin**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000/`.
   - Events list: `http://127.0.0.1:8000/events/`
   - Admin panel: `http://127.0.0.1:8000/admin/`
   - Login: `http://127.0.0.1:8000/accounts/login/`

## Features
- **Backend**: Django models for Users, Organizers, Events, and Schedules with relationships.
- **Frontend**: Pure HTML/CSS/JS with card layouts, modals for schedule CRUD via AJAX, animations, and desktop UI.
- **Authentication**: Login required for schedule management; only organizers can add/edit/delete schedules.
- **Admin Panel**: Full Django admin for managing all entities.
- **Database**: SQLite (default).

## Git Version Control

The project is already initialized with Git. To use it:

1. **Add Remote Origin** (if pushing to a remote repo):
   ```bash
   git remote add origin <your-repo-url>
   git branch -M main
   git push -u origin main
   ```

2. **Make Changes and Commit**:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push
   ```


## Docker Setup

### What is Docker?

Docker is a platform that allows you to package your application and its dependencies into a single container. This container can run on any system with Docker installed, ensuring consistency across different environments.

### Use of Docker in This Project

In this project, Docker is used to:
- Simplify setup and deployment by packaging the Django app and its dependencies.
- Ensure the application runs the same way on any computer or server.
- Make it easy to share, test, and deploy the project without manual installation of Python or dependencies.

With Docker, you can build and run the app using just a few commands, without worrying about environment issues.

### How to Use Docker

1. **Build the Docker image**
   ```bash
   docker build -t se-app .
   ```

2. **Run the Docker container**
   ```bash
   docker run -p 8000:8000 se-app
   ```

This will start the Django development server inside the container, accessible at `http://localhost:8000`.

## Additional Notes
- CSRF protection and form validation are integrated via Django forms.
- For production, use a proper database (e.g., PostgreSQL) and set `DEBUG = False` in settings.py.
- Tests are basic; expand in `events/tests.py` as needed.

Contact for issues!