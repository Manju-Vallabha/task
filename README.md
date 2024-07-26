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


