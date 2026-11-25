import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Global quadratic basin term with modified coefficient
        quadratic_term = 0.2 * np.sum(x_normalized**2)
        
        # Sinusoidal oscillations with higher frequency and additional cubic term
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(7 * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.1)**2) + 0.1 * x_normalized[i]**3
        
        # Additional multimodal component with cross-terms
        multivariate_sin = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multivariate_sin += np.sin(4 * np.pi * x_normalized[i]) * np.sin(2 * np.pi * x_normalized[j]) * (1 + 0.1 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        # Shifted global minimum to create more challenging landscape
        shift_term = 0.5 * np.sum((x_normalized - 0.3)**4)
        
        return quadratic_term + sin_term + multivariate_sin + shift_term