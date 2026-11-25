import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Global quadratic basin term with modified coefficient
        quadratic_term = 0.5 * np.sum(x_normalized**2)
        
        # Sinusoidal oscillations with exponentially increasing frequencies and added quintic term
        sin_term = 0.0
        for i in range(self.dim):
            freq = 10 * (2 ** i)  # Exponentially increasing frequencies
            sin_term += np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.3)**2) + 0.2 * x_normalized[i]**5
        
        # Additional multimodal component with higher frequency interactions and chaotic noise
        multivariate_sin = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 15 * (2 ** i)
                freq_j = 12 * (2 ** j)
                multivariate_sin += np.sin(freq_i * np.pi * x_normalized[i]) * np.sin(freq_j * np.pi * x_normalized[j]) * (1 + 0.3 * (x_normalized[i]**2 + x_normalized[j]**2)) * (1 + 0.1 * np.sin(50 * x_normalized[i] * x_normalized[j]))
        
        # Refined shifted global minimum with quintic terms for increased conditioning and noise
        shift_term = 1.3 * np.sum((x_normalized - 0.5)**5)
        
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(100 * x_normalized[i]) * np.cos(70 * x_normalized[i])
        
        return quadratic_term + sin_term + multivariate_sin + shift_term + noise