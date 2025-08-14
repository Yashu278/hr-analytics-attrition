# IBM HR Analytics: Comprehensive Employee Attrition Analysis

## 📊 Project Overview

This comprehensive project analyzes employee attrition patterns using IBM's HR Analytics dataset to identify critical factors that contribute to employee turnover. The analysis covers multiple dimensions including demographics, job satisfaction, performance metrics, compensation, and career growth to provide actionable insights for HR decision-making and employee retention strategies.

## 🎯 Project Objectives

- Analyze employee attrition patterns and identify key factors
- Perform comprehensive Exploratory Data Analysis (EDA)
- Create visualizations to understand data distributions and relationships
- Develop insights to help reduce employee turnover
- Provide recommendations for HR strategies

## 📁 Project Structure

```
IBM-HR-Analytics/
├── data/
│   ├── Raw/
│   │   └── Data Raw.csv              # Original IBM HR Analytics dataset (1,470 employees)
│   ├── Cleaned/
│   │   ├── Cleaned Data.xlsx         # Cleaned and processed data
│   │   └── Refined with EDA.xlsx     # Data with EDA insights
│   └── download.jpg                  # Dataset reference image
├── Photos/
│   ├── EDA.png                       # Exploratory Data Analysis visualizations
│   └── Whole file.png                # Complete dataset overview
├── Final Data file with Final Analysis.xlsx  # Comprehensive multi-sheet analysis
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
- Comprehensive multi-sheet analysis including:
  - **Demographic Insights**: Age distribution and demographic patterns
  - **Employee Satisfaction**: Job satisfaction and work-life balance analysis
  - **Performance**: Performance ratings and metrics correlation
  - **Compensation and Perks**: Income vs attrition analysis
  - **Role and Department Analysis**: Department-wise insights
  - **Education and Skills**: Education relation with skills
  - **Experience & Growth**: Career progression analysis
  - **EDA Dashboard**: Interactive dashboard with key metrics

## 🔍 Key Findings

The comprehensive analysis of 1,470 employees reveals several critical factors contributing to employee attrition (16.1% attrition rate):

1. **Job Satisfaction & Work-Life Balance**: Strong correlation between satisfaction scores and retention
2. **Compensation Impact**: Income levels significantly influence attrition decisions
3. **Career Growth Opportunities**: Limited advancement and promotion opportunities drive turnover
4. **Department-Specific Patterns**: Research & Development (961 employees) and Sales (446 employees) show different attrition patterns
5. **Performance & Experience**: Performance ratings and years of experience correlate with retention
6. **Demographic Factors**: Age, education, and marital status impact attrition likelihood

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

The IBM HR Analytics Attrition dataset contains comprehensive information about 1,470 employees across 35 features including:
- **Demographics**: Age, Gender, Education, Marital Status, Education Field
- **Job Information**: Department (R&D, Sales, HR), Job Role, Job Level, Years in Company
- **Work Environment**: Job Satisfaction, Work-Life Balance, Environment Satisfaction, Job Involvement
- **Performance Metrics**: Performance Rating, Years Since Last Promotion, Training Times
- **Compensation**: Monthly Income, Daily Rate, Hourly Rate, Percent Salary Hike
- **Career Factors**: Total Working Years, Years in Current Role, Years with Current Manager
- **Work-Life Factors**: Distance from Home, Business Travel, Overtime, Stock Option Level
- **Attrition Status**: Yes/No (237 employees left, 1,233 stayed)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Yashu278**
- GitHub: [@Yashu278](https://github.com/Yashu278)

## 🙏 Acknowledgments

- IBM for providing the HR Analytics dataset
- Kaggle for hosting the dataset
- The data science community for inspiration and resources

---

**Note**: This project is for educational and analytical purposes. The insights derived should be used responsibly in real-world HR applications.
