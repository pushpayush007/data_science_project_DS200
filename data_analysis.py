"""
Maharashtra Voter Registration Data Analysis
Data Science Project - IISc Bengaluru
Author: Ayush Kumar Pushp
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configure matplotlib for better plots
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def load_and_clean_data():
    """Load and preprocess the voter registration data"""
    print("Loading voter registration data...")
    
    # Load data
    df = pd.read_csv('data.csv')
    
    # Clean numeric columns (remove commas and handle 'NA' values)
    numeric_columns = ['Active Registration', 'Male', 'Female', 'Other']
    for col in numeric_columns:
        df[col] = df[col].astype(str).str.replace(',', '').replace('NA', '0')
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    # Calculate derived metrics
    df['Total_Registration'] = df['Male'] + df['Female'] + df['Other']
    df['Gender_Ratio'] = (df['Female'] / df['Male']) * 1000  # Females per 1000 males
    df['Female_Percentage'] = (df['Female'] / df['Active Registration']) * 100
    df['Male_Percentage'] = (df['Male'] / df['Active Registration']) * 100
    
    print(f"Data loaded successfully. Shape: {df.shape}")
    print(f"Divisions: {df['Division'].nunique()}")
    print(f"Districts: {df['District'].nunique()}")
    
    return df

def generate_scatter_plot(df):
    """Create scatter plot: Gender Ratio vs Registration Volume"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Create scatter plot with division-wise coloring
    divisions = df['Division'].unique()
    colors = plt.cm.tab10(np.linspace(0, 1, len(divisions)))
    
    for i, division in enumerate(divisions):
        division_data = df[df['Division'] == division]
        scatter = ax.scatter(division_data['Active Registration'], 
                           division_data['Gender_Ratio'],
                           c=[colors[i]], 
                           label=division,
                           alpha=0.7,
                           s=100,
                           edgecolors='black',
                           linewidth=0.5)
    
    # Formatting
    ax.set_xlabel('Active Registration', fontweight='bold', fontsize=12)
    ax.set_ylabel('Gender Ratio (Females per 1000 Males)', fontweight='bold', fontsize=12)
    ax.set_title('District-wise Gender Ratio vs Registration Volume\nMaharashtra Voter Data Analysis', 
                 fontweight='bold', fontsize=16, pad=20)
    
    # Add trend line
    z = np.polyfit(df['Active Registration'], df['Gender_Ratio'], 1)
    p = np.poly1d(z)
    ax.plot(df['Active Registration'], p(df['Active Registration']), 
            "r--", alpha=0.8, linewidth=2, label=f'Trend line (slope: {z[0]:.4f})')
    
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3)
    
    # Annotations for outliers
    high_ratio = df[df['Gender_Ratio'] > 1500]
    for _, row in high_ratio.iterrows():
        ax.annotate(f"{row['District']}\n({row['Gender_Ratio']:.0f})", 
                   (row['Active Registration'], row['Gender_Ratio']),
                   xytext=(10, 10), textcoords='offset points',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                   fontsize=8)
    
    plt.tight_layout()
    plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Scatter plot saved as 'scatter_plot.png'")

def generate_box_plot(df):
    """Create box plot: Registration distribution by Division"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Box plot 1: Registration by Division
    box_data = [df[df['Division'] == div]['Active Registration'].values 
                for div in df['Division'].unique()]
    
    bp1 = ax1.boxplot(box_data, labels=df['Division'].unique(), patch_artist=True)
    colors = plt.cm.Set3(np.linspace(0, 1, len(bp1['boxes'])))
    for patch, color in zip(bp1['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax1.set_title('Distribution of Active Registration by Division', fontweight='bold', fontsize=14)
    ax1.set_ylabel('Active Registration', fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3)
    
    # Box plot 2: Gender Ratio by Division
    box_data2 = [df[df['Division'] == div]['Gender_Ratio'].values 
                 for div in df['Division'].unique()]
    
    bp2 = ax2.boxplot(box_data2, labels=df['Division'].unique(), patch_artist=True)
    for patch, color in zip(bp2['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax2.set_title('Distribution of Gender Ratio by Division', fontweight='bold', fontsize=14)
    ax2.set_ylabel('Gender Ratio (Females per 1000 Males)', fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('box_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Box plot saved as 'box_plot.png'")

def generate_bar_plot(df):
    """Create bar plot: Top districts and division comparison"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12))
    
    # Bar plot 1: Top 15 districts by registration
    top_districts = df.nlargest(15, 'Active Registration')
    bars1 = ax1.bar(range(len(top_districts)), top_districts['Active Registration'],
                    color=plt.cm.viridis(np.linspace(0, 1, len(top_districts))))
    
    ax1.set_title('Top 15 Districts by Active Registration', fontweight='bold', fontsize=14)
    ax1.set_ylabel('Active Registration', fontweight='bold')
    ax1.set_xticks(range(len(top_districts)))
    ax1.set_xticklabels([f"{row['District']}\n({row['Division']})" 
                        for _, row in top_districts.iterrows()], 
                       rotation=45, ha='right', fontsize=10)
    
    # Add value labels on bars
    for i, (_, row) in enumerate(top_districts.iterrows()):
        ax1.text(i, row['Active Registration'] + max(top_districts['Active Registration']) * 0.01, 
                f'{row["Active Registration"]:,.0f}', ha='center', va='bottom', 
                fontweight='bold', fontsize=9, rotation=90)
    
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Bar plot 2: Division-wise statistics
    division_stats = df.groupby('Division').agg({
        'Active Registration': 'sum',
        'Male': 'sum', 
        'Female': 'sum',
        'Gender_Ratio': 'mean'
    }).round(0)
    
    x = np.arange(len(division_stats))
    width = 0.35
    
    bars2 = ax2.bar(x - width/2, division_stats['Male'], width, 
                    label='Male', alpha=0.8, color='lightblue')
    bars3 = ax2.bar(x + width/2, division_stats['Female'], width,
                    label='Female', alpha=0.8, color='lightpink')
    
    ax2.set_title('Division-wise Male vs Female Registration', fontweight='bold', fontsize=14)
    ax2.set_ylabel('Registration Count', fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(division_stats.index, rotation=45, ha='right')
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('bar_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Bar plot saved as 'bar_plot.png'")

def generate_summary_statistics(df):
    """Generate and display summary statistics"""
    print("\n" + "="*60)
    print("SUMMARY STATISTICS - MAHARASHTRA VOTER REGISTRATION")
    print("="*60)
    
    # Overall statistics
    print(f"\nOVERALL STATISTICS:")
    print(f"Total Active Registrations: {df['Active Registration'].sum():,}")
    print(f"Total Male Voters: {df['Male'].sum():,}")
    print(f"Total Female Voters: {df['Female'].sum():,}")
    print(f"Total Other Voters: {df['Other'].sum():,}")
    print(f"Average Gender Ratio: {df['Gender_Ratio'].mean():.0f} females per 1000 males")
    print(f"Overall Female Percentage: {(df['Female'].sum()/df['Active Registration'].sum())*100:.1f}%")
    
    # Division-wise statistics
    print(f"\nDIVISION-WISE STATISTICS:")
    division_summary = df.groupby('Division').agg({
        'Active Registration': ['sum', 'mean'],
        'Gender_Ratio': 'mean',
        'Female_Percentage': 'mean'
    }).round(1)
    
    print(division_summary.to_string())
    
    # Top and bottom districts
    print(f"\nTOP 5 DISTRICTS BY REGISTRATION:")
    top5 = df.nlargest(5, 'Active Registration')[['District', 'Division', 'Active Registration', 'Gender_Ratio']]
    print(top5.to_string(index=False))
    
    print(f"\nTOP 5 DISTRICTS BY GENDER RATIO:")
    top5_gender = df.nlargest(5, 'Gender_Ratio')[['District', 'Division', 'Gender_Ratio', 'Active Registration']]
    print(top5_gender.to_string(index=False))

def main():
    """Main analysis function"""
    print("Maharashtra Voter Registration Data Analysis")
    print("=" * 50)
    
    # Load and clean data
    df = load_and_clean_data()
    
    # Generate all plots
    print("\nGenerating visualizations...")
    
    print("\n1. Creating Scatter Plot...")
    generate_scatter_plot(df)
    
    print("\n2. Creating Box Plot...")
    generate_box_plot(df)
    
    print("\n3. Creating Bar Plot...")
    generate_bar_plot(df)
    
    # Generate summary statistics
    generate_summary_statistics(df)
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("Generated files:")
    print("- scatter_plot.png")
    print("- box_plot.png") 
    print("- bar_plot.png")
    print("="*60)

if __name__ == "__main__":
    main()
