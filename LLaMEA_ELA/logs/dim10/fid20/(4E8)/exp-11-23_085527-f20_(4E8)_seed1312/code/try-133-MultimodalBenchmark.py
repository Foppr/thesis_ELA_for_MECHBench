import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial base with mixed powers and adaptive conditioning
        polynomial = np.sum(x_scaled**3) + 0.4 * np.sum(x_scaled**5) + 0.2 * np.sum(x_scaled**7)
        
        # Chaotic trigonometric components with dynamic frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.2 + 0.5 * np.sin(i * 0.5))  # Increased chaotic frequency modulation
            amplitude = 1.0 / (1.0 + 0.6 * i**1.5)
            trigonometric += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Dynamic exponential decay with varying cross-terms (enhanced coefficients)
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.4 * (x_scaled[i]**2 + x_scaled[j]**2))  # Increased decay rate
                cross_term = np.sin(5 * x_scaled[i] * x_scaled[j]) * np.cos(4 * x_scaled[i] * x_scaled[j])  # Changed frequencies
                exponential += exp_term * cross_term
        
        # Non-separable interaction terms with enhanced chaotic weights and higher-order components
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.5 + 0.8 * np.sin(i * 0.5) * np.cos(j * 0.4)  # Enhanced weight pattern
                interaction += weight * (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(5 * x_scaled[i] * x_scaled[j]) + \
                              1.2 * (x_scaled[i]**4 + x_scaled[j]**4) * np.cos(4 * x_scaled[i] * x_scaled[j])
        
        # Additional quadratic and cubic terms with increased complexity
        quadratic = 0.8 * np.sum(x_scaled**2)
        cubic = 0.2 * np.sum(x_scaled**3)
        
        # Global scaling and combination with refined coefficients
        return 4.2 * polynomial + 3.6 * trigonometric + 2.5 * exponential + 2.8 * interaction + 1.5 * quadratic + 0.4 * cubic