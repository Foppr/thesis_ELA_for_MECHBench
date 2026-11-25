import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Global quadratic basin term with modified coefficient
        quadratic_term = 0.1 * np.sum(x_normalized**2)
        
        # Sinusoidal oscillations with exponentially increasing frequency and quintic interaction
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2 ** (i + 1) * np.pi
            sin_term += np.sin(freq * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.1)**2) + 0.05 * x_normalized[i]**5
        
        # Additional multimodal component with mixed interactions and chaotic noise
        multivariate_sin = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multivariate_sin += np.sin(7 * np.pi * x_normalized[i]) * np.sin(4 * np.pi * x_normalized[j]) + 0.03 * x_normalized[i]**2 * x_normalized[j]**3
        
        # Add quintic interaction terms for increased complexity
        quintic_term = 0.0
        for i in range(self.dim):
            quintic_term += 0.01 * x_normalized[i]**5
        
        # Multiple global minimum shifts with different offsets
        shift_term = 0.0
        shifts = [0.2, 0.4, 0.6, 0.8]
        for k, shift in enumerate(shifts[:self.dim]):
            shift_term += 0.03 * np.sum((x_normalized - shift)**5)
        
        # Add chaotic noise component to increase conditioning difficulty
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(13 * x_normalized[i]) * np.cos(17 * x_normalized[i])
        
        return quadratic_term + sin_term + multivariate_sin + quintic_term + shift_term + noise