import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base with mixed powers and adaptive conditioning
        polynomial = np.sum(x_scaled**3) + 0.3 * np.sum(x_scaled**5)
        
        # Chaotic trigonometric components with dynamic frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.3 * np.sin(i * 0.4))  # Slight chaotic frequency modulation
            amplitude = 1.0 / (1.0 + 0.4 * i**1.3)
            trigonometric += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Dynamic exponential decay with varying cross-terms (modified coefficients)
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))  # Increased decay rate
                cross_term = np.sin(4 * x_scaled[i] * x_scaled[j]) * np.cos(3 * x_scaled[i] * x_scaled[j])  # Changed frequencies
                exponential += exp_term * cross_term
        
        # Non-separable interaction terms with chaotic weights and higher-order components (modified weights)
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.2 + 0.6 * np.sin(i * 0.4) * np.cos(j * 0.3)  # Changed weight pattern
                interaction += weight * (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(4 * x_scaled[i] * x_scaled[j]) + \
                              0.9 * (x_scaled[i]**4 + x_scaled[j]**4) * np.cos(3 * x_scaled[i] * x_scaled[j])
        
        # Additional quadratic and cubic terms with increased complexity
        quadratic = 0.6 * np.sum(x_scaled**2)
        cubic = 0.15 * np.sum(x_scaled**3)
        
        # Global scaling and combination with refined coefficients
        return 3.8 * polynomial + 3.2 * trigonometric + 2.1 * exponential + 2.4 * interaction + 1.3 * quadratic + 0.35 * cubic