
Career Pathways Recommendation System
A Machine Learning–Based Career Pathways Recommendation System for Junior Secondary School Learners
1. Project Overview
The Career Pathways Recommendation System is a web-based application designed to support career pathway selection among Junior Secondary School (JSS) learners in Kenya.
The system integrates Machine Learning with web development to analyze learners' academic performance, project performance, and co-curricular participation to recommend a suitable career pathway.
The application is built using Python and Django, with a trained Random Forest classification model used to generate recommendations. It is intended to support evidence-based decision-making in career guidance within the Competency-Based Curriculum (CBC) framework.
The system considers three major career pathways:
STEM: Science, Technology, Engineering and Mathematics.
Social Sciences: Pathways associated with social sciences and related fields.
Arts and Sports Science: Pathways associated with creative arts, music, drama, sports and related fields.
The system is designed to assist learners, teachers and other education stakeholders in making more informed pathway decisions.
2. Objectives
The project aims to:
Develop a Machine Learning model for recommending suitable career pathways for JSS learners.
Identify the academic and co-curricular factors that contribute to career pathway recommendations.
Integrate the trained Machine Learning model into a web-based recommendation system.
Provide a platform for individual and batch learner pathway recommendations.
3. Key Features
3.1 Individual Learner Recommendations
The system allows users to enter learner information and obtain a recommended career pathway based on the trained Machine Learning model.
3.2 Teacher Dashboard
The application provides teacher-oriented functionality to support access to pathway recommendation services.
3.3 Batch Predictions
Teachers can upload learner records using supported CSV or Excel files to generate recommendations for multiple learners.
3.4 Machine Learning Integration
The application integrates a trained Random Forest model to classify learners into the supported career pathway categories.
3.5 Academic and Co-Curricular Factors
The model uses learner information such as academic marks, project performance and participation in selected co-curricular activities.
3.6 Report Generation
The application is designed to support the presentation of pathway recommendations and the generation of reports for learner records.
3.7 Authentication and Administration
Django's authentication and administration capabilities support user access and administrative management.
4. Technology Stack
Component
Technology
Programming language
Python
Web framework
Django
Machine Learning
Scikit-learn
Classification algorithm
Random Forest
Data processing
Pandas and NumPy
Model persistence
Pickle
Frontend
HTML, CSS, Bootstrap and JavaScript, where implemented
Database
SQLite for local development; PostgreSQL for production configuration
Database configuration
dj-database-url and psycopg2-binary
Deployment platform
Vercel
Production database hosting
Neon PostgreSQL
Version control
Git and GitHub
5. System Architecture
The system follows a web-based Machine Learning architecture.
The general workflow is:
A user accesses the web application.
The user provides learner information or uploads a supported dataset.
The application validates the supplied information.
The learner data is prepared in the format expected by the trained model.
The Random Forest model processes the input and generates a pathway prediction.
The application presents the recommended pathway.
Where applicable, the application produces results for multiple learners.
The prediction workflow can be represented as:
Learner Records → Data Validation → Feature Preparation → Random Forest Model → Pathway Classification → Results and Reports
6. Machine Learning Model
The system uses a trained Random Forest classification model saved as randomforest_model.pkl.
The model receives selected learner attributes, including academic performance, project-related variables, co-curricular participation and school type.
The input features used by the model include:
Gender
Mathematics
English
Kiswahili
Integrated Science
Pre-Technical Studies
Agriculture
Christian Religious Education (CRE)
Creative Arts
Social Studies
Science project performance
Creative Arts project performance
Agriculture project performance
Scouts or related participation
Music and drama participation
Sports participation
School type
The model uses these features to produce a recommendation among the supported pathway classes.
Important: The model's input columns must match the feature names and order used during training. The uploaded dataset must also contain the required learner-identification column when generating reports that include learner names.
The recommendations are intended to support career guidance. They should not be treated as a substitute for professional guidance, learner preferences, parental involvement or applicable education placement requirements.
7. Project Structure
The repository is organized around a Django project.
CAREER-PATHWAYS-SYSTEM/
│
├── schoolpathway/
│   ├── manage.py
│   ├── randomforest_model.pkl
│   ├── accounts/
│   ├── predictor/
│   ├── teacher/
│   │
│   └── schoolpathway/
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── asgi.py
│
├── requirements.txt
├── README.md
└── .gitignore
The structure above illustrates the main application components. Additional files may exist in the repository.
Main Components
accounts: User accounts, authentication and related pages.
predictor: Learner pathway prediction functionality.
teacher: Teacher-oriented functionality, including batch processing.
schoolpathway: Django project configuration and URL routing.
randomforest_model.pkl: Serialized Machine Learning model.
requirements.txt: Python dependencies.
8. Installation and Setup
Prerequisites
Install the following:
Python 3.12 or another Python version supported by the project's dependencies.
pip.
Git.
A code editor such as Visual Studio Code.
Step 1: Clone the Repository
git clone https://github.com/WAMALWA-debug/CAREER-PATHWAYS-SYSTEM.git
Navigate to the project directory:
cd CAREER-PATHWAYS-SYSTEM
Step 2: Create a Virtual Environment
python -m venv venv
Activate the environment on Windows:
venv\Scripts\activate
On Linux or macOS:
source venv/bin/activate
Step 3: Install Dependencies
From the repository root, run:
pip install -r requirements.txt
Step 4: Navigate to the Django Application
cd schoolpathway
Step 5: Configure Environment Variables
Create a .env file in the appropriate project directory if your local configuration uses environment variables.
For PostgreSQL, configure a DATABASE_URL containing your database connection string.
For example:
DATABASE_URL=your_postgresql_connection_string
Replace the placeholder with your actual connection string. Do not commit database credentials or secret keys to GitHub.
If using SQLite locally, configure Django to use the local SQLite database.
Step 6: Apply Database Migrations
python manage.py migrate
Step 7: Create an Administrator Account
python manage.py createsuperuser
Follow the prompts to configure the administrator username, email and password.
Step 8: Start the Development Server
python manage.py runserver
Open the local application in your browser:
http://127.0.0.1:8000/
The Django administration interface is available at:
http://127.0.0.1:8000/admin/
These instructions assume the repository's dependencies, environment variables and model file are correctly configured.
9. Batch Dataset Requirements
For batch predictions, prepare a CSV or Excel file with the column names expected by the application.
The expected column names are:
NAME
GENDER
MATH
ENG
KISW
INT. SCI
PRE.TECH
AGRI
CRE
C/A
SST
SCI_PROJ
CREA_PROJ
AGR_PROJ
PRE&SCOUT
MUSIC&DRAMA
SPORTS
SCH. TYPE
Dataset Guidelines
Use the exact column names expected by the application.
Include all required columns.
Ensure marks are numeric and fall within the validation range configured by the application.
Use consistent values for categorical fields.
Avoid missing values in required fields.
Save the file in CSV or Excel format supported by the application.
The NAME column identifies learners in the results; it is not necessarily a feature used by the trained model.
The precise accepted values for categorical variables must match the preprocessing rules implemented in the application.
10. Deployment
The project is configured for deployment using Vercel, with Neon PostgreSQL intended for production database storage.
The deployment requires:
A valid Vercel project configuration.
The correct Django project root directory.
All required Python dependencies.
The trained Random Forest model file.
Correct production environment variables.
A valid PostgreSQL connection string.
Database migrations applied to the production database.
Proper handling of Django static files.
Production credentials must be configured through environment variables rather than committed to the repository.
The production deployment should also use an appropriate Django secret key, DEBUG=False, restricted allowed hosts and secure cookie settings.
11. Security and Data Privacy
The system processes learner information, which may include academic performance and personal identifiers.
Users deploying or operating the system should:
Protect learner records from unauthorized access.
Store passwords using Django's authentication mechanisms.
Keep database credentials and secret keys private.
Restrict access according to user roles.
Use HTTPS in production.
Avoid publishing identifiable learner records in public repositories.
Follow applicable Kenyan data protection requirements.
12. Future Improvements
Potential improvements include:
More comprehensive model evaluation and validation.
Explainable Machine Learning to clarify factors influencing recommendations.
Improved learner result dashboards.
Additional reporting and analytics.
Enhanced accessibility and mobile responsiveness.
Further validation using new learner records.
Monitoring model performance and fairness across learner groups.
13. Intended Users
The system is intended to support:
Junior Secondary School learners.
Teachers and career guidance personnel.
School administrators.
Education researchers.
Other stakeholders involved in learner pathway guidance.
14. Project Status
The project combines Django web application development with a trained Random Forest model for career pathway recommendations.
Deployment, static-file delivery, database connectivity and user authentication should be tested in the target environment before the application is considered production-ready.
15. Author and Repository
Project: Career Pathways Recommendation System
Repository: https://github.com/WAMALWA-debug/CAREER-PATHWAYS-SYSTEM
Deployment: https://career-pathways-system.vercel.app/
Primary technologies: Python, Django and Machine Learning.
Important: one issue I noticed in your current GitHub code
While reviewing the repository, I found that the published settings.py still appears to contain some configuration problems:
The database condition uses DATABSE_URL instead of DATABASE_URL.
DEBUG is set to True.
The Django secret key is exposed in the public repository.
The displayed settings do not yet show the WhiteNoise middleware configuration discussed earlier. �
GitHub
These issues should be fixed before you describe the deployment as production-ready. Since the secret key has been published, generate a new one and store it securely as an environment variable.
How to add the README to GitHub
Open your GitHub repository⁠�.
Click Add file → Create new file.
Enter README.md as the filename in the repository's root directory.
Copy the README above into the editor.
Click Commit changes.
GitHub will then display the README on your repository's front page.
One recommendation: Because this is also your research implementation, keep the README focused on the system's purpose, architecture, model inputs, setup and limitations. Avoid claiming that the model is clinically or educationally validated unless you have documented validation results to support that claim.
