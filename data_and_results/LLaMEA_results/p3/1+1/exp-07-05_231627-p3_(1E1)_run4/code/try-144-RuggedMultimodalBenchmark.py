import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Exponentially decaying sinusoidal waves with varying frequencies and amplitudes
        wave_component = np.sum(np.exp(-10 * np.abs(x_norm)) * np.sin(20 * np.pi * x_norm) * 
                               np.cos(15 * np.pi * x_norm) * np.sin(25 * np.pi * x_norm**2))
        
        # Polynomial chaos with high-degree terms and multiple local optima
        poly_component = np.sum((x_norm**9 - 15 * x_norm**7 + 80 * x_norm**5 - 180 * x_norm**3 + 120 * x_norm)**2)
        
        # Cross-dimensional interaction terms with exponential decay
        cross_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_component += np.exp(-5 * np.abs(x_norm[i] - x_norm[j])) * np.sin(10 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Gaussian peaks with varying widths and heights to create rugged terrain
        peak_component = 0
        for i in range(20):
            center = np.random.uniform(-1, 1, self.dim)
            width = np.random.uniform(0.1, 0.5)
            height = np.random.uniform(0.5, 2.0)
            peak_component += height * np.exp(-np.sum(((x_norm - center) / width)**2))
        
        # Fractional power and logarithmic terms to introduce non-smooth behavior
        frac_component = np.sum(np.abs(x_norm)**1.7 + 0.3 * np.log(1 + np.abs(x_norm)))
        
        # Additional harmonic component with varying weights
        harmonic_component = np.sum(np.sin(30 * np.pi * x_norm**3) * np.cos(20 * np.pi * x_norm**3) + 
                                   np.sin(35 * np.pi * x_norm**4) * np.cos(25 * np.pi * x_norm**4))
        
        # Combine all components with different weights
        result = 0.25 * wave_component + 0.35 * poly_component + 0.15 * cross_component + \
                 0.18 * peak_component + 0.08 * frac_component + 0.09 * harmonic_component
        
        # Add controlled noise
        noise = 0.02 * (1 + np.abs(np.sum(x_norm**4))) * np.random.uniform(-1, 1)
        
        return result + noise