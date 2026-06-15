import numpy as np
from sklearn.ensemble import RandomForestRegressor

def predict_crop_yield(ndvi_mean_score):
    """
    Trains an advanced ensemble Machine Learning model (Random Forest)
    using synthetic multi-variable agricultural training logs to output
    highly nuanced yield estimations.
    """
    print("\n🤖 Initializing Advanced Random Forest ML Forecasting Architecture...")
    
    # 1. Enhanced Training Logs (NDVI Mean, Peak Biomass Intensity) -> Historical Yield (Tons/Hectare)
    # This simulates complex non-linear crop growth patterns
    X_train = np.array([
        [0.10, 0.20],  # Poor growth / bare soil
        [0.20, 0.35],  # Early vegetative phase
        [0.40, 0.55],  # Healthy mid-growth
        [0.60, 0.85],  # Optimal canopy structure (Peak Yield sweet spot)
        [0.75, 0.95],  # Dense saturation
        [0.90, 1.00]   # Extreme overgrowth/weed anomalies (Yield begins tapering)
    ])
    
    y_train = np.array([0.5, 1.1, 2.8, 5.4, 4.8, 4.2])
    
    # 2. Initialize the Ensemble Forest Model
    # n_estimators=100 creates an array of 100 parallel decision trees for maximum voting stability
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Train the estimators
    model.fit(X_train, y_train)
    print("📈 Ensemble model training phase complete across historical arrays.")
    
    # 3. Format input feature array
    # For now, we will pair the real mean score with a safe peak intensity estimate (e.g., mean * 2, capped at 1.0)
    simulated_peak = min(1.0, ndvi_mean_score * 2.2)
    input_features = np.array([[ndvi_mean_score, simulated_peak]])
    
    # Execute prediction matrix pass
    predicted_tonnage = model.predict(input_features)[0]
    
    print("-" * 50)
    print(f"🔮 PREDICTED HARVEST YIELD: {predicted_tonnage:.2f} Metric Tons per Hectare")
    print("-" * 50)
    
    return predicted_tonnage

if __name__ == "__main__":
    # Test baseline verification run
    predict_crop_yield(0.1944)