# myWeb Backend

This is the backend repository for myWeb project, built with Django REST Framework.

## Tech Stack
- Framework: Django 5.1.7
- API: Django REST Framework
- Authentication: JWT (djangorestframework-simplejwt)
- Database: MySQL
- Container: Docker
- Cloud Services: AWS Lambda
- Social Authentication: social-auth-app-django

## API Features
- RESTful API endpoints
- JWT Authentication
- Social Login Integration
- CORS Support
- Database Management
- AWS Lambda Functions

## Project Structure
```
myWeb-Backend/
├── api/                 # Main Django project settings
├── persona/            # Persona management
├── resume/             # Resume related functionality
├── static/             # Static files
├── staticfiles/        # Collected static files
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
└── lambda_function.py # AWS Lambda handler
```

## Setup Instructions
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure database settings in `api/settings.py`

3. Run migrations:
```bash
python manage.py migrate
```

4. Start development server:
```bash
python manage.py runserver
```

## Docker Deployment
Build and run with Docker:
```bash
docker build -t myweb-backend .
docker run -p 8000:8000 myweb-backend
```

## Related Projects
- Frontend Repository: https://github.com/peter890176/myWeb-Frontend
- Live Demo: https://myweb-peterli.netlify.app