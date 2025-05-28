import os
import django
import sys

# Get the directory where this script is located (should be myWeb-Backend)
script_dir = os.path.dirname(os.path.abspath(__file__))

# If your Django project (the one with settings.py) is also named 'myWebBackend'
# and is a direct subdirectory of where manage.py is, then manage.py handles paths.
# For a standalone script, we might need to ensure the parent of 'myWebBackend' (i.e. 'myWeb')
# is in sys.path if 'myWebBackend.settings' is meant to be found like that, OR
# that the script_dir itself is enough if 'myWebBackend' is the project name
# and settings.py is in a subdirectory also called 'myWebBackend'.

# Common structure: 
# myWeb/
#   myWeb-Backend/  <-- manage.py, update_persona_script.py is here
#     myWebBackend/ <-- settings.py is here (Django project directory)
#       settings.py
#     persona/      <-- your app
#     ...
#   myWeb-Frontend/

# Add the directory containing the Django project (myWebBackend) to sys.path
# This is usually the directory where manage.py resides.
if script_dir not in sys.path:
    sys.path.append(script_dir)

# Your Django project's settings module. 
# This assumes your settings.py is inside a folder named 'myWebBackend' 
# which is at the same level as your 'persona' app, all inside the main 'myWeb-Backend' directory.
# So, the path would be myWebBackend.settings if the project directory is also myWebBackend.
SETTINGS_MODULE = 'api.settings' 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULE)

try:
    django.setup()
    print(f"Django setup successful using settings: {SETTINGS_MODULE}")
except ModuleNotFoundError as e:
    print(f"Error setting up Django: {e}")
    print(f"Could not find the Django settings module: '{SETTINGS_MODULE}'.")
    print("Please ensure:")
    print(f"1. This script (update_persona_script.py) is in the correct directory: {script_dir}")
    print("2. Your Django project's settings.py file is located correctly.")
    print(   "   (e.g., for 'myWebBackend.settings', it expects ./myWebBackend/settings.py relative to a directory in sys.path)")
    print(f"Current sys.path includes: {script_dir}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred during Django setup: {e}")
    sys.exit(1)

from persona.models import PersonalInfo
from django.utils import timezone

def run_update():
    translated_additional_info = """
# Basic Information
name: Yue Wen Peter Li
origin: Born in Seattle, grew up in Taipei
current_residence: Between Taipei and Boston
siblings: One younger brother
languages: English, Mandarin
zodiac_sign: Aries
personality_type: Extrovert

# Education
education:
  - institution: Northeastern University, Boston, MA
    degree: M.S. in Computer Science
  - institution: National Yang Ming Chiao Tung University, Taipei, Taiwan
    degree: M.S. in Health and Welfare Policy
  - institution: Fu-Jen Catholic University, Taipei, Taiwan
    degree: B.A. in Sociology & B.S. in Psychology
highest_education:
  institution: Northeastern University, Boston, MA
  degree: M.S. in Computer Science
reason_for_field: Discovered an interest in underlying computer science while studying statistics.

# Work Experience
work_experience:
  - role: Research Assistant
    organization: Institute of Health and Welfare Policy, Taipei, Taiwan

# Technical Skills
programming_languages:
  - Python
  - Java
  - C++
  - HTML
  - CSS
  - JavaScript
  - TypeScript
  - React.js
  - Django (DRF)
  - Node.js
  - Express.js
  - MYSQL
  - MongoDB
  - Git
  - CI/CD
  - Docker
  - AWS
strongest_skill: Full stack development
ui_design_experience: Experience with Figma from a Human-Computer Interaction course.

# Interests & Lifestyle
interests:
  - Cats
  - Coffee
  - Trading
relaxation_method: Getting enough sleep
cooking_preference: I have a list of signature dishes.
gaming_habits: Used to play a lot; please recommend games if you have any.

# Personality & Self-Perception
self_description: I enjoy stimulating my brain with knowledge from different fields.
team_vs_individual: Depends
conflict_approach: Observe quietly and intervene at critical moments.
preference_for_solitude: Don't like it but am good at it.
meeting_new_people: I like meeting interesting people.
perceived_strength: I am good at discovering interesting phenomena that most people don't notice.
how_others_see_me: No particular hope, but I hope others can experience interesting things with me and resonate together.
others_common_perception: A very nice person.
perfectionism_view: I am a pragmatic idealist.

# Mindset & Beliefs
most_valued_in_life: The autonomy of life.
view_on_success: The beginning of the next challenge.
view_on_failure: Just one path that didn't work out; need to find another way.
motto: Self-motivated and proactive.
decision_making_process: Write it down for rational analysis, then make decisions based on experience and sensibility.
belief_in_fate: Not really.
rational_vs_emotional: Both are very important.
meaning_of_life: Hope to experience this life well.
view_on_ai: It's fantastic!
belief_in_intuition: I believe in it.

# Habits & Lifestyle (Continued)
wake_up_time: Early to bed and early to rise.
morning_vs_night_person: Morning person.
exercise_habits: Jogging daily.
dietary_preferences: No particular restrictions.
coffee_vs_tea: Drink both.
weekend_activities: Enjoy the weekend thoroughly; rest well if there's nothing to do.
household_chores: Often, I'm the only one doing them...
daily_must_do_habit: Need coffee every day.
screen_time: I'm doomed.
urban_vs_rural_preference: I like the countryside with urban conveniences.
view_on_future_of_tech: It's fantastic!
five_year_plan: In the age of AI, the future changes too quickly; take it one step at a time.
aspire_to_start_company: Yes.
if_won_lottery: I'll think about it when I win.
biggest_challenge_sought: Maybe it hasn't appeared yet.
expectations_for_future: Work well, enjoy well, rest well.
"""
    try:
        info, created = PersonalInfo.objects.update_or_create(
            full_name='Yue Wen Peter Li',
            defaults={
                'job_title': 'AI Application Developer', 
                'bio': 'A passionate developer exploring the intersection of AI and web technologies. Currently building a persona-based AI assistant.',
                'skills_summary': 'Python, Django, React, AWS Lambda, OpenAI API, Full-Stack Development.',
                'experience_summary': 'Research Assistant and various project experiences in software development.',
                'hobbies': 'Cats, Coffee, Trading, Learning new technologies.',
                'contact_email': 'peter.li.yw@example.com', 
                'additional_info': translated_additional_info,
                'is_active': True, 
                'last_updated': timezone.now()
            }
        )
        if created:
            print(f"Successfully CREATED new PersonalInfo for: {info.full_name}")
        else:
            print(f"Successfully UPDATED PersonalInfo for: {info.full_name}")
    except django.core.exceptions.AppRegistryNotReady:
        print("Django App Registry Not Ready. Ensure django.setup() was called correctly and settings are configured.")
    except Exception as e:
        print(f"An error occurred during database operation: {e}")
        print("Please ensure the PersonalInfo model is correctly migrated and check your query parameters.")

if __name__ == '__main__':
    print("Attempting to update/create PersonalInfo record...")
    run_update()
    print("Script finished.") 