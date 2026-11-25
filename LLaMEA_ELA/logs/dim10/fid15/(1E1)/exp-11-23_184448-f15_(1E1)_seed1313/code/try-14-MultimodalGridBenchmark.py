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
            freq = 1.5 + 2.5 * np.sin(i * np.pi / self.dim)  # Slightly reduced frequency range
            amp = 1.2 + 0.3 * np.cos(i * np.pi / (self.dim + 1))  # Adjusted amplitude
            oscillation_term += amp * np.sin(freq * x[i]) * np.cos(1.5 * freq * x[i])
        
        # Add nested quadratic basins with varying depths
        nested_basins = 0.0
        for i in range(self.dim):
            basin_depth = 0.3 + 0.7 * np.sin(i * np.pi / self.dim)  # Modified depth range
            center_offset = 1.5 * np.cos(i * np.pi / (self.dim + 1))
            nested_basins += basin_depth * ((x[i] - center_offset) ** 2)
        
        # Add a strong central attraction with chaotic quartic penalty
        center_penalty = 0.0
        for i in range(self.dim):
            # Chaotic penalty centers
            penalty_center = 1.8 * np.sin(i * np.pi / (self.dim + 2))
            center_penalty += ((x[i] - penalty_center) ** 4) + ((x[i] + penalty_center) ** 4)
        
        # Add dimensionality-dependent complexity factor
        dim_factor = 1.0 + 0.25 * np.log(self.dim + 1)  # Slightly reduced complexity factor
        
        # Introduce cross-dimensional interaction terms for increased complexity
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.15 * np.sin(x[i] * x[j]) * (i + j) / (self.dim ** 2)  # Increased interaction strength
        
        # Add fractal-like nested oscillations
        fractal_oscillations = 0.0
        for i in range(self.dim):
            for k in range(1, 6):
                fractal_oscillations += (0.1 * k) * np.sin(k * x[i]) * np.cos(k * x[i] * 0.5)
        
        # Add chaotic coupling between dimensions
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling += 0.2 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (i * j) / (self.dim ** 2)
        
        # Add exponentially decaying radial terms
        radial_term = 0.0
        for i in range(self.dim):
            radial_term += 0.15 * np.exp(-0.5 * (x[i] ** 2)) * np.sin(3 * x[i])
        
        return dim_factor * (base_term + 0.5 * grid_minima + 0.35 * oscillation_term + 0.15 * nested_basins + 0.25 * center_penalty + 0.15 * interaction_term + 0.2 * fractal_oscillations + 0.1 * chaotic_coupling + 0.1 * radial_term)