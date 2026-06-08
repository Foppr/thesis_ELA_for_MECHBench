import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

exp_name = "exp-06-04_002048-LLaMEA-qwen3-coder_30b-ELA_for_MECHBENCH"
problem = 'p1'

log = []
with open(f"{exp_name}/log.jsonl", 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            log.append(json.loads(line))

# Sorting ascending because lower fitness means lower raw distance (better)
sorted_log = sorted(log, key=lambda x: x['fitness'])
top_5_individuals = sorted_log[:5]

# Loop through the top 5 entries
for rank, individual in enumerate(top_5_individuals, start=1):
    best_code = individual['code']
    fitness_score = individual['fitness']
    print(f"\nProcessing Rank {rank} (Fitness: {fitness_score:.4f})...")

    # Isolate everything from "class landscape" onwards
    class_start_idx = best_code.find("class landscape:")

    if class_start_idx != -1:
        clean_class_code = best_code[class_start_idx:]

        # Execute and inject into globals (overwriting the previous 'landscape' class)
        exec(clean_class_code, globals())
    else:
        print(f"Could not find the landscape class declaration for Rank {rank}. Skipping.")
        continue

    # Instantiate the newly injected class
    ls = landscape(dim=5)
    lower_bound, upper_bound = -5.0, 5.0
    resolution = 400

    # ==========================================
    # 1. GENERATE 2D GRAPH (Line Plot)
    # ==========================================
    plt.figure(figsize=(10, 5))
    plt.style.use('seaborn-v0_8-whitegrid')

    x1_vals = np.linspace(lower_bound, upper_bound, resolution)
    y_2d = []

    for x1 in x1_vals:
        input_vector = np.array([x1, 0.0, 0.0, 0.0, 0.0])
        y_2d.append(ls.f(input_vector))

    plt.plot(x1_vals, y_2d, color='#1f77b4', linewidth=1.5)
    plt.title(f'2D Slice of Landscape [Rank {rank}, Fit: {fitness_score:.3f}]\n($x_0$ varying, $x_{{1..4}}=0$)',
              fontsize=12, fontweight='bold')
    plt.xlabel('$x_0$', fontsize=10)
    plt.ylabel('f(x)', fontsize=10)
    plt.tight_layout()

    # Appended rank to the filename to avoid overwrites
    plt.savefig(f'proxy_graphs/{problem}_landscape_2d_rank{rank}.png', dpi=300)
    plt.close()  # Close figure to free memory

    # ==========================================
    # 2. GENERATE 3D GRAPH (Surface Plot)
    # ==========================================
    resolution_3d = 150
    x_grid = np.linspace(lower_bound, upper_bound, resolution_3d)
    y_grid = np.linspace(lower_bound, upper_bound, resolution_3d)
    X, Y = np.meshgrid(x_grid, y_grid)

    Z = np.zeros_like(X)

    # Using fixed tuple index loops
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            input_vector = np.array([X[i, j], Y[i, j], 0.0, 0.0, 0.0])
            Z[i, j] = ls.f(input_vector)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)

    ax.set_title(f'3D Surface Slice of Landscape [Rank {rank}, Fit: {fitness_score:.3f}]\n($x_0, x_1$ varying)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('$x_0$', fontsize=11)
    ax.set_ylabel('$x_1$', fontsize=11)
    ax.set_zlabel('f(x)', fontsize=11)

    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, pad=0.1)
    ax.view_init(elev=30, azim=135)

    plt.tight_layout()

    # Appended rank to the filename to avoid overwrites
    plt.savefig(f'proxy_graphs/{problem}_landscape_3d_rank{rank}.png', dpi=300)
    plt.close()  # Close figure to free memory

print("\nAll 5 landscape pairs generated successfully!")