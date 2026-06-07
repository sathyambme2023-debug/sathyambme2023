# Usage

This document describes how to run the provided simulations and reproduce the benchmarking results.

Prerequisites
- Python 3.8+
- Virtual environment activated
- Dependencies installed: `pip install -r requirements.txt`

Quick demo
1. Run the simulation module (CLI):

```bash
python -m src.simulation
```

2. To reproduce notebook results, open the notebooks and run all cells in order using Jupyter Notebook or JupyterLab.

Advanced
- Use `nbconvert` to execute notebooks headless:

```bash
jupyter nbconvert --to notebook --execute Control_System_Diagnostic_Notebook.ipynb --output Control_System_Diagnostic_Notebook_executed.ipynb
jupyter nbconvert --to notebook --execute Robotic_Arm_Design_Simulation.ipynb --output Robotic_Arm_Design_Simulation_executed.ipynb
```

Data and plots
- The simulation saves a `simulation_results.png` file in the project root when notebooks are executed.
