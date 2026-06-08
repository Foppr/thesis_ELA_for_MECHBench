import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

missing_niche_radius = True


def load_log(exp_name):
    log = []
    with open(f"{exp_name}/log.jsonl", 'r', encoding='utf-8') as f:
        for line in f:
            # Strip whitespace and ignore empty lines if any exist
            if line.strip():
                log.append(json.loads(line))

    max_gen = 0

    if missing_niche_radius:
        for gen in range(50):
            dists = []
            individuals_genX = []
            for individual in log:
                if individual['generation'] > max_gen:
                    max_gen = individual['generation']
                if individual['fitness'] == np.inf:  # Skip for infinity
                    log.remove(individual)
                    continue
                if individual['generation'] == gen:
                    individuals_genX.append(individual)
            for i in range(len(individuals_genX)):
                for j in range(i + 1, len(individuals_genX)):
                    ind1 = individuals_genX[i]
                    ind2 = individuals_genX[j]
                    try:
                        proxy_ela1 = ind1['metadata']['Proxy ELA values']
                        proxy_ela2 = ind2['metadata']['Proxy ELA values']
                        dist = np.sum(np.abs(np.asarray(proxy_ela1) - np.asarray(proxy_ela2)))
                        dists.append(dist)
                    except KeyError:
                        print(ind1['fitness'])
                        print(ind2['fitness'])
                        print(type(ind1['fitness']))
                        print(type(ind2['fitness']))
            niche_radius = float(np.mean(dists))

            for individual in log:
                if individual['generation'] == gen:
                    individual['metadata']['niche_radius'] = niche_radius

    # 1. Convert the list of dictionaries into a Pandas DataFrame
    df_log = pd.DataFrame(log)

    # 2. Group by 'generation' and calculate the required statistics
    # We grab the min, max, and mean of the 'fitness' column for every generation
    df_log = df_log.groupby('generation')['fitness'].agg(['min', 'max', 'mean']).reset_index()

    # Sort by generation just in case the logs are out of order
    df_log = df_log.sort_values('generation')

    # 3. Extract the columns for plotting
    generations = df_log['generation']
    avg_distance = df_log['mean']
    max_avg = max(avg_distance)
    best_distance = df_log['min']
    max_best = max(best_distance)
    ub = max(max_avg, max_best)

    return df_log, max_gen, ub


def plot_evolution_progress(df_log, problems_data, name, minimize=True):
    """
    Plots the best and average raw distance (fitness) across generations
    with the global best distance highlighted in dark green.
    """
    max_gen, ub = problems_data
    df_log = df_log[df_log['generation'] <= max_gen]

    generations = df_log['generation']
    avg_distances = df_log['mean']
    best_distances = df_log['min']

    # --- NEW: Identify the global best (minimum distance) ---
    min_val = best_distances.min()
    # Find the first generation that achieved this minimum
    best_gen = df_log.loc[df_log['min'] == min_val, 'generation'].iloc[0]

    best_label = 'Best Raw Distance (Min)'

    # Set up the plot aesthetics
    plt.figure(figsize=(10, 6))
    plt.style.use('seaborn-v0_8-whitegrid')

    # Plot the lines
    plt.plot(generations, best_distances, label=best_label, color='#1f77b4', linewidth=2.5, marker='o', markersize=4)
    plt.plot(generations, avg_distances, label='Avg Raw Distance', color='#ff7f0e', linewidth=2, linestyle='--')

    # --- NEW: Highlight the absolute best dot ---
    plt.scatter(best_gen, min_val, color='#2ca02c', s=100, zorder=5, label='Global Best')

    # Add text label below the dot
    # We use a small offset (va='top') to place it below the green dot
    plt.text(best_gen, min_val - (ub * 0.02), f'{min_val:.3f}',
             color='#006400', fontweight='bold', ha='center', va='top', fontsize=14)

    plt.ylim(0, ub)

    # Labels and Title
    plt.title(f'LLaMEA Evolutionary Progress (Problem {name[1]})', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Generation', fontsize=12, labelpad=10)
    plt.ylabel('Raw Distance (Fitness)', fontsize=12, labelpad=10)

    # Set X-axis to show integer generation numbers clearly
    plt.xticks(generations)

    # Add a legend and tighten the layout
    plt.legend(fontsize=11, loc='upper right', frameon=True, facecolor='white', edgecolor='none')
    plt.tight_layout()

    # Save and show the graph
    filename = f'llamea_evolution_progress_{name}.png'
    plt.savefig(filename, dpi=300)
    print(f"Graph successfully saved as '{filename}'")
    plt.close()  # Close to free memory between plots


def compare_problem_results(p1_name, p2_name, p3_name):
    log1, max_gen1, ub1 = load_log(p1_name)
    log2, max_gen2, ub2 = load_log(p2_name)
    log3, max_gen3, ub3 = load_log(p3_name)
    max_gen = min(max_gen1, max_gen2, max_gen3)
    ub = max(ub1, ub2, ub3)
    return max_gen, ub


same_scales = "_highlight_minimum"
name1 = "exp-06-04_002048-LLaMEA-qwen3-coder_30b-ELA_for_MECHBENCH"
log_and_data1 = load_log(name1)
name2 = "exp-06-04_122824-LLaMEA-qwen3-coder_30b-ELA_for_MECHBENCH"
log_and_data2 = load_log(name2)
name3 = "exp-06-05_110213-LLaMEA-qwen3-coder_30b-ELA_for_MECHBENCH"
log_and_data3 = load_log(name3)

problem_stats = compare_problem_results(name1, name2, name3)

plot_evolution_progress(log_and_data1[0], problem_stats, name=f"p1_budget800_niche2{same_scales}")
plot_evolution_progress(log_and_data2[0], problem_stats, name=f"p2_budget800_niche2{same_scales}")
plot_evolution_progress(log_and_data3[0], problem_stats, name=f"p3_budget800_niche2{same_scales}")
