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

- Jenkins can be set up to watch your GitHub repository.
- When you push changes, Jenkins can automatically:
  - Run tests
  - Build your project
  - Deploy your application

### Basic Jenkins Workflow
1. **Set up Jenkins and install the Git plugin.**
2. **Create a new Jenkins job (Pipeline or Freestyle).**
3. **Configure the job to use your GitHub repository URL.**
4. **Set up build triggers (e.g., build on every push).**
5. **Add build steps (test, build, deploy, etc.).**

Now, whenever you push code from any PC, Jenkins will automatically run your configured tasks.

---

For more details, see the official documentation:
- [GitHub Docs](https://docs.github.com/en/get-started/quickstart)
- [Jenkins Docs](https://www.jenkins.io/doc/)
