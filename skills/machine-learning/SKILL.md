
---
name: machine-learning
description: Machine learning skill for designing, developing, training, evaluating, optimizing, and deploying machine learning models and systems.
---

# Machine Learning Skill

## Purpose

Help AI assistants design, build, train, evaluate, optimize, and deploy reliable machine learning models and systems.

## Instructions

When working on machine learning tasks:

1. Understand the problem and expected outcomes.
2. Identify the machine learning task type.
3. Collect and inspect relevant datasets.
4. Prepare and preprocess data.
5. Select suitable algorithms and models.
6. Design a reproducible training workflow.
7. Train models using appropriate methods.
8. Evaluate model performance using relevant metrics.
9. Optimize models when necessary.
10. Deploy and monitor trained models.
11. Document experiments and results.

## Workflow

### 1. Problem Definition

Identify:
- Business or research objectives.
- Target variables.
- Input features.
- Expected predictions.
- Machine learning task type.
- Technical constraints.
- Success criteria.

### 2. Data Collection and Exploration

Evaluate:
- Data sources.
- Dataset size.
- Data quality.
- Missing values.
- Duplicate records.
- Class distribution.
- Data relevance.
- Potential data leakage.

Use authorized and appropriate datasets.

### 3. Data Preparation

Perform suitable operations:
- Data cleaning.
- Missing-value handling.
- Feature selection.
- Feature engineering.
- Encoding categorical variables.
- Feature scaling.
- Dataset splitting.

Prevent data leakage by fitting preprocessing steps only on training data.

### 4. Model Selection

Choose appropriate approaches based on the problem:

- Supervised learning.
- Unsupervised learning.
- Semi-supervised learning.
- Reinforcement learning.

Consider algorithms such as:
- Linear Regression.
- Logistic Regression.
- Decision Trees.
- Random Forest.
- Gradient Boosting.
- Support Vector Machines.
- K-Nearest Neighbors.
- Naive Bayes.
- K-Means Clustering.
- Neural Networks.

Evaluate model complexity, interpretability, computational requirements, and suitability.

### 5. Model Training

Establish:
- Training configuration.
- Hyperparameters.
- Validation strategy.
- Reproducible random seeds.
- Experiment tracking.
- Baseline models.

Train models using appropriate datasets and computational resources.

### 6. Model Evaluation

Use suitable evaluation metrics.

For classification:
- Accuracy.
- Precision.
- Recall.
- F1-score.
- Confusion Matrix.
- ROC-AUC when appropriate.

For regression:
- MAE.
- MSE.
- RMSE.
- R-squared.

For clustering:
- Silhouette Score.
- Davies-Bouldin Index.
- Cluster interpretation.

Evaluate generalization and check for overfitting and underfitting.

### 7. Model Optimization

Improve models through:
- Hyperparameter tuning.
- Feature engineering.
- Regularization.
- Cross-validation.
- Model comparison.
- Appropriate optimization techniques.

Avoid optimizing solely for a single metric when other requirements matter.

### 8. Deployment

Prepare models for practical use through:
- Model serialization.
- API integration.
- Inference pipelines.
- Input validation.
- Version management.
- Deployment testing.
- Rollback planning.

Select deployment infrastructure based on performance, reliability, and cost requirements.

### 9. Monitoring and Maintenance

Monitor:
- Prediction quality.
- Model performance.
- Data drift.
- Concept drift.
- Inference latency.
- Resource consumption.
- Operational failures.

Retrain or update models when evidence shows that improvements are necessary.

## Rules

- Never fabricate datasets, experiments, or evaluation results.
- Do not assume that high training accuracy means good generalization.
- Prevent data leakage.
- Use appropriate evaluation metrics.
- Keep experiments reproducible.
- Respect dataset licenses and privacy requirements.
- Protect sensitive training data.
- Document model limitations and assumptions.
- Consider fairness and potential bias.
- Do not deploy models without appropriate testing.
- Explain uncertainty and limitations clearly.

## Output

Provide:

1. Problem definition and machine learning approach.
2. Dataset requirements and preparation strategy.
3. Algorithm and model selection rationale.
4. Training implementation.
5. Evaluation metrics and results.
6. Optimization recommendations.
7. Deployment strategy.
8. Monitoring and maintenance plan.
