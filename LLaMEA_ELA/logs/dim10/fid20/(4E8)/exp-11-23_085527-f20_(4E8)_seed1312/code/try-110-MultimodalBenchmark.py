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
            freq = (i + 1) * np.pi * (1.0 + 0.2 * np.sin(i * 0.5))  # Slight chaotic frequency modulation
            amplitude = 1.0 / (1.0 + 0.3 * i**1.5)
            trigonometric += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Dynamic exponential decay with varying cross-terms
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.2 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(3 * x_scaled[i] * x_scaled[j]) * np.cos(4 * x_scaled[i] * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Non-separable interaction terms with chaotic weights and higher-order components
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.5 + 0.5 * np.sin(i * 0.3) * np.cos(j * 0.4)
                interaction += weight * (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(3 * x_scaled[i] * x_scaled[j]) + \
                              0.8 * (x_scaled[i]**4 + x_scaled[j]**4) * np.cos(2 * x_scaled[i] * x_scaled[j])
        
        # Additional quadratic and cubic terms with increased complexity
        quadratic = 0.5 * np.sum(x_scaled**2)
        cubic = 0.1 * np.sum(x_scaled**3)
        
        # Global scaling and combination with refined coefficients
        return 4.0 * polynomial + 3.0 * trigonometric + 2.0 * exponential + 2.2 * interaction + 1.2 * quadratic + 0.3 * cubic