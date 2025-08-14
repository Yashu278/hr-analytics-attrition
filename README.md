# HR Analytics: Employee Attrition Analysis

## 📊 Project Overview

This project analyzes employee attrition patterns using IBM's HR Analytics dataset to identify factors that contribute to employee turnover and provide actionable insights for HR decision-making.

## 🎯 Project Objectives

- Analyze employee attrition patterns and identify key factors
- Perform comprehensive Exploratory Data Analysis (EDA)
- Create visualizations to understand data distributions and relationships
- Develop insights to help reduce employee turnover
- Provide recommendations for HR strategies

## 📁 Project Structure

```
HR-Analytics/
├── data/
│   ├── Raw/
│   │   └── Data Raw.csv              # Original raw dataset
│   ├── Cleaned/
│   │   ├── Cleaned Data.xlsx         # Cleaned and processed data
│   │   └── Refined with EDA.xlsx     # Data with EDA insights
│   └── download.jpg                  # Dataset reference image
├── Photos/
│   ├── EDA.png                       # Exploratory Data Analysis visualizations
│   └── Whole file.png                # Complete dataset overview
├── Final Data file with Final Analysis.xlsx  # Comprehensive analysis results
├── download_dataset.py               # Script to download dataset from Kaggle
└── README.md                         # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Required Python packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - openpyxl
  - kagglehub

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hr-analytics-attrition.git
cd hr-analytics-attrition
```

2. Install required packages:
```bash
pip install pandas numpy matplotlib seaborn openpyxl kagglehub
```

3. Download the dataset:
```bash
python download_dataset.py
```

## 📈 Analysis Components

### 1. Raw Data (`data/Raw/Data Raw.csv`)
- Original IBM HR Analytics Attrition dataset
- Contains employee information including demographics, job details, and attrition status

### 2. Cleaned Data (`data/Cleaned/`)
- **Cleaned Data.xlsx**: Processed and cleaned dataset ready for analysis
- **Refined with EDA.xlsx**: Enhanced dataset with exploratory analysis insights

### 3. Visualizations (`Photos/`)
- **EDA.png**: Comprehensive exploratory data analysis charts
- **Whole file.png**: Complete dataset overview and summary statistics

### 4. Final Analysis (`Final Data file with Final Analysis.xlsx`)
- Complete analysis results including:
  - Statistical summaries
  - Correlation analysis
  - Attrition patterns
  - Key insights and recommendations

## 🔍 Key Findings

The analysis reveals several important factors contributing to employee attrition:

1. **Job Satisfaction**: Employees with lower job satisfaction scores are more likely to leave
2. **Work-Life Balance**: Poor work-life balance significantly impacts retention
3. **Career Growth**: Limited advancement opportunities correlate with higher attrition
4. **Compensation**: Salary dissatisfaction is a major factor in employee turnover
5. **Department and Role**: Certain departments and job roles show higher attrition rates

## 📊 Visualizations

The project includes comprehensive visualizations covering:
- Attrition distribution across different variables
- Correlation heatmaps
- Box plots for numerical variables
- Bar charts for categorical analysis
- Histograms for distribution analysis

## 🛠️ Tools Used

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib & Seaborn**: Data visualization
- **Excel**: Additional analysis and reporting
- **Kaggle**: Dataset source

## 📋 Dataset Information

The IBM HR Analytics Attrition dataset contains information about employees including:
- Demographics (Age, Gender, Education, etc.)
- Job-related information (Department, Job Role, Years in Company, etc.)
- Work environment factors (Job Satisfaction, Work-Life Balance, etc.)
- Performance metrics (Performance Rating, Years Since Last Promotion, etc.)
- Attrition status (Yes/No)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- IBM for providing the HR Analytics dataset
- Kaggle for hosting the dataset
- The data science community for inspiration and resources

---

**Note**: This project is for educational and analytical purposes. The insights derived should be used responsibly in real-world HR applications.
