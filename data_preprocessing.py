import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

stock_files = [
    "TCS_stock_data.csv",
    "RELIANCE_stock_data.csv",
    "APPLE_stock_data.csv",
    "TESLA_stock_data.csv",
    "MICROSOFT_stock_data.csv"
]

output_folder = "processed_data"
os.makedirs(output_folder, exist_ok=True)

for file in stock_files:
    print(f"Processing {file}...")

    df = pd.read_csv(file)

    # ✅ Select Close column safely
    data = df[['Close']].copy()

    # ✅ Force numeric conversion (strings → NaN)
    data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

    # ✅ Drop invalid rows
    data = data.dropna()

    # ✅ Scaling
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    # Save processed file
    processed_df = pd.DataFrame(scaled_data, columns=['Scaled_Close'])
    output_path = os.path.join(
        output_folder,
        file.replace(".csv", "_processed.csv")
    )

    processed_df.to_csv(output_path, index=False)

    print(f"✅ Saved: {output_path}")
    print("-" * 40)

print("🎉 Data preprocessing completed successfully.")
