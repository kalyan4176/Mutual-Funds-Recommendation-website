import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np

class FundRecommender:
    def __init__(self, data_path="funds.csv"):
        self.data_path = data_path
        self.df = None
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.load_data()
        self.train_model()

    def load_data(self):
        try:
            self.df = pd.read_csv(self.data_path)
            # Handle missing values in returns and ratios
            cols_to_clean = ['returns_1yr', 'returns_3yr', 'returns_5yr', 'sd', 'beta', 'sharpe', 'alpha']
            for col in cols_to_clean:
                if col in self.df.columns:
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce').fillna(0)
            
            # Risk Level is already numeric (1-6) in this dataset
            # 1=Low, 6=High
            if 'risk_level' in self.df.columns:
                 self.df['risk_score'] = pd.to_numeric(self.df['risk_level'], errors='coerce').fillna(3)
            else:
                 self.df['risk_score'] = 3

        except Exception as e:
            print(f"Error loading data: {e}")

    def train_model(self):
        if self.df is None:
            return

        # Features for recommendation: Risk Score, Returns (1Y, 3Y, 5Y), Ratios
        features = ['risk_score', 'returns_1yr', 'returns_3yr', 'returns_5yr', 'sd', 'sharpe']
        
        # Handle missing values
        X = self.df[features].fillna(0)
        
        # Scale features
        self.X_scaled = self.scaler.fit_transform(X)
        
        # Train KNN
        self.model = NearestNeighbors(n_neighbors=10, metric='euclidean')
        self.model.fit(self.X_scaled)

    def get_recommendations(self, user_profile):
        """
        user_profile: dict containing user inputs
        """
        age = int(user_profile.get('age', 30))
        duration = int(user_profile.get('duration', 5))
        risk_appetite = user_profile.get('risk_appetite', 'Medium')
        
        # Calculate Risk Capacity Score (1-6 scale to match dataset)
        score = 0
        
        # Age Factor
        if age < 35: score += 2
        elif age < 50: score += 1.5
        else: score += 1
        
        # Duration Factor
        if duration > 7: score += 2
        elif duration > 3: score += 1.5
        else: score += 1
        
        # Risk Appetite Factor (User Preference)
        appetite_map = {'Low': 1, 'Medium': 3, 'High': 5}
        appetite_score = appetite_map.get(risk_appetite, 3)
        
        # Combine
        final_risk_score = (score + appetite_score) / 2
        
        # Clamp to 1-6
        final_risk_score = max(1, min(6, final_risk_score))
        
        # Target Vector
        # We want good returns (e.g. 15-20%) and good sharpe (1.0+)
        target_returns = final_risk_score * 4 + 5 # e.g. Risk 6 -> 29%, Risk 1 -> 9%
        target_sharpe = 1.0 
        target_std = final_risk_score * 3 # Higher risk = higher std dev
        
        target_vector = np.array([[final_risk_score, target_returns, target_returns, target_returns, target_std, target_sharpe]])
        target_scaled = self.scaler.transform(target_vector)
        
        # Get Neighbors
        distances, indices = self.model.kneighbors(target_scaled)
        
        # Return Funds
        recommended_funds = self.df.iloc[indices[0]].to_dict(orient='records')
        
        # Ensure NaN values are handled for JSON serialization
        for fund in recommended_funds:
            for k, v in fund.items():
                if pd.isna(v):
                    fund[k] = None
        
        return recommended_funds
