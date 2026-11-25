import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial base with mixed powers and adaptive conditioning
        polynomial = np.sum(x_scaled**4) + 0.2 * np.sum(x_scaled**6)
        
        # Improved trigonometric components with dynamic frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.2 * np.sin(i * 0.5))
            amplitude = 1.0 / (1.0 + 0.4 * i)
            trigonometric += amplitude * np.cos(freq * x_scaled[i]) * np.sin(freq * x_scaled[i])
        
        # Strengthened exponential decay with more complex cross-terms
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(5 * x_scaled[i] * x_scaled[j]) * np.cos(2 * x_scaled[i] * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Enhanced non-separable interaction terms with modified weights and higher-order components
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_scaled[i]**3 + x_scaled[j]**3) * np.sin(4 * x_scaled[i] * x_scaled[j]) + \
                              0.5 * (x_scaled[i]**2 + x_scaled[j]**2) * np.cos(2 * x_scaled[i] * x_scaled[j])
        
        # Additional quadratic and cubic terms with increased complexity
        quadratic = 0.7 * np.sum(x_scaled**2)
        cubic = 0.2 * np.sum(x_scaled**3)
        
        # Global scaling and combination with refined coefficients
        return 5.0 * polynomial + 3.0 * trigonometric + 2.5 * exponential + 1.8 * interaction + 1.0 * quadratic + 0.4 * cubic