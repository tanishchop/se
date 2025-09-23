# College Event Management System

## DevOps Tools Used: Git & Jenkins

This project demonstrates the use of two DevOps tools:

**Git**: Used for version control. All source code changes are tracked, committed, and pushed to a remote repository. Collaboration and code history are managed using Git commands (`add`, `commit`, `push`, etc.).

**Jenkins**: Used for Continuous Integration/Continuous Deployment (CI/CD). The included `Jenkinsfile` automates the build, test, and deployment pipeline. Jenkins pulls the latest code from Git, installs dependencies, runs migrations and tests, and can deploy the application automatically. This ensures code quality and streamlines deployment.

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

## Jenkins CI/CD Setup

This setup assumes you have Jenkins installed and a Git repository hosted (e.g., GitHub).

1. **Install Jenkins Plugins**:
   - Git Plugin
   - Pipeline Plugin
   - Django Plugin (optional)
   - Warnings Next Generation (for reports)

2. **Create Jenkinsfile** in the project root (add this file to your repo):
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Checkout') {
               steps {
                   git branch: 'main', url: '<your-repo-url>'
               }
           }
           stage('Install Dependencies') {
               steps {
                   bat 'venv\Scripts\activate && pip install -r requirements.txt'
               }
           }
           stage('Run Migrations') {
               steps {
                   bat 'venv\Scripts\activate && python manage.py migrate'
               }
           }
           stage('Run Tests') {
               steps {
                   bat 'venv\Scripts\activate && python manage.py test'
               }
           }
           stage('Deploy') {
               steps {
                   // Add deployment steps, e.g., copy to server, restart service
                   echo 'Deployment successful'
               }
           }
       }
       post {
           always {
               bat 'venv\Scripts\activate && python manage.py collectstatic --noinput'
           }
       }
   }
   ```
   (Adjust for Linux/macOS with `sh` instead of `bat` if needed.)

3. **Configure Jenkins Job**:
   - Create a new Pipeline job.
   - Set Repository URL to your Git repo.
   - Script Path: `Jenkinsfile`.
   - Trigger on push to main branch.

4. **Deployment**: Customize the 'Deploy' stage for your hosting (e.g., Heroku, VPS). Ensure environment variables for secrets.

## Additional Notes
- CSRF protection and form validation are integrated via Django forms.
- For production, use a proper database (e.g., PostgreSQL) and set `DEBUG = False` in settings.py.
- Tests are basic; expand in `events/tests.py` as needed.

Contact for issues!