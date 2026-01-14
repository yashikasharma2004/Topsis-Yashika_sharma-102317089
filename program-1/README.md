📊 TOPSIS Implementation in Python
Assignment: Predictive Analysis – Assignment 1
Name: yashika sharma Roll Number: 102317089

🧠 Overview
This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method in Python to rank multiple alternatives based on multiple criteria.

📁 Project Files

topsis_pkg.py            → TOPSIS Python program
102317089-data.csv      → Input dataset
102317089-result.csv    → Output file (generated)

📥 Input Dataset Format
CSV file
First column: Alternative names
Remaining columns: Numeric criteria
Example
Fund Name,P1,P2,P3,P4,P5
M1,0.93,0.86,4,40.3,11.52
M2,0.64,0.41,5.5,43.2,12.44
▶️ Execution Command
The output CSV file is generated using the following command:

python topsis_pkg.py 102317089-data.csv "1,1,1,1,1" "+,+,-,+,-" 102317089-result.csv
Weights: 1,1,1,1,1

Impacts:

+ → Higher value is better
- → Lower value is better
📤 Output
The generated CSV file contains:

Topsis Score
Rank (Rank 1 indicates the best alternative)