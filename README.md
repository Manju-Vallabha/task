# Job Portal: Candidate Ranking System

## Overview

The **Candidate Ranking System** is a web application developed using Streamlit that helps recruiters search and rank candidates based on their skills and experience. It utilizes LightGBM’s LambdaMART algorithm to provide a ranked list of candidates who possess a specific skill and have completed relevant courses.

## Features

- **Skill-Based Search:** Input a skill to find candidates who have that skill.
- **Ranking System:** Candidates are ranked based on the number of courses they have completed that include the specified skill.
- **Progress Indicator:** A progress bar gives visual feedback during data processing.
- **Detailed View:** The top candidates are displayed in expandable sections, showing their courses and experience.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Streamlit
- Pandas
- LightGBM



## Ranking Algorithms in Machine Learning

### LightGBM Ranking

**LightGBM** (Light Gradient Boosting Machine) is a gradient boosting framework that is highly efficient for large datasets. It includes specific functionalities for ranking tasks, which are useful in applications like search engines or recommendation systems.

- **Objective Function (`lambdarank`):** 
  - **LambdaMART:** LightGBM supports LambdaMART, an extension of MART (Multiple Additive Regression Trees), specifically designed for ranking. It optimizes the ranking quality by leveraging pairwise comparisons and focusing on metrics like NDCG (Normalized Discounted Cumulative Gain).
  - **NDCG as Evaluation Metric:** NDCG measures the effectiveness of the ranking by considering the position of relevant items. Higher relevance items are weighted more heavily if they appear earlier in the list.

### Other Ranking Algorithms

1. **XGBoost Ranking:**
   - **Objective Function (`rank:pairwise`):** 
     - **Pairwise Ranking:** XGBoost uses a pairwise ranking approach where the model learns to predict which of two items should be ranked higher. This approach optimizes for ranking metrics such as NDCG and is used to train models that improve the order of items based on their relevance.

2. **RankNet:**
   - **Neural Network-Based Model:** 
     - **Pairwise Comparisons:** RankNet uses neural networks to model the ranking problem as a series of pairwise comparisons. It learns to predict the probability of one item being ranked higher than another, which is useful for fine-tuning ranking results.

3. **RankSVM:**
   - **Support Vector Machines for Ranking:** 
     - **Classification-Based Ranking:** RankSVM frames ranking as a classification problem where it tries to separate relevant and irrelevant items based on their scores. It optimizes for a ranking loss function to improve the order of items.

## How It Works

In this project, LightGBM's `lambdarank` objective function is used to train a model that ranks candidates based on the number of relevant courses containing a specified skill. The ranking model is trained with features like the number of relevant courses and experience, and the results are evaluated using NDCG to ensure effective ranking.


## Dataset

### Description

The dataset used in this project is a CSV file named `updated_skills_courses.csv`. It contains information about candidates, their skills, courses, and experience. The data is utilized to rank candidates based on their proficiency in a specified skill and their relevant course history.

### Columns

The dataset includes the following columns:

1. **Name**: 
   - **Type**: `str`
   - **Description**: The name of the candidate.

2. **Skills**: 
   - **Type**: `str`
   - **Description**: A list of skills possessed by the candidate, separated by a vertical bar (`|`). For example, `Python|Java|SQL`.

3. **Courses**: 
   - **Type**: `str`
   - **Description**: A list of courses completed by the candidate, separated by a vertical bar (`|`). Each course title may include the relevant skills. For example, `Python Basics|Advanced Python Programming|Data Science with SQL`.

4. **Experience**: 
   - **Type**: `int`
   - **Description**: The number of years of experience the candidate has in their field.

### Example

| Name   | Skills               | Courses                                            | Experience |
|--------|----------------------|----------------------------------------------------|------------|
| Alice  | Python|Java          | Python Basics|Advanced Python|Java Fundamentals | 3          |
| Bob    | Python|SQL           | Data Science with Python|SQL for Data Analysis | 2          |
| Carol  | Java|SQL             | Java Programming Basics|Advanced SQL Techniques | 4          |

### Data Usage

- **Skill Search**: Users input a skill to search for candidates who possess that skill.
- **Ranking**: Candidates are ranked based on the number of courses containing the specified skill and their years of experience.
- **Filtering**: Only candidates who have the searched skill are considered for ranking.

This dataset is crucial for evaluating and ranking candidates effectively based on their skills and educational background. Make sure to update the dataset regularly to maintain the accuracy of the rankings.



