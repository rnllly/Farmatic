import tkinter as tk
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("sample-database-42c3b-firebase-adminsdk-fbsvc-95a98bbb64.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
plant_ref = db.collection("Farmatic").document("Readings")

sensor_data = {
    "Moisture": "45%",
    "Temperature": "23°C",
    "Humidity": "60%",
    "Light": "350 lux"
}

def fetch_data_from_firebase():
    try:
      plant_data = plant_ref.get().to_dict()
      if plant_data:
          sensor_data["Moisture"] = plant_data.get("Moisture")
          sensor_data["Temperature"] = plant_data.get("Temperature")
          sensor_data["Humidity"] = plant_data.get("Humidity")
          sensor_data["Light"] = plant_data.get("Light")
    except Exception as e:
        print(f"Error fetching data form Firebase: {e}")
    update_values()

def update_values():
    moisture_var.set(sensor_data["Moisture"])
    temperature_var.set(sensor_data["Temperature"])
    humidity_var.set(sensor_data["Humidity"])
    light_var.set(sensor_data["Light"])
        
root = tk.Tk()
root.title("Farmatic Sensor Monitor")
root.geometry("300x300")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12), padding=5)

moisture_var = tk.StringVar()
temperature_var = tk.StringVar()
humidity_var = tk.StringVar()
light_var = tk.StringVar()

ttk.Label(root, text="Moisture:").pack(anchor="w")
ttk.Label(root, textvariable=moisture_var).pack(anchor="w")

ttk.Label(root, text="Temperature:").pack(anchor="w")
ttk.Label(root, textvariable=temperature_var).pack(anchor="w")

ttk.Label(root, text="Humidity:").pack(anchor="w")
ttk.Label(root, textvariable=humidity_var).pack(anchor="w")

ttk.Label(root, text="Light Level:").pack(anchor="w")
ttk.Label(root, textvariable=light_var).pack(anchor="w")


ttk.Button(root, text="Refresh", command=update_values).pack(pady=10)

fetch_data_from_firebase()

def auto_refresh():
    fetch_data_from_firebase()
    root.after(5000, auto_refresh)  

auto_refresh()

root.mainloop()