import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

def create_database():
    conn = sqlite3.connect('data_analysis.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    latency REAL,
                    packet_loss REAL)''')
    conn.commit()
    conn.close()

def record_data(latency, packet_loss):
    conn = sqlite3.connect('data_analysis.db')
    c = conn.cursor()
    c.execute('INSERT INTO data (latency, packet_loss) VALUES (?, ?)', (latency, packet_loss))
    conn.commit()
    conn.close()

def train_model():
    conn = sqlite3.connect('data_analysis.db')
    data = pd.read_sql_query("SELECT * FROM data", conn)
    conn.close()

    X = data[['latency']]
    y = data['packet_loss']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def analyze_task_startup(latency, model):
    predicted_packet_loss = model.predict([[latency]])[0]
    if predicted_packet_loss > 10:
        print("High packet loss predicted: ", predicted_packet_loss)
    else:
        print("Packet loss within acceptable range: ", predicted_packet_loss)

def join_data_with_external_source():
    external_data = pd.DataFrame({
        'external_id': [1, 2, 3],
        'external_info': ['info1', 'info2', 'info3']
    })

    conn = sqlite3.connect('data_analysis.db')
    data = pd.read_sql_query("SELECT * FROM data", conn)
    conn.close()

    joined_data = data.merge(external_data, left_on='id', right_on='external_id')
    return joined_data

if __name__ == "__main__":
    create_database()
    record_data(50, 5)  # Example data
    record_data(100, 20)  # Example data

    model = train_model()
    analyze_task_startup(70, model)
    joined_data = join_data_with_external_source()
    print(joined_data)
