import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Global quadratic basin term with modified coefficient
        quadratic_term = 0.1 * np.sum(x_normalized**2)
        
        # Sinusoidal oscillations with increased frequency and quintic interaction
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(11 * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.1)**2) + 0.08 * x_normalized[i]**5
        
        # Additional multimodal component with mixed interactions
        multivariate_sin = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multivariate_sin += np.sin(7 * np.pi * x_normalized[i]) * np.sin(4 * np.pi * x_normalized[j]) + 0.03 * x_normalized[i]**2 * x_normalized[j]**3
        
        # Add quintic interaction terms for increased complexity
        quintic_term = 0.0
        for i in range(self.dim):
            quintic_term += 0.015 * x_normalized[i]**5
        
        # Shifted global minimum to improve conditioning
        shift_term = 0.03 * np.sum((x_normalized - 0.2)**5)
        
        return quadratic_term + sin_term + multivariate_sin + quintic_term + shift_term