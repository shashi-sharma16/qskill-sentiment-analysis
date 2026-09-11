# Sentiment Analysis Web Application

A web application developed as part of a **QSkill Internship** task. The application analyzes user-entered text and classifies its sentiment as **Positive, Negative, or Neutral** using **TextBlob**.

## Project Overview

The application provides a simple web interface where users can enter a sentence or paragraph and analyze its sentiment.

It displays:

* Sentiment classification
* Polarity score
* Subjectivity score

## Features

* Analyze user-entered text
* Classify text as Positive, Negative, or Neutral
* Display polarity score
* Display subjectivity score
* Clear input and results
* Responsive and user-friendly interface

## Technologies Used

* **Python**
* **Flask**
* **TextBlob**
* **HTML**
* **CSS**

## How It Works

1. The user enters text into the web application.
2. Flask receives the submitted text.
3. TextBlob analyzes the text and calculates its polarity and subjectivity.
4. The application classifies the sentiment based on the polarity score:

   * Polarity > 0 → Positive
   * Polarity < 0 → Negative
   * Polarity = 0 → Neutral
5. The sentiment and scores are displayed on the webpage.

## Project Structure

```text
sentiment-analysis/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
cd sentiment-analysis
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

### 6. Open the application

Open the local Flask URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## Example

**Input:**

```text
I absolutely love this product!
```

**Output:**

```text
Sentiment: Positive
Polarity: 0.63
Subjectivity: 0.60
```

## Internship Task

**QSkill Internship Task:**
Develop a web application using Flask or Django that performs sentiment analysis on user-entered text. The application should classify the text as positive, negative, or neutral using TextBlob and display polarity and subjectivity scores.
