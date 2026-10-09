<h1 align="center">WaveEase</h1>

<p align="center">
  <b><i>Catch the wave, teach with ease!</i></b>
</p>

## What is it?
Teachers spend hours creating materials for their classes; WaveEase reduces that workload in minutes. WaveEase is a teacher assistant platform aimed at simplifying and supplementing classroom management. It utilizes Artificial Intelligence to streamline everyday needs for teachers. It includes a lesson planner, rubric maker, quiz creator,  email framer, grading assistant, and text leveler. 

## Key Features
**Lesson Planner** - Creates a complete lesson with a timeline and resources.

**Rubric Designer** - Creates a rubric tailored to any assignment. Weighs different categories and analyzes learning targets.

**Quiz Maker** - Designs a quiz on any subject. The tool leverages the provided items to create progressively difficult questions.

**Email Framer** - Crafts professional emails for communication with students, parents, and administrators.

**Grading Assistant** - Reviews and scores students' work. Provides specific feedback that helps students improve.

**Text Leveler** - Converts any text into versions appropriate for their grade level. Preserves the core meaning while adjusting vocabulary or language to match the grade selected.

## Screenshots
<img width="45%" height="834" alt="Screenshot 2026-06-24 at 12 53 39 AM" src="https://github.com/user-attachments/assets/a7caaa18-adf8-45b6-9c5f-0bcabe8167f9" />
<img width="45%" height="835" alt="Screenshot 2026-06-24 at 12 54 02 AM" src="https://github.com/user-attachments/assets/f5314d03-aadb-450b-93ce-11108c71380d" />
<img width="45%" height="834" alt="Screenshot 2026-06-24 at 1 04 05 AM" src="https://github.com/user-attachments/assets/ae66b1e2-4b16-4177-b652-2b6b7cfec9c8" />
<img width="45%" height="835" alt="Screenshot 2026-06-24 at 1 07 08 AM" src="https://github.com/user-attachments/assets/420b0dc2-3635-4e1c-b9a3-f9e44fb60da6" />

## Tech Stack

**Backend:** Python, Django

**AI:** OpenAI API (GPT-5-mini)

**Frontend:** HTML, CSS, JavaScript

## Setup

Before starting, get an OpenAI API key from the OpenAI Platform.

1. Clone the repository

```bash
git clone https://github.com/x2txct64/waveease.git
cd waveease
```

2. Create a virtual environment

```bash
python3 -m venv venv
```

3. Activate the virtual environment

```bash
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root and add your API key

```env
OPENAI_API_KEY="your_api_key_here"
```

6. Run the server

```bash
python3 manage.py runserver
```

7. Open your browser and go to

```text
http://127.0.0.1:8000/
```

## Demo Video

https://github.com/user-attachments/assets/b5edfacc-dc74-476b-b1cd-793f4e169946












