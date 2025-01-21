from pandas import DataFrame, read_csv
import numpy as np

def generate_synthetic_data(num_samples=2000):
    np.random.seed(42)
    
    data = {
        "Machine_ID": np.arange(1, num_samples + 1),
        "Temperature": np.random.normal(80, 10, num_samples).clip(60, 100).round(0),
        "Run_Time": np.random.uniform(50, 500, num_samples).round(0),
        "Torque": np.random.normal(40, 10, num_samples).clip(10, 70).round(1),
        "Tool_Wear": np.random.uniform(0, 200, num_samples).round(0),
    }
    
    data["Downtime_Flag"] = [
        1 if (temp > 90 and runtime > 400) or torque > 60 else 0
        for temp, runtime, torque in zip(
            data["Temperature"], data["Run_Time"], data["Torque"]
        )
    ]
    
    return DataFrame(data)