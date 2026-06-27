import requests
from config import API_KEY

url = "https://afferens.com/api/perception"

headers = {
    "X-API-KEY": API_KEY
}

params = {
    "modality": "vision",
    "limit": 1
}

response = requests.get(url, headers=headers, params=params)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    try:
        objects = data['data'][0]['data']['objects']

        print("\n👁️ LIVE VISION ACTIVE")
        print("📡 Scanning Environment...\n")

        for obj in objects:
            label = obj['label']
            confidence = obj['confidence']

            print(f"- Detected: {label} ({confidence})")

            # 🔥 SMART DECISION ENGINE (WINNER FEATURE)
            if label == "person" and confidence > 0.7:
                print("🔥 HIGH CONFIDENCE HUMAN DETECTED → ALERT MODE ACTIVE")
                print("📡 Sending signal to system...")
                print("💡 Smart Perception System Activated\n")

            elif label == "person":
                print("⚠️ HUMAN DETECTED BUT LOW CONFIDENCE\n")

            else:
                print("🚫 NO HUMAN → SYSTEM IDLE\n")

    except Exception as e:
        print("Error parsing data:", e)

else:
    print("❌ API Error or No Stream Active")