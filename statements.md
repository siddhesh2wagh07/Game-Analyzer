1. Problem Statement 
Competitive and casual gamers lack a simple, automated tool to systematically track and analyze their performance over multiple playing sessions. Currently, insights into consistency, psychological trends (like tilt and fatigue), and core skill metrics (like accuracy and reaction speed) are fragmented or rely on manual, complex calculations. This makes it difficult for players to identify specific weaknesses, measure skill growth, and receive targeted, actionable advice to improve their gameplay.

2. Scope of the Project
The scope of this project is to create a lightweight, terminal-based application that processes manual session inputs and provides a comprehensive, data-driven analysis.

In Scope:
Manual input system for core session data (time, moves, success rate, mistakes, difficulty, win/loss).
Calculation of derived metrics (e.g., Accuracy, Reaction Speed, Focus Index, Skill Growth).
High-level analytical output (Trend, Tilt Status, Pace Style, Error Recovery).
Basic data visualization using line graphs for key metrics (Accuracy, Focus, Fatigue).
Genre-specific advice and performance scoring based on user selection.

Out of Scope (Future Enhancements):
Direct API integration with real-world games for automatic data retrieval.
Advanced statistical modeling (e.g., regression analysis).
Web or Graphical User Interface (GUI) development.
Persistent data storage (e.g., databases or permanent log files).

3. Target User
The primary target users are competitive and dedicated casual video gamers who want to seriously track and improve their performance.
Individuals: Players focused on self-improvement in their chosen game genre (e.g., eSports enthusiasts, Fighting Game players, Strategy gamers).
Coaches/Analysts (Secondary): Individuals who may use the tool to manually log and analyze client or team performance in a simple, portable format.
Users comfortable with terminal/command line interfaces.

4. High-Level Features
The Game Performance Analyzer offers the following core capabilities:
Data Acquisition	-- Allows users to manually input key performance metrics for multiple sequential game sessions.
Core Metric Calculation	-- Calculates essential performance indicators like Overall Accuracy, Consistency Score, and Risk Percentage.
Psychological & Trend Analysis	-- Automatically derives and reports non-technical factors such as Tilt Status, Focus Index, Fatigue Index, and Performance Trend (Improving/Declining).
Advanced Indexing	-- Provides quantified ratings for factors like Combo Mastery, Map Awareness, Strategy Rating, and Decision Quality.
Visual Reporting --	Generates and displays intuitive line graphs for Accuracy, Focus, and Fatigue progression over sessions.
Genre-Specific Guidance	-- Offers tailored, actionable tips based on the selected game genre (Shooter, RPG, Strategy, etc.).
