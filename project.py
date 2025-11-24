import matplotlib.pyplot as plt
import random
import statistics

print("GAME PERFORMANCE ANALYZER\n")

n = int(input("Enter number of game rounds / sessions : "))

if n <= 0:
    print("Number of rounds must be greater than 0")
    exit()

print("\nChoose Game Genre:")
print("1. Shooter")
print("2. Fighting")
print("3. RPG")
print("4. Strategy")
print("5. Open World")

genre_choice = int(input("Enter genre number: "))

genre_map = {
    1: "Shooter",
    2: "Fighting",
    3: "RPG",
    4: "Strategy",
    5: "Open World"
}

genre = genre_map.get(genre_choice, "Shooter")
print(f"Selected Genre: {genre}")

# DATA STORAGE

times = []
moves = []
corrects = []
mistakes = []
difficulties = []
risks = []
results = []
accuracies = []
reaction_speed = []
focus_level = []
fatigue_level = []
aggression_index = []
combo_efficiency = []
map_awareness = []
stamina_control = []
exploration_score = []
mental_stability = []
decision_quality = []
strategy_score = []
genre_scores = []

# MANUAL INPUT SYSTEM

for i in range(n):
    print(f"\nSESSION {i+1}")

    t = float(input("Time taken (seconds): "))
    m = int(input("Total actions/moves: "))
    c = int(input("Successful actions: "))
    ms = int(input("Mistakes / Misses: "))
    r = input("Playstyle (safe/risky): ").lower()
    d = int(input("Difficulty (1-10): "))
    res = input("Win/Loss: ").lower()

    times.append(t)
    moves.append(m)
    corrects.append(c)
    mistakes.append(ms)
    risks.append(r)
    difficulties.append(d)
    results.append(res)

    if m == 0:
        acc = 0
    else:
        acc = (c / m) * 100

    accuracies.append(acc)
    reaction_speed.append(round((1 / t) * 120, 2))
    focus_level.append(max(0, 100 - (ms * 5)))
    fatigue_level.append(min(100, (i + 1) * 10))
    aggression_index.append(85 if r == "risky" else 30)
    combo_efficiency.append(round((c / (m + 1)) * 100, 2))
    map_awareness.append(round(random.uniform(40, 95), 2))
    stamina_control.append(round(random.uniform(50, 100), 2))
    exploration_score.append(round(random.uniform(30, 100), 2))
    mental_stability.append(round(random.uniform(40, 100), 2))
    decision_quality.append(round(random.uniform(45, 100), 2))
    strategy_score.append(round(random.uniform(35, 95), 2))

    # Genre Performance Score
    genre_score = (acc + strategy_score[-1] + focus_level[-1]) / 3
    genre_scores.append(round(genre_score, 2))

# CORE ANALYSIS

avg_time = statistics.mean(times)
consistency = statistics.pstdev(times)
overall_accuracy = (sum(corrects) / sum(moves)) * 100
risk_rate = (risks.count("risky") / n) * 100

if avg_time < 5:
    pace = "Hyper Fast"
elif avg_time < 10:
    pace = "Balanced"
else:
    pace = "Slow Tactical"

if mistakes[-1] > mistakes[0]:
    tilt = "Psychological Tilt Detected"
else:
    tilt = "Stable Mindset"

if accuracies[-1] > accuracies[0]:
    trend = "Improving Performance"
else:
    trend = "Declining Performance"

# Error Recovery
error_recovery = "Poor"
for i in range(1, n):
    if mistakes[i-1] > 0 and accuracies[i] > accuracies[i-1]:
        error_recovery = "Strong"

# Advanced Indexes
focus_index = statistics.mean(focus_level)
fatigue_index = statistics.mean(fatigue_level)
aggression_avg = statistics.mean(aggression_index)
combo_mastery = statistics.mean(combo_efficiency)
map_mastery = statistics.mean(map_awareness)
stamina_mastery = statistics.mean(stamina_control)
strategy_avg = statistics.mean(strategy_score)
mental_avg = statistics.mean(mental_stability)
decision_avg = statistics.mean(decision_quality)
skill_growth = accuracies[-1] - accuracies[0]

best_genre_score = statistics.mean(genre_scores)

# FINAL REPORT

print("\n================ PLAYER ANALYSIS REPORT ================")
print("Game Genre:", genre)
print("Overall Accuracy:", round(overall_accuracy, 2), "%")
print("Consistency Score:", round(consistency, 2))
print("Pace Style:", pace)
print("Tilt Status:", tilt)
print("Performance Trend:", trend)
print("Error Recovery:", error_recovery)
print("Risk Percentage:", round(risk_rate, 2), "%")
print("Focus Index:", round(focus_index, 2))
print("Fatigue Index:", round(fatigue_index, 2))
print("Aggression Level:", round(aggression_avg, 2))
print("Combo Mastery:", round(combo_mastery, 2))
print("Map Awareness:", round(map_mastery, 2))
print("Stamina Control:", round(stamina_mastery, 2))
print("Strategy Rating:", round(strategy_avg, 2))
print("Mental Stability:", round(mental_avg, 2))
print("Decision Quality:", round(decision_avg, 2))
print("Skill Growth Index:", round(skill_growth, 2))
print("Genre Performance Score:", round(best_genre_score, 2))
print("========================================================")

# GENRE SPECIFIC TIPS

print("\n============= GENRE BASED TIPS =============")

if genre == "Shooter":
    print("- Improve headshot precision and reaction timing")
    print("- Practice recoil control and strafing")
    print("- Pre-aim corners for advantage")

elif genre == "Fighting":
    print("- Master combo chains and frame timing")
    print("- Improve block and counter mechanics")
    print("- Understand character matchups")

elif genre == "RPG":
    print("- Focus on balanced skill upgrades")
    print("- Explore side quests for XP boost")
    print("- Optimize gear and inventory")

elif genre == "Strategy":
    print("- Improve resource management")
    print("- Predict opponent tactics")
    print("- Strengthen early-game planning")

elif genre == "Open World":
    print("- Increase exploration efficiency")
    print("- Balance main and side missions")
    print("- Improve navigation skills")

print("===========================================")

# VISUAL GRAPHS

rounds = list(range(1, n + 1))

plt.figure()
plt.plot(rounds, accuracies)
plt.title("Accuracy Progression")
plt.xlabel("Session")
plt.ylabel("Accuracy %")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(rounds, focus_level)
plt.title("Focus Level Progression")
plt.xlabel("Session")
plt.ylabel("Focus Index")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(rounds, fatigue_level)
plt.title("Fatigue Level Progression")
plt.xlabel("Session")
plt.ylabel("Fatigue Index")
plt.grid(True)
plt.show()
