TOPSIS Implementation for Multi-Criteria Decision Making
Roll Number: 102317089

This project provides a complete suite for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis, including a command-line tool, a published Python package, and a live web application.

🚀 Project Overview
Program 1: Python Implementation
A robust Python script that performs TOPSIS analysis on a CSV dataset. It handles data normalization, weight application, and calculates distance from ideal best/worst solutions to provide final rankings.

Program 2: PyPI Package
The logic is packaged and published on PyPI for easy installation and reuse in other data science projects.

Package Name: Topsis-Yashika-102317089

Installation: pip install Topsis-Yashika-102317089

PyPI Link: https://pypi.org/project/Topsis-Yashika-102317089/

Program 3: Web Application
A user-friendly web interface built with Streamlit that allows anyone to upload a CSV and get TOPSIS results without writing any code.

Live App Link:(https://topsis-yashikasharma-102317089-xsjvpgzkpf9rnebkprcjze.streamlit.app/)

🛠️ Installation & Usage
Usage via Command Line
If you have the package installed, you can run it directly from your terminal:

Bash

topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
Example:

Bash

topsis 102317089-data.csv "1,1,1,2,1" "+,+,-,+,+" 102317089-result.csv
Usage via Web App
Open the [Live Web App Link].

Upload your CSV file (Ensure the first column contains names/models and subsequent columns are numeric).

Enter the weights (e.g., 1,1,1,2) and impacts (e.g., +,+,-,+).

Click Calculate and download your results.

📂 Repository Structure
topsis_pkg.py: Core logic for the TOPSIS algorithm.

app.py: Streamlit web application code.

setup.py: Configuration for PyPI packaging.

requirements.txt: Dependencies for the web app (Pandas, Numpy, Streamlit).

README.md: Project documentation.

🎯 Vision 2026
This project is part of my academic journey in the 6th semester, aiming toward securing a top-tier internship and placement by mastering MLOps and data science tools.
