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

        print("\n👁️ Detected Objects:\n")

        for obj in objects:
            label = obj['label']
            confidence = obj['confidence']

            print(f"- {label} ({confidence})")

            # 🔥 ACTION PART (IMPORTANT)
            if label == "person":
                print("👤 HUMAN DETECTED → SYSTEM ACTIVE MODE 🔥")
            else:
                print("🚫 NO HUMAN → SYSTEM IDLE")

    except Exception as e:
        print("Error parsing data:", e)

else:
    print("❌ API Error or No Stream Active")