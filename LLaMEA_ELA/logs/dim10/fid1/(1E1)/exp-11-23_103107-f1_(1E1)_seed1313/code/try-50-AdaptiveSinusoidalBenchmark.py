import numpy as np

class AdaptiveSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.exp(-0.1 * x**2))
        
        # Polynomial coupling between dimensions with adaptive exponents
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                poly_coupling += (diff**2 + 0.5 * diff**4) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Adaptive penalty regions that become more severe near the global optimum
        penalty = 0
        center = np.ones(self.dim)
        dist_to_center = np.sqrt(np.sum((x - center)**2))
        
        if dist_to_center < 1.0:
            penalty += 20 * (1 - np.exp(-0.5 * dist_to_center**2)) * np.sin(5 * np.pi * dist_to_center)**2
        else:
            penalty += 5 * (dist_to_center - 1)**3 * np.cos(2 * np.pi * dist_to_center)**2
            
        # Additional multimodal component with multiple local minima
        multi_modal = 0
        for i in range(self.dim):
            multi_modal += np.sin(8 * x[i]) * np.cos(4 * x[i]) + \
                          np.sin(6 * x[i]) * np.cos(2 * x[i]) + \
                          np.sin(10 * x[i]) * np.cos(5 * x[i])
            
        # Combine all components with dynamic weights
        return 0.8 * sin_term + 0.3 * poly_coupling + penalty + 0.5 * multi_modal