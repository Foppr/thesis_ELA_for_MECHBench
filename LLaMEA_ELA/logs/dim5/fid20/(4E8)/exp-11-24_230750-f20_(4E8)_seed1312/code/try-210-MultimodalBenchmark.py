import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal recursive cosine interactions with self-similar patterns
        fractal_cos = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-term interaction
                fractal_cos += np.cos(2 * np.pi * (x[i] + x[j])) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Self-similar basin structures with varying depths
        basin_structure = 0.0
        for i in range(self.dim):
            basin_structure += np.sin(0.5 * x[i]) ** 2 * np.exp(-0.05 * x[i]**2)
        
        # Logarithmic barrier penalties with nested complexity
        log_barrier = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.0:
                log_barrier += np.log(1 + np.abs(x[i]) - 3.0) * np.exp(-0.1 * (x[i] ** 2))
        
        # Recursive sine-wave interactions with diminishing amplitudes
        recursive_sine = 0.0
        amplitude = 1.0
        for i in range(self.dim):
            recursive_sine += amplitude * np.sin(2 ** i * x[i]) * np.exp(-0.02 * i)
            amplitude *= 0.8  # Diminishing amplitude
        
        # Mixed polynomial-trigonometric interactions with adaptive exponents
        mixed_interaction = 0.0
        for i in range(self.dim):
            mixed_interaction += (x[i] ** 3) * np.cos(3 * x[i]) + (x[i] ** 2) * np.sin(2 * x[i])
        
        # Multi-scale Gaussian peaks with varying widths and heights
        gaussian_peaks = 0.0
        for i in range(0, self.dim, 2):  # Every other dimension
            if i < self.dim:
                peak_center = 2.5 * np.sin(i)
                width = 0.5 + 0.3 * np.cos(i)
                height = 1.0 + 0.5 * np.sin(i)
                gaussian_peaks += height * np.exp(-0.5 * ((x[i] - peak_center) ** 2) / (width ** 2))
        
        # Cross-term exponential attraction basins with varying strengths
        cross_attraction = 0.0
        strength = 1.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j]) ** 2 + 1e-8)
                cross_attraction += strength * np.exp(-dist) * np.cos(3 * dist)
                strength *= 0.95  # Slight decay
        
        # Combined fitness with adjusted weights
        return 0.25 * fractal_cos + 0.2 * basin_structure + 0.15 * log_barrier + 0.15 * recursive_sine + 0.1 * mixed_interaction + 0.08 * gaussian_peaks + 0.07 * cross_attraction