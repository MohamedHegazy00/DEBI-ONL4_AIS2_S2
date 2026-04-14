import pandas as pd
import mlflow
import warnings
import os

warnings.filterwarnings("ignore")

# English comments: Input data for prediction
data = [
    [-0.7541830079917924, 0.5780143566720919, 0.11375998165198585, -0.14673040749854463, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 2.0],
    [-0.5605884106597949, 0.753908347743766, 0.7003528882054108, 1.6923927520037099, 0.0, 1.0, 0.0, 1.0, 9.0, 1.0, 1.0]
]
df = pd.DataFrame(data)

# English comments: Updated paths based on your actual directory structure
base_path = r"C:\github depi\DEBI-ONL4_AIS2_S2\python\MachineLearning"
# English comments: Using '0' as experiment_id as shown in your directory list
experiment_id = "0" 

# ملاحظة: تأكد من اسم الـ Run ID داخل مجلد رقم 0
# لو طلع خطأ "No such file"، ادخل جوه فولدر "0" وشوف اسم الفولدر اللي جواه وحدث الـ run_id هنا
run_id = "4cac54c38fe34645b3cf5a9a1794355b" 

# English comments: Construct local path
model_path = os.path.join(base_path, "mlruns", experiment_id, run_id, "artifacts", "model_rf")

print(f"Checking path: {model_path}")

if not os.path.exists(model_path):
    print(f"❌ Error: Model path not found! Please check the Run ID inside 'mlruns/0/'")
else:
    try:
        # English comments: Load model directly using path
        loaded_model = mlflow.pyfunc.load_model(model_path)
        predictions = loaded_model.predict(df)
        print("\n✅ Predictions successful:")
        print(predictions)
    except Exception as e:
        print(f"❌ Error: {e}")