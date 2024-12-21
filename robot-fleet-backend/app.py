from flask import Flask, jsonify
import random
import time
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
# Enable CORS for WebSocket connections (allow connections from localhost:3000)
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)



# Load robot data from JSON
robots = [
    {
        "Robot ID": "63e06a27-8fb5-49b6-afdd-555d6a01f131",
        "Online/Offline": False,
        "Battery Percentage": 40,
        "CPU Usage": 25,
        "RAM Consumption": 5514,
        "Last Updated": "2024-12-11 11:19:51",
        "Location Coordinates": [34.946804, -1.265231],
    },
    {
        "Robot ID": "fbe83522-ea53-4869-97cb-d8cb40007f83",
        "Online/Offline": False,
        "Battery Percentage": 59,
        "CPU Usage": 77,
        "RAM Consumption": 6243,
        "Last Updated": "2024-12-11 10:50:10",
        "Location Coordinates": [13.700687, -50.895561],
    },
    {
        "Robot ID": "ab465182-3288-4d91-a2bf-3b7448d1b9f0",
        "Online/Offline": False,
        "Battery Percentage": 60,
        "CPU Usage": 34,
        "RAM Consumption": 3845,
        "Last Updated": "2024-12-11 10:41:02",
        "Location Coordinates": [
            31.0267,
            56.005055
        ]
    },
    {
        "Robot ID": "96881d11-7a06-4275-b64b-ad26f935111a",
        "Online/Offline": False,
        "Battery Percentage": 65,
        "CPU Usage": 13,
        "RAM Consumption": 7000,
        "Last Updated": "2024-12-11 10:55:50",
        "Location Coordinates": [
            -54.823863,
            -2.796469
        ]
    },
    {
        "Robot ID": "225b4c2b-12c7-4649-a61e-5fde5e96c555",
        "Online/Offline": True,
        "Battery Percentage": 28,
        "CPU Usage": 31,
        "RAM Consumption": 7007,
        "Last Updated": "2024-12-11 10:49:20",
        "Location Coordinates": [
            -2.136094,
            56.199452
        ]
    },
    {
        "Robot ID": "ff812149-19ff-4004-9206-f4d467637493",
        "Online/Offline": False,
        "Battery Percentage": 33,
        "CPU Usage": 96,
        "RAM Consumption": 1246,
        "Last Updated": "2024-12-11 11:10:16",
        "Location Coordinates": [
            -63.665718,
            -121.737855
        ]
    },
    {
        "Robot ID": "b8160337-3440-4bae-a40f-b4aa8f8c25ad",
        "Online/Offline": True,
        "Battery Percentage": 3,
        "CPU Usage": 0,
        "RAM Consumption": 1246,
        "Last Updated": "2024-12-11 11:10:52",
        "Location Coordinates": [
            -20.683334,
            94.293747
        ]
    },
    {
        "Robot ID": "14acff23-8ed3-4152-9047-a50a0a30a69f",
        "Online/Offline": False,
        "Battery Percentage": 19,
        "CPU Usage": 78,
        "RAM Consumption": 1544,
        "Last Updated": "2024-12-11 10:47:26",
        "Location Coordinates": [
            -12.732148,
            -26.722574
        ]
    },
    {
        "Robot ID": "2cbeaa95-9f63-4721-9b84-3e9b08745d7a",
        "Online/Offline": False,
        "Battery Percentage": 37,
        "CPU Usage": 14,
        "RAM Consumption": 2960,
        "Last Updated": "2024-12-11 11:26:34",
        "Location Coordinates": [
            -51.457729,
            19.688121
        ]
    },
    {
        "Robot ID": "e099243f-820a-4d4d-bc90-e60d4f9e5cdb",
        "Online/Offline": True,
        "Battery Percentage": 68,
        "CPU Usage": 51,
        "RAM Consumption": 2228,
        "Last Updated": "2024-12-11 10:41:07",
        "Location Coordinates": [
            -60.499743,
            133.44173
        ]
    },
    
]

@app.route("/robots", methods=["GET"])
def get_robots():
    # Simulate real-time updates
    for robot in robots:
        robot["Battery Percentage"] = max(0, robot["Battery Percentage"] - random.randint(0, 5))
        robot["CPU Usage"] = random.randint(10, 100)
        robot["RAM Consumption"] = random.randint(5000, 8000)
        robot["Online/Offline"] = random.choice([True, False])
        robot["Last Updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Emit robot data over WebSocket
    socketio.emit('robot_data', robots)

    return jsonify(robots)

if __name__ == "__main__":
    socketio.run(app, debug=True)