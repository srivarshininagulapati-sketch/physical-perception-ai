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

# -----------------------------
# ACTION LAYER
# -----------------------------
def perform_action(label, confidence):
    if label == "person" and confidence > 0.7:
        print("🔊 ACTION: ALERT TRIGGERED")
        print("📢 Human detected with high confidence!")
        print("💡 Smart Perception System Activated\n")

    elif label == "person":
        print("⚠️ ACTION: Human detected (low confidence)\n")

    else:
        print("🟢 ACTION: System idle - safe environment\n")


# -----------------------------
# API CALL FUNCTION
# -----------------------------
def get_data():
    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        print("Status Code:", response.status_code)

        if response.status_code != 200:
            return None

        return response.json()

    except Exception as e:
        print("⚠️ API ERROR:", e)
        return None


# -----------------------------
# MAIN LOGIC
# -----------------------------
data = get_data()

if data:
    try:
        objects = (
            data.get('data', [{}])[0]
            .get('data', {})
            .get('objects', [])
        )

        print("\n👁️ LIVE VISION ACTIVE")
        print("📡 Scanning Environment...\n")

        if not objects:
            print("🚫 No objects detected\n")

        for obj in objects:
            label = obj.get('label', 'unknown')
            confidence = obj.get('confidence', 0)

            print(f"- Detected: {label} ({confidence})")

            perform_action(label, confidence)

    except Exception as e:
        print("❌ PARSE ERROR:", e)

else:
    # -----------------------------
    # FALLBACK MODE (VERY IMPORTANT)
    # -----------------------------
    print("\n⚠️ API NOT AVAILABLE - SWITCHING TO FALLBACK MODE")

    fallback_objects = [
        {"label": "person", "confidence": 0.85},
        {"label": "chair", "confidence": 0.90}
    ]

    print("\n👁️ SIMULATED VISION ACTIVE")
    print("📡 Running fallback perception...\n")

    for obj in fallback_objects:
        print(f"- Detected: {obj['label']} ({obj['confidence']})")
        perform_action(obj['label'], obj['confidence'])