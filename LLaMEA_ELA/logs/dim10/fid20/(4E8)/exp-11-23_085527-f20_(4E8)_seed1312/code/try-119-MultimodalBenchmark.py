import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial base with higher-order terms and adaptive conditioning
        polynomial = np.sum(x_scaled**4) + 0.5 * np.sum(x_scaled**6) + 0.1 * np.sum(x_scaled**8)
        
        # Chaotic trigonometric components with dynamic frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.5 + 0.5 * np.sin(i * 0.7))  # Increased chaotic frequency modulation
            amplitude = 1.0 / (1.0 + 0.5 * i**2)
            trigonometric += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Dynamic exponential decay with varying cross-terms and increased complexity
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(4 * x_scaled[i] * x_scaled[j]) * np.cos(5 * x_scaled[i] * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Non-separable interaction terms with chaotic weights and higher-order components
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 2.0 + 0.8 * np.sin(i * 0.4) * np.cos(j * 0.5)
                interaction += weight * (x_scaled[i]**3 + x_scaled[j]**3) * np.sin(4 * x_scaled[i] * x_scaled[j]) + \
                              1.2 * (x_scaled[i]**5 + x_scaled[j]**5) * np.cos(3 * x_scaled[i] * x_scaled[j])
        
        # Additional quadratic and cubic terms with increased complexity
        quadratic = 0.7 * np.sum(x_scaled**2)
        cubic = 0.2 * np.sum(x_scaled**3)
        
        # Global scaling and combination with refined coefficients
        return 5.0 * polynomial + 4.0 * trigonometric + 3.0 * exponential + 3.0 * interaction + 1.5 * quadratic + 0.4 * cubic