A.Title -
Gameplay Analyzer

B.Overview of the Project -
It analyzes the gameplay of the player and helps them improve their gameplay with tips

C.Technologies/Tools used-
•	Python 3.x
•	Matplotlib
•	Statistics module
•	Random module

D.Steps to install and run the project -
Prerequisites--
Before you begin, ensure you have the following installed on your system:
Python: Version 3.6 or higher.
pip: Python's package installer (usually included with Python).

Installation--
This project requires the matplotlib library for generating performance graphs and the built-in statistics module.
Step 1: Install Python Dependencies
Open your terminal or command prompt and run the following command to install matplotlib:
pip install matplotlib

How to Run--
Step 1: Save the Code -- 
Save the entire provided Python code into a file named analyzer.py (or any .py file of your choice).

Step 2: Execute the Script --
Navigate to the directory where you saved the file using your terminal or command prompt, and execute the script with the following command:
python analyzer.py

Step 3: Follow the Prompts -- 
The script will guide you through the input process:
Enter the number of game rounds/sessions you wish to analyze.
Select the game genre by entering the corresponding number (1-5).
For each session, you will be prompted to enter the performance metrics:
Time taken (seconds)
Total actions/moves
Successful actions
Mistakes/Misses
Playstyle (safe/risky)
Difficulty (1-10)
Win/Loss (win/loss)

Step 4: Review the Analysis and Graphs -- 
After all sessions' data have been entered, the script will:
Display the PLAYER ANALYSIS REPORT with various performance indexes.
Show GENRE BASED TIPS relevant to your selected game genre.
Generate and display three graphical plots:
Accuracy Progression
Focus Level Progression
Fatigue Level Progression
You may need to close the graph windows for the script to fully complete its execution.

E. Instructions for testing -
Data Input and Calculation Tests
This uses specific data sets to verify that the core metrics, derived indexes, and trend logic are calculated correctly.

Test Set A: Consistent, High-Performance Session
This set simulates a player with excellent performance and a safe playstyle.

Metric -- Session 1,Session 2,Session 3 

--Expected Outcome Check--
Time taken (s) -- 5.0,5.0,5.0
avg_time should be ≈5.0. 
Pace Style should be Balanced.
Total actions -- 100,100,100,
Successful actions -- 90,95,98,Overall Accuracy should be high (approx. 94.33%). Performance Trend should be Improving Performance.
Mistakes / Misses -- 10,5,2,
Tilt Status should be Stable Mindset (since 2<10).
Playstyle -- safe,safe,safe
Risk Percentage should be 0.0%. 
Aggression Level should be ≈30.
Win/Loss -- win,win,win

Metric -- Session 1,Session 2,Session 3 

--Expected Outcome Check--
Time taken (s) -- 12.0,15.0,18.0
avg_time should be ≈15.0. 
Pace Style should be Slow Tactical.
Total actions -- 50,50,50,
Successful actions -- 45,30,20
Performance Trend should be Declining Performance (Accuracy 90%→40%).
Mistakes / Misses -- 5,20,30 
Tilt Status should be Psychological Tilt Detected (since 30>5).
Playstyle -- risky,risky,safe 
Risk Percentage should be 66.67%.

Key Output Checks--
After running Test Set A and B, check the following sections in the final report:
Pace Style: Must match the expected outcome based on avg_time.
Performance Trend: Must match the expected outcome based on the change in accuracy (accuracies[-1] vs. accuracies[0]).
Tilt Status: Must match the expected outcome based on the change in mistakes (mistakes[-1] vs. mistakes[0]).
Error Recovery: For Test Set B, check if it correctly identifies Poor recovery (since accuracy dropped from Session 1 to 2 after mistakes were made).

Visual Output Test
This phase confirms that the graphs display correctly.
Run with any data set (e.g., Test Set A).
Confirm Graph Appearance: Three separate windows should appear, each containing a line graph:
-Accuracy Progression: Should show an upward trend for Test Set A.
-Focus Level Progression: Should show an upward trend for Test Set A (as mistakes decreased).
-Fatigue Level Progression: Should show a clear upward trend from session 1 to n.
Close Graphs: Ensure the script returns to the command line after all graph windows are closed.

Genre Tips Test
Rerun the script, choosing a different genre number each time (1 through 5).

Verify that the GENRE BASED TIPS section displays the correct, corresponding tips for the selected genre. For example, selecting 2. Fighting must show tips like "Master combo chains and frame timing" and "Improve block and counter mechanics."
