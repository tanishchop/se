# How to Work with This Project on Multiple PCs and Use Jenkins

## Using GitHub to Sync Your Code

1. **Clone the Repository on Another PC**
   - Open a terminal or Git Bash.
   - Run:
     ```sh
     git clone https://github.com/tanishchop/se.git
     cd se
     ```

2. **Make Changes**
   - Edit files as needed.

3. **Save and Upload Your Changes**
   - Stage and commit your changes:
     ```sh
     git add .
     git commit -m "Describe your changes"
     ```
   - Push your changes to GitHub:
     ```sh
     git push
     ```

4. **Pull Latest Changes Before Working**
   - Always run this before starting work to get the latest code:
     ```sh
     git pull
     ```

## Using Jenkins for Automation

  - Run tests
  - Build your project
  - Deploy your application

## How to Install and Run Jenkins on Windows

1. **Download Jenkins**
  - Go to https://www.jenkins.io/download/ and download the latest LTS "Generic Java package (.war)" file.

2. **Make Sure Java is Installed**
  - Jenkins requires Java (JDK or JRE 8 or newer). You can check by running:
    ```powershell
    java -version
    ```
  - If Java is not installed, download and install it from https://adoptium.net/ or https://www.oracle.com/java/technologies/downloads/.

3. **Run Jenkins**
  - Open PowerShell and navigate to the folder where you downloaded `jenkins.war`.
  - Run:
    ```powershell
    java -jar jenkins.war
    ```
  - Wait for Jenkins to start. When ready, open your browser and go to:
    http://localhost:8080

4. **Unlock Jenkins**
  - Jenkins will ask for an initial admin password.
  - The setup page will show the file path (usually `C:\Users\yourname\.jenkins\secrets\initialAdminPassword`).
  - Open that file, copy the password, and paste it into Jenkins.

5. **Finish Setup**
  - Follow the on-screen instructions to install recommended plugins and create your admin user.

Jenkins is now ready to use!

### Basic Jenkins Workflow
1. **Set up Jenkins and install the Git plugin.**
2. **Create a new Jenkins job (Pipeline or Freestyle).**
3. **Configure the job to use your GitHub repository URL.**
4. **Set up build triggers (e.g., build on every push).**
5. **Add build steps (test, build, deploy, etc.).**

### To add file to git

Now, whenever you push code from any PC, Jenkins will automatically run your configured tasks.


For more details, see the official documentation:
