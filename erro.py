import cv2
import numpy as np
import matplotlib.pyplot as plt
import folium

# -----------------------------
# 📁 Load Image
# -----------------------------
image_path = "C:/Users/saile/OneDrive/Pictures/Screenshots/map7.png"
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

# Resize for faster processing
img = cv2.resize(img, (600, 600))

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# -----------------------------
# 🎯 Color Detection
# -----------------------------

# 🌳 Trees (Green)
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# 🏢 Buildings (White/Gray)
lower_building = np.array([0, 0, 70])
upper_building = np.array([180, 50, 255])
mask_building = cv2.inRange(hsv, lower_building, upper_building)

# 🛣️ Roads (Brown/Orange)
lower_road = np.array([10, 100, 20])
upper_road = np.array([25, 255, 200])
mask_road = cv2.inRange(hsv, lower_road, upper_road)

# 💧 Water (Blue)
lower_water = np.array([90, 50, 50])
upper_water = np.array([130, 255, 255])
mask_water = cv2.inRange(hsv, lower_water, upper_water)

# -----------------------------
# 📊 Percentage Calculation
# -----------------------------
total_pixels = img.shape[0] * img.shape[1]

green_pixels = np.sum(mask_green > 0)
building_pixels = np.sum(mask_building > 0)
road_pixels = np.sum(mask_road > 0)
water_pixels = np.sum(mask_water > 0)

tree_percent = (green_pixels / total_pixels) * 100
building_percent = (building_pixels / total_pixels) * 100
road_percent = (road_pixels / total_pixels) * 100
water_percent = (water_pixels / total_pixels) * 100

# -----------------------------
# 🌍 Pollution Index
# -----------------------------
pollution_index = (
        (building_percent * 0.5) +
        (road_percent * 0.3) -
        (tree_percent * 0.4)
)

# -----------------------------
# 🚦 Pollution Level
# -----------------------------
if pollution_index > 50:
    pollution_level = "HIGH"
    color = "red"
elif pollution_index > 25:
    pollution_level = "MODERATE"
    color = "orange"
else:
    pollution_level = "LOW"
    color = "green"

# -----------------------------
# 🌱 Suggestions
# -----------------------------
if tree_percent < 20:
    suggestion = "Plant more trees urgently 🌳"
elif tree_percent < 40:
    suggestion = "Increase green cover 🌿"
else:
    suggestion = "Environment is healthy 🌍"

# -----------------------------
# 🖨️ Print Output
# -----------------------------
print("\n===== ANALYSIS RESULT =====")
print(f"Tree Coverage: {tree_percent:.2f}%")
print(f"Building Coverage: {building_percent:.2f}%")
print(f"Road Coverage: {road_percent:.2f}%")
print(f"Water Coverage: {water_percent:.2f}%")

print(f"\nPollution Index: {pollution_index:.2f}")
print(f"Pollution Level: {pollution_level}")
print(f"Suggestion: {suggestion}")

print(f"\n===== GRAPH COLORS =====")
print("🌳 Trees (Green)")
print("🏢 Buildings & Roads (Red)")
print("🛣️ Land with soil shown as satellite image")
print("💧 Water (Blue)")

# -----------------------------
# 🎨 Visualization (Image)
# -----------------------------
result = img.copy()

result[mask_green > 0] = [0, 255, 0]      # Green
result[mask_building > 0] = [0, 0, 255]   # Red
result[mask_road > 0] = [0, 165, 255]     # Orange
result[mask_water > 0] = [255, 0, 0]      # Blue

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(1,2,2)
plt.title("Detected Areas")
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

plt.show()





