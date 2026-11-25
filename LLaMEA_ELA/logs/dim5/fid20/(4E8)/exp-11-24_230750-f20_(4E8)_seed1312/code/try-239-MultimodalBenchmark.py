import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical basin components with varying radii
        spherical_basins = 0.0
        for i in range(self.dim):
            radius = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            spherical_basins += (x[i] ** 2) / (radius ** 2)
        
        # Saddle-point corridors with hyperbolic tangent modulation
        saddle_corridors = 0.0
        for i in range(self.dim):
            saddle_corridors += np.tanh(x[i]) * np.sinh(0.5 * x[i]) * np.cos(2 * x[i])
        
        # Log-periodic oscillations with exponential decay
        log_oscillations = 0.0
        for i in range(self.dim):
            if x[i] != 0:
                log_oscillations += np.sin(np.log(np.abs(x[i])) * 3) * np.cos(np.log(np.abs(x[i])) * 2) * np.exp(-0.1 * np.abs(x[i]))
        
        # Cross-dimensional coupling with polynomial interactions (modified)
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x[i] ** 3) * (x[j] ** 2) * np.sin(x[i] + x[j]) * np.cos(0.5 * x[i] * x[j])
        
        # Gaussian ridge structures with varying orientations
        gaussian_ridges = 0.0
        for i in range(self.dim):
            gaussian_ridges += np.exp(-0.5 * (x[i] - np.sin(i)) ** 2) * np.cos(3 * x[i])
        
        # Fractal-like step functions with recursive scaling
        fractal_steps = 0.0
        for i in range(self.dim):
            fractal_steps += np.floor(np.abs(x[i]) * 2) * np.sin(x[i] ** 2)
        
        # Chaotic logistic map component (new addition)
        chaotic_component = 0.0
        r = 3.9 + 0.1 * np.sin(0.1 * sum(x))
        for i in range(self.dim):
            chaotic_component += r * x[i] * (1 - x[i]) * np.cos(i)
        
        # Combined fitness function with dynamic weighting
        return 0.25 * spherical_basins + 0.2 * saddle_corridors + 0.15 * log_oscillations + 0.15 * cross_coupling + 0.1 * gaussian_ridges + 0.08 * fractal_steps + 0.07 * chaotic_component