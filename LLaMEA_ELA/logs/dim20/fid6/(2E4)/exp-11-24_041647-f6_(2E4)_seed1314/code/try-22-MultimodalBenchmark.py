import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Global quadratic basin term with modified coefficient
        quadratic_term = 0.2 * np.sum(x_normalized**2)
        
        # Sinusoidal oscillations with exponentially increasing frequency and cubic interaction
        sin_term = 0.0
        for i in range(self.dim):
            freq = 10 ** (i % 3 + 1)  # Exponentially increasing frequencies
            sin_term += np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.1)**2) + 0.1 * x_normalized[i]**3
        
        # Additional multimodal component with mixed interactions and quartic cross-terms
        multivariate_sin = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multivariate_sin += np.sin(5 * np.pi * x_normalized[i]) * np.sin(3 * np.pi * x_normalized[j]) + 0.05 * x_normalized[i]**2 * x_normalized[j] + 0.01 * x_normalized[i]**4 * x_normalized[j]**2
        
        # Add higher-order quartic interaction terms for increased complexity
        quartic_term = 0.0
        for i in range(self.dim):
            quartic_term += 0.05 * x_normalized[i]**4 + 0.02 * x_normalized[i]**6
        
        # Shifted global minimum with exponential scaling to improve conditioning
        shift_term = 0.1 * np.sum((x_normalized - 0.3)**6)
        
        return quadratic_term + sin_term + multivariate_sin + quartic_term + shift_term