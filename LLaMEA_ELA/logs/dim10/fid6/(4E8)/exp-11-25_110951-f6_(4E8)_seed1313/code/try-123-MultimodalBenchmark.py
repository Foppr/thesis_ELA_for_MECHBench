import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay basin with multiple local minima
        basin_term = np.sum(np.exp(-0.5 * x_norm**2) * (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Trigonometric coupling between dimensions with varying frequencies
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(3 * (x_norm[i] + x_norm[j])) * np.cos(2 * (x_norm[i] - x_norm[j]))
        
        # Stochastic perturbation with chaotic-like behavior
        stochastic_perturbation = 0.0
        for i in range(self.dim):
            stochastic_perturbation += np.sin(13 * x_norm[i]) * np.cos(7 * x_norm[i]) * \
                                     np.exp(-0.1 * np.abs(x_norm[i])) * np.random.uniform(0.8, 1.2)
        
        # Multi-scale oscillatory component with varying amplitudes
        oscillatory_term = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * 
                                 np.sin(10 * x_norm) * np.cos(5 * x_norm))
        
        # Fractal-like structure with self-similar patterns at different scales
        fractal_term = 0.0
        for scale in [0.5, 1.0, 2.0]:
            fractal_term += scale * np.sin(scale * x_norm) * np.cos(scale * x_norm)
        
        # Cross-dimensional interaction with polynomial scaling
        interaction_term = np.sum(x_norm**3 * np.sin(4 * x_norm)) / self.dim
        
        # Combined function with adaptive weights and noise injection
        return 0.5 * basin_term + 0.3 * coupling_term + 0.2 * stochastic_perturbation + \
               0.15 * oscillatory_term + 0.1 * fractal_term + 0.05 * interaction_term