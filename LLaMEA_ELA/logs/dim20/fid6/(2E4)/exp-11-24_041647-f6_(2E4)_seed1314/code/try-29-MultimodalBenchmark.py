import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Global quadratic basin term with modified coefficient
        quadratic_term = 0.3 * np.sum(x_normalized**2)
        
        # Sinusoidal oscillations with increased frequency and added quartic term
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(20 * np.pi * x_normalized[i]) * np.exp(-0.2 * (x_normalized[i] - 0.2)**2) + 0.15 * x_normalized[i]**4
        
        # Additional multimodal component with higher frequency interactions
        multivariate_sin = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multivariate_sin += np.sin(12 * np.pi * x_normalized[i]) * np.sin(8 * np.pi * x_normalized[j]) * (1 + 0.4 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        # Refined shifted global minimum with quintic terms for increased conditioning
        shift_term = 0.9 * np.sum((x_normalized - 0.25)**5)
        
        return quadratic_term + sin_term + multivariate_sin + shift_term