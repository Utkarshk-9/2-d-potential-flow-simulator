# 2-d-potential-flow-simulator
Author:- Utkarsh Singh — Computational Aerospace Engineering student. Self-directed researcher building physics simulations from first principles.

2D Potential Flow Simulator — NACA Airfoil
Overview

This project implements a 2D potential flow simulator to visualize airflow around a NACA 4-digit airfoil. It combines basic aerodynamic theory with numerical visualization to simulate velocity fields, pressure distribution, and streamline behavior.

The simulation includes:

Airfoil geometry generation (NACA 4-digit)

Uniform freestream flow

Controlled circulation to approximate lift

Pressure coefficient (Cp) computation

Animated streamlines using Matplotlib

Features:

Generate any NACA 4-digit airfoil (e.g., 2412)

Apply angle of attack through geometric rotation

Simulate airflow using potential flow theory

Visualize pressure distribution (Cp contours)

Animate streamlines to mimic airflow motion

Mask solid airfoil region for physical consistency

Physics Background

The simulation is based on:

Potential Flow Theory (inviscid, irrotational flow)

Superposition Principle (uniform flow + circulation)

Circulation Concept to approximate lift behavior

Bernoulli’s Principle for pressure calculation

Note: This is not a full CFD solver. Effects like viscosity, turbulence, and boundary layers are not modeled.

Project Structure
main.py

Key components inside the code:

Airfoil generation

Flow field setup

Circulation modeling

Pressure coefficient calculation

Airfoil masking

Animation and visualization

Installation

Make sure you have Python 3 installed.

Install required libraries:

pip install numpy matplotlib
Usage

Run the script:

python main.py

An animation window will open showing:

Airflow moving around the airfoil

Pressure distribution (color map)

Streamlines evolving over time

Customization

You can modify:

Airfoil

generate_naca("2412")

Angle of Attack

alpha = np.deg2rad(-20)

Freestream Velocity

U = 140.0

Circulation Strength

Gamma = -1.5

Output


The simulation produces:

Animated airflow visualization

Pressure contour field (Cp)

Streamline behavior around the airfoil

Limitations:-
Inviscid flow assumption (no viscosity)

No turbulence modeling

Circulation is manually controlled (not solved via Kutta condition)

Not suitable for real engineering predictions




