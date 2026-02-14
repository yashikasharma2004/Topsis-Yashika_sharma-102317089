TOPSIS Multi-Criteria Decision AnalysisTOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision analysis method that ranks alternatives based on their distance from ideal solutions.🎯 Assignment OverviewThis repository contains three complete implementations of TOPSIS as part of an academic assignment for UCS654:ProgramDescriptionLinkProgram 1Command-line Python scriptView CodeProgram 2Published PyPI PackagePyPI LinkProgram 3Web Application (Streamlit)Live Demo📦 Program 1: Command-Line ImplementationStandalone Python script for TOPSIS analysis via command line.Usage:Bashpython topsis_pkg.py 102317089-data.csv "1,1,1,1,1" "+,+,-,+,-" 102317089-result.csv
📦 Program 2: Python Package on PyPIInstallable Python package for TOPSIS analysis.Installation:Bashpip install Topsis-Yashika-102317089
Usage:Bashtopsis input.csv "1,1,1,2" "+,+,-,+" result.csv
🌐 Program 3: Web ApplicationA user-friendly web interface built with Streamlit for instant TOPSIS calculations.Features:File upload (CSV)Dynamic weight and impact inputReal-time result generation and rankingDownloadable result fileRun Locally:Bashcd "program-3"
pip install -r requirements.txt
streamlit run app.py
📊 Input FormatThe algorithm expects a CSV file where:First column: Names/Models (e.g., M1, M2)Other columns: Numeric values for criteriaWeights: Comma-separated (e.g., "1,1,1,2")Impacts: Comma-separated "+" for benefit, "-" for cost (e.g., "+,+,-,+")📁 Repository StructurePlaintextTopsis-Yashika_sharma-102317089/
│
├── program-1/                # Command-line script
├── program-2/                # PyPI package source
│   ├── setup.py
│   └── README.md
├── program-3/                # Web application (Streamlit)
│   ├── app.py                # Backend & UI
│   └── requirements.txt      # Dependencies
└── README.md                 # This file
👤 AuthorYashika Sharma Roll Number: 102317089Branch: B.Tech CSE
