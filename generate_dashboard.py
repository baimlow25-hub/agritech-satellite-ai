import json
import os
import matplotlib.pyplot as plt

def generate_analytics_report():
    log_file = "analytics_history.json"
    output_image = "farm_analytics_report.png"
    
    print("📊 Extracting time-series arrays from JSON database...")
    
    # 1. Check if database exists
    if not os.path.exists(log_file):
        print(f"❌ Error: '{log_file}' not found. Run main.py first to generate data!")
        return

    # 2. Parse the JSON history strings
    with open(log_file, "r") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"❌ Error reading JSON matrix: {e}")
            return

    if not data:
        print("⚠️ Database is empty. Nothing to plot.")
        return

    # 3. Extract tracking vectors
    timestamps = [entry["timestamp"].split()[1] for entry in data] # Get just the HH:MM:SS time
    ndvi_scores = [entry["mean_ndvi_canopy_score"] for entry in data]
    yield_predictions = [entry["predicted_yield_mt_per_ha"] for entry in data]

    # 4. Initialize dual-axis professional chart layout
    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Plot Canopy Health (NDVI) on Left Axis
    color = '#2ecc71'
    ax1.set_xlabel('Execution Timeline (Timestamp)', fontweight='bold', labelpad=12)
    ax1.set_ylabel('Mean NDVI (Canopy Health)', color=color, fontweight='bold')
    
    # Handle single or multi-point plotting cleanly
    if len(ndvi_scores) == 1:
        ax1.plot(timestamps * 2, ndvi_scores * 2, color=color, marker='o', linewidth=2, label="NDVI Trend")
    else:
        ax1.plot(timestamps, ndvi_scores, color=color, marker='o', linewidth=2, label="NDVI Trend")
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Instantiate Right Axis for AI Yield Predictions
    ax2 = ax1.twinx()
    color = '#3498db'
    ax2.set_ylabel('AI Predicted Yield (Metric Tons/Ha)', color=color, fontweight='bold')
    
    if len(yield_predictions) == 1:
        ax2.plot(timestamps * 2, yield_predictions * 2, color=color, marker='s', linestyle='--', linewidth=2, label="AI Prediction")
    else:
        ax2.plot(timestamps, yield_predictions, color=color, marker='s', linestyle='--', linewidth=2, label="AI Prediction")
    ax2.tick_params(axis='y', labelcolor=color)

    # Title and Formatting
    plt.title('AGRITECH SATELLITE AI: Chronological Farm Analytics Dashboard', fontsize=14, fontweight='bold', pad=15)
    fig.tight_layout()

    # Save out the high-res visualization asset
    plt.savefig(output_image, dpi=300)
    print(f"📈 Dashboard layer compiled successfully! Asset saved as: '{output_image}'")

if __name__ == "__main__":
    generate_analytics_report()