from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def resume(request):
    # 獲取當前主機
    host = request.get_host()
    protocol = 'https' if request.is_secure() else 'http'
    base_url = f"{protocol}://{host}"
    
    data = {
        "name": "Yue Wen Peter Li" ,
        "job": "Computer Science Graduate Student",
        "about": "Born in Seattle, raised in Taiwan, and currently based in Boston. A programmer who loves coffee, cats, memes, and trading.",
        "email": "li.yuew@northeastern.edu",
        "linkedin": "https://www.linkedin.com/in/peter-li-97081429a/",
        "github": "https://github.com/peter890176",
        "profileImage": f"{base_url}/static/images/profile.jpg",
        "portfolio": [
            {
                "title": "Foundation Of Software Development",
                "description": "Mock Stake Overflow",
                "technologies": ["Java", "Spring Boot", "React"],
                "image": f"{base_url}/static/images/project1.jpg",
                "link": "#"
            },
            {
                "title": "Programming Design Paradigm",
                "description": "Image processing application in Java",
                "technologies": ["Java", "OOP", "Design Patterns"],
                "image": f"{base_url}/static/images/project2.jpg",
                "link": "#"
            },
            {
                "title": "Little Lemon Restaurant",
                "description": "Booking and Cart functionality",
                "technologies": ["React", "JavaScript", "CSS"],
                "image": f"{base_url}/static/images/project3.jpg",
                "link": "#"
            }
        ],
        "certificates": [
            {
                "name": "Meta Back-End Developer",
                "issuer": "Meta on Coursera",
                "date": "March 13, 2025",
                "link": "https://coursera.org/share/3775c11d21d5f9220992dc6a7901991e"
            },
            {
                "name": "Meta Front-End Developer",
                "issuer": "Meta on Coursera",
                "date": "September 15, 2024",
                "link": "https://coursera.org/share/009e810073c5ba4fbc0e6469a02b70d3"
            },
            {
                "name": "Google Data Analytics",
                "issuer": "Google on Coursera",
                "date": "September 16, 2021",
                "link": "https://coursera.org/share/3d166611be9d9714f28b16980b6295b6"
            }
        ],
        "education": [
            {
                "institution": "Northeastern University, Boston, MA",
                "department": "Khoury College of Computer Sciences",
                "degree": "Master of Science in Computer Science (General track)",
                "period": "Sep 2023 - Present",
                "expected": "Expected graduation: April 2025",
                "gpa": "GPA: 3.8/4.0"
            },
            {
                "institution": "National Yang Ming Chiao Tung University, Taipei, Taiwan",
                "degree": "Master of Science in Health and Welfare Policy",
                "period": "Sep 2019 - Jan 2023",
                "gpa": "GPA: 4.1/4.3"
            },
            {
                "institution": "Fu-Jen Catholic University, Taipei, Taiwan",
                "degree": "B.A. in Sociology & B.S. in Psychology (Double Degree)",
                "period": "Sep 2014 - Jun 2018",
                "gpa": "GPA: 3.8/4.0"
            }
        ],
        "skills": [
            "Python", "Java", "C++",
            "HTML", "CSS", "JavaScript", "TypeScript",
            "React",
            "Django (DRF)", "Node.js", "Express.js",
            "SQL", "MongoDB",
            "Git", "CI/CD", "Docker"
        ],
        "cvPdf": "/documents/cv.pdf"
    }
    return Response(data)