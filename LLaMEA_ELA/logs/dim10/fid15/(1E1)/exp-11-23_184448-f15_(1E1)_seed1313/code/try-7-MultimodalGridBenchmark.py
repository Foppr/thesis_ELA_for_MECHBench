import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Add multiple global minima in a grid pattern with chaotic spacing
        grid_minima = 0.0
        for i in range(self.dim):
            # Chaotic grid positions using golden ratio for irregularity
            grid_positions = np.array([-4.0, -2.0, 0.0, 2.0, 4.0])
            # Apply chaotic perturbation to grid positions
            chaotic_positions = grid_positions + 0.5 * np.sin(grid_positions * np.pi / 3)
            distances = np.abs(x[i] - chaotic_positions)
            min_distance = np.min(distances)
            # Exponentially decaying penalty with adaptive rate based on dimension
            decay_rate = 0.1 + 0.2 * (self.dim / 10.0)
            grid_minima += (min_distance ** 2) * np.exp(-decay_rate * min_distance)
        
        # Add chaotic sinusoidal oscillations with varying frequencies and amplitudes
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / self.dim)
            amp = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 1))
            oscillation_term += amp * np.sin(freq * x[i]) * np.cos(1.5 * freq * x[i])
        
        # Add nested quadratic basins with varying depths
        nested_basins = 0.0
        for i in range(self.dim):
            basin_depth = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            center_offset = 2.0 * np.cos(i * np.pi / (self.dim + 1))
            nested_basins += basin_depth * ((x[i] - center_offset) ** 2)
        
        # Add a strong central attraction with chaotic quartic penalty
        center_penalty = 0.0
        for i in range(self.dim):
            # Chaotic penalty centers
            penalty_center = 1.5 * np.sin(i * np.pi / (self.dim + 2))
            center_penalty += ((x[i] - penalty_center) ** 4) + ((x[i] + penalty_center) ** 4)
        
        # Add dimensionality-dependent complexity factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return dim_factor * (base_term + 0.5 * grid_minima + 0.3 * oscillation_term + 0.1 * nested_basins + 0.2 * center_penalty)