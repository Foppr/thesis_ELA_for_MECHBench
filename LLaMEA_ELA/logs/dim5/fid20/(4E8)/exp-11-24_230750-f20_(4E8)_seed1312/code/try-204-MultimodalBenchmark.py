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
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for fractal structure
                fractal_cos += np.cos(2 * np.pi * (x[i] + x[j])) * np.cos(3 * np.pi * (x[i] - x[j]))
        
        # Adaptive radial basis functions with dynamic widths and heights
        rbf_sum = 0.0
        centers = np.linspace(-4.8, 4.8, 9)
        for center in centers:
            width = 0.5 + 0.3 * np.sin(center)
            height = 1.0 + 0.5 * np.cos(center)
            rbf_sum += height * np.exp(-0.5 * np.sum((x - center) ** 2) / (width ** 2))
        
        # Dynamic noise modulation with time-varying amplitude
        noise_amp = 0.1 + 0.05 * np.sin(0.3 * self.dim)
        noise = noise_amp * np.random.normal(0, 1, self.dim)
        dynamic_noise = np.sum(noise * x) * np.exp(-0.01 * np.sum(x ** 2))
        
        # Recursive polynomial coupling with varying exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            exp_factor = 2 + 0.5 * np.sin(i)
            poly_coupling += (x[i] ** exp_factor) * np.sum([x[j] ** (exp_factor - 1) for j in range(i)])
        
        # Multi-scale sinusoidal basin structures with varying frequencies
        basin_structure = 0.0
        frequencies = np.linspace(1, 5, 5)
        for freq in frequencies:
            basin_structure += np.sin(freq * np.sum(x)) * np.cos(freq * np.sum(x ** 2))
        
        # Cross-dimensional exponential attraction basins with adaptive weights
        cross_attraction = 0.0
        weights = np.linspace(0.1, 0.5, self.dim)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j]) ** 2 + 1e-6)
                cross_attraction += weights[i] * weights[j] * np.exp(-dist) * np.sin(3 * dist)
        
        # Chaotic sine-cosine interaction with modified parameters
        chaotic_interaction = 0.0
        for i in range(self.dim):
            chaotic_interaction += np.sin(x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * (x[i] ** 2))
        
        # Combined fitness function with adjusted weights and scaling factors
        return 0.3 * fractal_cos + 0.25 * rbf_sum + 0.15 * dynamic_noise + 0.1 * poly_coupling + 0.1 * basin_structure + 0.05 * cross_attraction + 0.05 * chaotic_interaction