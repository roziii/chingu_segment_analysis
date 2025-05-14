from typing import List, Dict, Union
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import Ridge, Lasso, SGDRegressor, SGDClassifier
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier, plot_tree
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_squared_error, r2_score
)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

class MLModeler:
    """
    A modular class for building, training, evaluating, and visualizing various ML models.
    Supports classification and regression tasks with KNN, Decision Trees, Ridge/Lasso, and SGD models.
    """
    def __init__(self, df , features: list , target: list , task='classification', test_size=0.2, random_state=42):
        self.task = task
        self.df = df 
        self.test_size = test_size
        self.random_state = random_state
        self.models = {}
        self.results = {}
        self.sgd_loss_history = {}

        self.X_interp, self.X_extrap, self.y_interp, self.y_extrap = train_test_split(
           self.df[features], self.df[target], test_size=0.2, random_state=self.random_state
        )

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X_interp, self.y_interp, test_size=self.test_size, random_state=self.random_state
        )

    def add_model(self, name, model, use_scaler=True):
        if use_scaler:
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('model', model)
            ])
        else:
            pipeline = Pipeline([
                ('model', model)
            ])
        self.models[name] = pipeline

    def add_knn_model(self, n_neighbors=5):
        if self.task == 'classification':
            knn = KNeighborsClassifier(n_neighbors=n_neighbors)
            self.add_model(f'KNNClassifier_k{n_neighbors}', knn)
        elif self.task == 'regression':
            knn = KNeighborsRegressor(n_neighbors=n_neighbors)
            self.add_model(f'KNNRegressor_k{n_neighbors}', knn)
    
    
    def add_decision_tree_model(self, **kwargs):
        if self.task == 'regression':
            tree = DecisionTreeRegressor(random_state=self.random_state, **kwargs)
            self.add_model('DecisionTreeRegressor', tree, use_scaler=False)
        elif self.task == 'classification':
            tree = DecisionTreeClassifier(random_state=self.random_state, **kwargs)
            self.add_model('DecisionTreeClassifier', tree, use_scaler=False)

    def add_binary_tree_model(self, **kwargs):
        if self.task != 'classification':
            print("Binary tree model is only applicable for classification tasks.")
            return
        tree = DecisionTreeClassifier(random_state=self.random_state, max_leaf_nodes=2, **kwargs)
        self.add_model('BinaryDecisionTreeClassifier', tree, use_scaler=False)

    def add_ridge_lasso_models(self):
        if self.task != 'regression':
            print("Ridge/Lasso only apply to regression tasks.")
            return

        alphas = np.arange(0.01, 6.01, 0.01)
        best_ridge = (None, -np.inf)
        best_lasso = (None, -np.inf)
        ridge_scores = {}
        lasso_scores = {}

        for alpha in alphas:
            ridge = Pipeline([('scaler', StandardScaler()), ('model', Ridge(alpha=alpha))])
            lasso = Pipeline([('scaler', StandardScaler()), ('model', Lasso(alpha=alpha))])
            ridge.fit(self.X_train, self.y_train)
            lasso.fit(self.X_train, self.y_train)
            r_score = r2_score(self.y_test, ridge.predict(self.X_test))
            l_score = r2_score(self.y_test, lasso.predict(self.X_test))
            ridge_scores[alpha] = r_score
            lasso_scores[alpha] = l_score
            if r_score > best_ridge[1]:
                best_ridge = (alpha, r_score)
            if l_score > best_lasso[1]:
                best_lasso = (alpha, l_score)

        self.add_model(f'Ridge_alpha_{best_ridge[0]:.2f}', Ridge(alpha=best_ridge[0]))
        self.add_model(f'Lasso_alpha_{best_lasso[0]:.2f}', Lasso(alpha=best_lasso[0]))

        plt.figure(figsize=(10, 5))
        plt.plot(list(ridge_scores.keys()), list(ridge_scores.values()), label='Ridge')
        plt.plot(list(lasso_scores.keys()), list(lasso_scores.values()), label='Lasso')
        plt.xlabel('Alpha')
        plt.ylabel('R² Score')
        plt.title('R² Score vs Alpha for Ridge and Lasso')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_decision_tree(self, model_name, max_depth=3):
        model = self.models.get(model_name)
        if model and hasattr(model.named_steps['model'], 'tree_'):
            plt.figure(figsize=(16, 10))
            plot_tree(model.named_steps['model'], feature_names=self.X_train.columns, filled=True, max_depth=max_depth)
            plt.title(f"Decision Tree Visualization: {model_name}")
            plt.show()
        else:
            print(f"Model '{model_name}' is not a decision tree or not yet trained.")

    def add_gradient_descent_model(self, learning_rate=0.01, max_iter=1000, tol=1e-3):
        if self.task == 'regression':
            sgd = SGDRegressor(learning_rate='constant', eta0=learning_rate,
                               max_iter=max_iter, tol=tol, verbose=1)
            self.add_model('SGDRegressor', sgd)
        elif self.task == 'classification':
            sgd = SGDClassifier(learning_rate='constant', eta0=learning_rate,
                                max_iter=max_iter, tol=tol, verbose=1)
            self.add_model('SGDClassifier', sgd)

    def plot_sgd_convergence(self):
        for name, model in self.models.items():
            if 'SGD' in name:
                if hasattr(model.named_steps['model'], 't_'):
                    print(f"{name} ran for {model.named_steps['model'].t_} iterations")
                else:
                    print(f"{name} convergence info not available")

    def plot_correlation_matrix(self):
        corr_data = self.X_interp.select_dtypes(include=[np.number]).copy()
        corr_data['target'] = self.y_interp
        corr_matrix = corr_data.corr()
        sorted_features = corr_matrix['target'].abs().sort_values(ascending=False)
        sorted_cols = sorted_features.index.tolist()
        plt.figure(figsize=(12, 8))
        sns.heatmap(corr_matrix.loc[sorted_cols, sorted_cols], annot=True, fmt=".2f", cmap="coolwarm", square=True)
        plt.title("Correlation Matrix of Numeric Features (Sorted by Correlation to Target)")
        plt.tight_layout()
        plt.show()

    def plot_coefficients(self, model_name):
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Model '{model_name}' not found")

        if hasattr(model.named_steps['model'], 'coef_'):
            coefs = model.named_steps['model'].coef_
            if coefs.ndim > 1:
                coefs = coefs[0]
            features = self.X_train.columns if hasattr(self.X_train, 'columns') else [f'x{i}' for i in range(len(coefs))]
            coef_df = pd.DataFrame({'Feature': features, 'Coefficient': coefs})
            coef_df = coef_df.sort_values(by='Coefficient', key=abs, ascending=False)
            plt.figure(figsize=(10, 6))
            sns.barplot(data=coef_df, x='Coefficient', y='Feature', palette='viridis')
            plt.title(f"Feature Coefficients: {model_name}")
            plt.tight_layout()
            plt.show()
        else:
            print(f"Model '{model_name}' does not have coefficients to display.")

    def plot_y_vs_yhat(self, model_name):
        model = self.models.get(model_name)
        if model is None:
            raise ValueError(f"Model '{model_name}' not found.")
    
        y_hat = model.predict(self.X_test)
        plt.figure(figsize=(8, 6))
        plt.scatter(self.y_test, y_hat, alpha=0.6)
        plt.plot([self.y_test.min(), self.y_test.max()], [self.y_test.min(), self.y_test.max()], 'r--')
        plt.xlabel("Actual y")
        plt.ylabel("Predicted ŷ")
        plt.title(f"Actual vs Predicted: {model_name}")
        plt.tight_layout()
        plt.grid(True)
        plt.show()


    def plot_classifier_performance_boxplot(self):
        if self.task != 'classification':
            print("Box plot only applicable for classification tasks.")
            return

        scores_df = pd.DataFrame()
        for name, model in self.models.items():
            try:
                scores = cross_val_score(model, self.X_interp, self.y_interp, cv=5, scoring='accuracy')
                temp_df = pd.DataFrame({'Model': name, 'Accuracy': scores})
                scores_df = pd.concat([scores_df, temp_df], ignore_index=True)
            except Exception as e:
                print(f"Skipping {name}: {e}")

        if not scores_df.empty:
            plt.figure(figsize=(12, 6))
            sns.boxplot(x='Model', y='Accuracy', data=scores_df)
            plt.xticks(rotation=45)
            plt.title("Classifier Accuracy Distribution (5-Fold CV)")
            plt.tight_layout()
            plt.grid(True)
            plt.show()


    def find_optimal_training_size(self, model_name, step=0.1):
        model = self.models.get(model_name)
        if model is None:
            raise ValueError(f"Model '{model_name}' not found.")

        fractions = np.arange(step, 1.01, step)
        train_scores = []
        test_scores = []

        for frac in fractions:
            n_rows = int(len(self.X_interp) * frac)
            X_frac = self.X_interp.iloc[:n_rows]
            y_frac = self.y_interp.iloc[:n_rows]

            try:
                model.fit(X_frac, y_frac)
                y_train_pred = model.predict(X_frac)
                y_test_pred = model.predict(self.X_test)
                if self.task == 'classification':
                    train_score = accuracy_score(y_frac, y_train_pred)
                    test_score = accuracy_score(self.y_test, y_test_pred)
                else:
                    train_score = r2_score(y_frac, y_train_pred)
                    test_score = r2_score(self.y_test, y_test_pred)
                train_scores.append(train_score)
                test_scores.append(test_score)
            except Exception as e:
                train_scores.append(np.nan)
                test_scores.append(np.nan)
                print(f"Error with {frac*100:.0f}% of data: {e}")

        plt.figure(figsize=(10, 5))
        plt.plot(fractions * 100, train_scores, marker='o', label='Train')
        plt.plot(fractions * 100, test_scores, marker='s', label='Test')
        plt.xlabel("Training Data Size (%)")
        plt.ylabel("Accuracy" if self.task == 'classification' else "R² Score")
        plt.title(f"Train vs Test Performance: {model_name}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def cross_validate_models(self, cv=5):
        scores = {}
        for name, model in self.models.items():
            try:
                score = cross_val_score(model, self.X_interp, self.y_interp, cv=cv,
                                        scoring='r2' if self.task == 'regression' else 'accuracy')
                scores[name] = score.mean()
            except Exception as e:
                print(f"Skipping {name}: {e}")
        return pd.Series(scores).sort_values(ascending=False)

    
    def kfold_train(self, k=5):
        kf = KFold(n_splits=k, shuffle=True, random_state=self.random_state)
        kfold_results = {}
        for name, model in self.models.items():
            scores = []
            for train_index, test_index in kf.split(self.X_interp):
                X_train_fold = self.X_interp.iloc[train_index]
                X_test_fold = self.X_interp.iloc[test_index]
                y_train_fold = self.y_interp.iloc[train_index]
                y_test_fold = self.y_interp.iloc[test_index]
                model.fit(X_train_fold, y_train_fold)
                y_pred = model.predict(X_test_fold)
                if self.task == 'classification':
                    scores.append(accuracy_score(y_test_fold, y_pred))
                else:
                    scores.append(r2_score(y_test_fold, y_pred))
            kfold_results[name] = np.mean(scores)
        return pd.Series(kfold_results).sort_values(ascending=False)

        
    def train_all(self):
        for name, model in self.models.items():
            model.fit(self.X_train, self.y_train)

            
    def evaluate_all(self):
        for name, model in self.models.items():
            y_pred = model.predict(self.X_test)
            if self.task == 'classification':
                self.results[name] = {
                    'accuracy': accuracy_score(self.y_test, y_pred),
                    'precision': precision_score(self.y_test, y_pred, average='macro'),
                    'recall': recall_score(self.y_test, y_pred, average='macro'),
                    'f1_score': f1_score(self.y_test, y_pred, average='macro')
                }
            elif self.task == 'regression':
                self.results[name] = {
                    'mse': mean_squared_error(self.y_test, y_pred),
                    'r2': r2_score(self.y_test, y_pred)
                }

    def plot_model_complexity_boxplot(self, model_type, param_name, param_range):
        from sklearn.base import clone
        scores_df = pd.DataFrame()

        for val in param_range:
            if self.task == 'classification':
                if model_type == 'decision_tree':
                    base_model = DecisionTreeClassifier(**{param_name: val}, random_state=self.random_state)
                elif model_type == 'knn':
                    base_model = KNeighborsClassifier(**{param_name: val})
                else:
                    print(f"Unsupported model type: {model_type}")
                    return
                score_type = 'accuracy'
            else:
                if model_type == 'decision_tree':
                    base_model = DecisionTreeRegressor(**{param_name: val}, random_state=self.random_state)
                elif model_type == 'knn':
                    base_model = KNeighborsRegressor(**{param_name: val})
                else:
                    print(f"Unsupported model type: {model_type}")
                    return
                score_type = 'r2'

            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('model', base_model)
            ])

            try:
                scores = cross_val_score(pipeline, self.X_interp, self.y_interp, cv=5, scoring=score_type)
                df = pd.DataFrame({
                    'Param': val,
                    'Score': scores
                })
                scores_df = pd.concat([scores_df, df], ignore_index=True)
            except Exception as e:
                print(f"Error with {param_name}={val}: {e}")

        if not scores_df.empty:
            plt.figure(figsize=(12, 6))
            sns.boxplot(data=scores_df, x='Score', y='Param', orient='h')
            plt.xlabel(score_type.capitalize())
            plt.ylabel(param_name)
            plt.title(f"Model Performance by {param_name} ({model_type})")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
    
    def get_results(self):
        return pd.DataFrame(self.results).T.sort_values(by='r2' if self.task == 'regression' else 'accuracy', ascending=False)

    
    def predict(self, model_name, X_new):
        model = self.models.get(model_name)
        if model:
            return model.predict(X_new)
        raise ValueError(f"Model '{model_name}' not found")
