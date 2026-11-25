import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Global quadratic basin term
        quadratic_term = 0.1 * np.sum(x_normalized**2)
        
        # Sinusoidal oscillations with multiple local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5 * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.2)**2)
        
        # Additional multimodal component
        multivariate_sin = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multivariate_sin += np.sin(3 * np.pi * x_normalized[i]) * np.sin(3 * np.pi * x_normalized[j])
        
        return quadratic_term + sin_term + multivariate_sin