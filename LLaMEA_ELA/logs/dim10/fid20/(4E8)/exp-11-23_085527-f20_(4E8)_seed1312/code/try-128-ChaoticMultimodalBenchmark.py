import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base with mixed powers and adaptive conditioning
        polynomial = np.sum(x_scaled**4) + 0.2 * np.sum(x_scaled**6)
        
        # Chaotic trigonometric components with dynamic frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.5 * np.sin(i * 0.3))  # Chaotic frequency modulation
            amplitude = 1.0 / (1.0 + 0.3 * i**1.2)
            trigonometric += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Dynamic exponential decay with varying cross-terms (modified coefficients)
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.4 * (x_scaled[i]**2 + x_scaled[j]**2))  # Increased decay rate
                cross_term = np.sin(3 * x_scaled[i] * x_scaled[j]) * np.cos(2 * x_scaled[i] * x_scaled[j])  # Changed frequencies
                exponential += exp_term * cross_term
        
        # Non-separable interaction terms with chaotic weights and higher-order components (modified weights)
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.5 + 0.5 * np.sin(i * 0.5) * np.cos(j * 0.4)  # Changed weight pattern
                interaction += weight * (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(3 * x_scaled[i] * x_scaled[j]) + \
                              0.8 * (x_scaled[i]**3 + x_scaled[j]**3) * np.cos(2 * x_scaled[i] * x_scaled[j])
        
        # Additional quadratic and quartic terms with increased complexity
        quadratic = 0.5 * np.sum(x_scaled**2)
        quartic = 0.1 * np.sum(x_scaled**4)
        
        # Global scaling and combination with refined coefficients
        return 4.0 * polynomial + 3.0 * trigonometric + 2.5 * exponential + 2.2 * interaction + 1.5 * quadratic + 0.25 * quartic