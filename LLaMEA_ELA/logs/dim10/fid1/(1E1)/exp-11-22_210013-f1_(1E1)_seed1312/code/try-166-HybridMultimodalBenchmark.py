import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term with increasing degree
        polynomial = 0.0
        for i in range(self.dim):
            polynomial += 0.1 * x[i]**4 + 0.05 * x[i]**3
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            trigonometric += 2.0 * np.sin(3 * x[i]) * np.cos(2 * x[(i + 1) % self.dim])
            trigonometric += 1.5 * np.cos(4 * x[i]) * np.sin(5 * x[(i + 2) % self.dim])
            trigonometric += 0.8 * np.sin(6 * x[i]) * np.cos(7 * x[(i + 3) % self.dim])
        
        # Exponential interaction terms creating steep gradients
        exponential = 0.0
        for i in range(self.dim):
            exponential += 1.2 * np.exp(-0.5 * (x[i] - 1)**2) * np.sin(3 * x[(i + 1) % self.dim])
            exponential += 0.9 * np.exp(-0.3 * (x[i] + 2)**2) * np.cos(4 * x[(i + 2) % self.dim])
        
        # Cross-term interactions with high conditioning
        cross_terms = 0.0
        for i in range(self.dim):
            cross_terms += 1.5 * x[i] * x[(i + 1) % self.dim] * np.sin(2 * x[i])
            cross_terms += 0.7 * x[i]**2 * x[(i + 2) % self.dim] * np.cos(3 * x[(i + 1) % self.dim])
        
        # Global structure with multiple basins
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += 0.5 * (x[i] - 3)**6
            global_structure += 0.3 * np.sin(8 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Noise component with varying intensity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.4 * np.random.rand() * np.sin(15 * x[i])
        
        # Combine all components with different weights
        return 0.6 * polynomial + 1.8 * trigonometric + 1.2 * exponential + 1.5 * cross_terms + 1.0 * global_structure + 0.5 * noise