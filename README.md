Hill-Climbing Algorithm Educational Demo
(Group 24 — Tyler Kasniak, James Kibrick, Jeffrey Peralta)

This repository contains an interactive educational demo showcasing several variants of the Hill-Climbing
local search algorithm applied to real-world terrain data. The project’s purpose is to help students and
educators visualize how different hill-climbing strategies behave when navigating elevation landscapes.
The demo uses the Open-Elevation API to fetch actual terrain coordinates and outputs both visualizations
and performance summaries of each algorithm.

Project Goals
The demo aims to:
1. Implement multiple hill-climbing variants (simple, stochastic, random-restart).
2. Visualize how each algorithm traverses terrain.
3. Provide useful statistics such as number of steps, start/end elevation, and success at reaching a peak.
4. Serve as a reusable educational tool for students learning local search and optimization.

Background
Hill-Climbing is a greedy local search procedure typically used to find local maxima or minima in optimization
problems. Variants differ in how they explore neighbors:
A. Simple Hill-Climbing — moves to the first improving neighbor.
B. Steepest-Ascent — evaluates all neighbors but may still get stuck in a local max.
C. Stochastic — selects random neighbors, often escaping traps.
D. Random-Restart — performs multiple climbs to avoid local optima.
These strategies are widely used in ML hyperparameter tuning, robotics pathfinding, logistics optimization, and scheduling.

Features
1. Hill-Climbing Algorithm Code
- Python implementations of all required algorithm variants. These form the core logic of the demo.
2. Visualization Module
Tools to display algorithm traversal:
- iteration-by-iteration plots
- path lines
- animated climbs
3. Performance Summary
Generated statistics such as:
- Number of steps taken
- Starting vs. ending elevation
- Whether a peak was reached
- Comparison across algorithms or terrains

Data Source
The program fetches terrain elevation data using Open-Elevation API
This free service provides real-world coordinates that allow algorithms to climb actual terrain.

