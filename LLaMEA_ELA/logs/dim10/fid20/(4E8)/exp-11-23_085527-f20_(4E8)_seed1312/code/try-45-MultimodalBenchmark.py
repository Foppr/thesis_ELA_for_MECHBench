import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base term with mixed powers and adaptive conditioning
        polynomial = np.sum((x_scaled**4) * (1.0 + 0.3 * np.abs(x_scaled))) + 0.7 * np.sum(x_scaled**8)
        
        # Enhanced trigonometric components with dynamic frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.2 * np.sin(i))
            amplitude = 1.5 / (1.0 + 0.2 * i**1.5)
            trigonometric += amplitude * np.cos(freq * x_scaled[i]) * np.sin(freq * x_scaled[i])
        
        # Exponential decay components with stronger cross-terms and non-separable interactions
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(5 * x_scaled[i] * x_scaled[j]) * np.cos(2 * x_scaled[i] + 3 * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Complex interaction terms with higher-order non-separability
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_scaled[i]**2 + x_scaled[j]**2)**2 * np.sin(3 * x_scaled[i] * x_scaled[j])
        
        # Additional high-frequency oscillatory component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(10 * x_scaled[i]) * np.cos(7 * x_scaled[i])
        
        # Global scaling and combination with increased complexity
        return 7.0 * polynomial + 4.0 * trigonometric + 3.0 * exponential + 2.0 * interaction + 1.0 * high_freq