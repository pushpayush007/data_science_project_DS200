# Maharashtra Voter Registration Data Analysis

A comprehensive data science project analyzing voter registration patterns across Maharashtra districts using Python and data visualization techniques.

## 📊 Project Overview

This project analyzes voter registration data from Maharashtra, India, focusing on gender distribution patterns, registration volumes, and district-wise variations. The analysis provides insights into voting demographics and helps understand electoral participation across different regions.

## 📁 Repository Structure

```
├── data_analysis.py          # Main analysis script
├── data.csv                  # Raw voter registration dataset
├── scatter_plot.png          # Gender ratio vs registration volume
├── box_plot.png             # Distribution analysis by division
├── bar_plot.png             # Top districts and comparative analysis
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## 📈 Data Source

**Dataset**: Maharashtra Voter Registration Data  
**Source**: [data.gov.in](https://data.gov.in/) - Government of India Open Data Platform  
**Coverage**: District-wise voter registration data across Maharashtra divisions  
**Variables**: 
- Division and District names
- Active Registration counts
- Gender-wise breakdown (Male, Female, Other)
- Registration totals

## 🔍 Analysis Overview

### Key Metrics Calculated:
- **Gender Ratio**: Females per 1000 males
- **Female Percentage**: Proportion of female voters
- **Registration Density**: Total active registrations per district

### Research Questions:
1. How does gender ratio vary across different divisions in Maharashtra?
2. Which districts have the highest voter registration volumes?
3. What are the patterns in male vs female voter registration?
4. Are there any outliers in terms of gender distribution?

## 📊 Visualizations Generated

### 1. Scatter Plot Analysis
**File**: `scatter_plot.png`
- **Purpose**: Analyze relationship between registration volume and gender ratio
- **Key Findings**:
  - Most districts show gender ratio between 1000-1500 females per 1000 males
  - Higher registration volumes don't necessarily correlate with better gender ratios
  - Several districts show exceptional gender ratios above 1500

### 2. Box Plot Analysis  
**File**: `box_plot.png`
- **Purpose**: Compare distribution patterns across divisions
- **Key Findings**:
  - Nashik division shows highest median registration volumes
  - Mumbai division has lowest registration volumes but consistent patterns
  - Significant variation exists within divisions

### 3. Bar Plot Analysis
**File**: `bar_plot.png`
- **Purpose**: Identify top-performing districts and division comparisons
- **Key Findings**:
  - Nashik leads in absolute registration numbers
  - Pune and Nashik divisions dominate top district rankings
  - Clear urban vs rural registration patterns emerge

## 🔬 Key Insights

### Statistical Summary:
- **Total Active Registrations**: ~35 million voters
- **Average Gender Ratio**: ~1,350 females per 1000 males
- **Female Voter Percentage**: ~62.7%
- **Top Division by Volume**: Nashik
- **Highest Gender Ratio District**: Chandrapur (4,054 per 1000)

### Notable Observations:

1. **Gender Representation**: Maharashtra shows a favorable gender ratio with more female voters than male voters in most districts.

2. **Urban vs Rural Patterns**: Urban areas (Mumbai) show different registration patterns compared to rural/semi-urban regions.

3. **Division-wise Variations**: Significant differences exist between divisions, with Nashik and Pune showing highest engagement.

4. **Outlier Analysis**: Chandrapur district shows exceptionally high female participation, warranting further investigation.

## 🛠️ Technical Implementation

### Tools and Libraries Used:
- **Python 3.8+**
- **pandas**: Data manipulation and analysis
- **matplotlib**: Static visualizations
- **seaborn**: Statistical plotting
- **numpy**: Numerical computations

### Key Features:
- Data cleaning and preprocessing
- Statistical analysis and summary generation
- Multiple visualization types (scatter, box, bar plots)
- Outlier detection and annotation
- Export-ready high-resolution plots

## 🚀 Running the Analysis

### Prerequisites:
```bash
pip install pandas matplotlib seaborn numpy
```

### Execution:
```bash
python data_analysis.py
```

### Google Colab:
1. Upload `data.csv` to Colab environment
2. Install required packages: `!pip install pandas matplotlib seaborn`
3. Run the analysis script
4. Download generated plots

## 📊 Results and Impact

This analysis provides valuable insights for:
- **Electoral Planning**: Understanding voter distribution patterns
- **Policy Making**: Identifying areas with unique demographic characteristics  
- **Research**: Baseline data for political science studies
- **Demographics**: Gender participation patterns in democratic processes

## 🔮 Future Work

Potential extensions to this analysis:
- Time-series analysis if historical data becomes available
- Correlation with socio-economic indicators
- Machine learning models for voter turnout prediction
- Interactive dashboard development using Plotly/Dash

## 📚 References

1. **Data Source**: Government of India Open Data Platform. (2024). *Maharashtra Voter Registration Data*. Retrieved from https://data.gov.in/
2. **Election Commission of India**: Voter registration statistics and demographic analysis guidelines
3. **Census of India**: Population and demographic reference data for Maharashtra state

## 👨‍💻 Author

**Ayush Kumar Pushp**  
M.Tech in Computational and Data Science  
Indian Institute of Science, Bengaluru  
📧 ayushpushp@iisc.ac.in  

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page and submit pull requests.

---

*Last updated: December 2024*
