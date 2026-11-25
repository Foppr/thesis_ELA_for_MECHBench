import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive conditioning parameters
        self.conditioning = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        self.frequency_mod = np.array([1.0 + 0.3 * np.cos(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with dimension-specific conditioning
        for i in range(self.dim):
            exp_term = self.conditioning[i] * np.exp(-0.1 * np.abs(x[i])) * np.cos(2 * np.pi * x[i])
            result += exp_term
            
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                coupling = np.sin(self.frequency_mod[i] * x[i]) * np.cos(self.frequency_mod[j] * x[j])
                coupling *= np.exp(-0.05 * (x[i] - x[j])**2)
                result += 0.1 * coupling
                
        # Adaptive polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            poly_term = 0.02 * x[i]**4 * np.sin(3 * x[i]) * self.frequency_mod[i]
            result += poly_term
            
        # Add global multimodal component with varying amplitude
        global_multimodal = 0.0
        for i in range(self.dim):
            global_multimodal += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
        result += 0.5 * global_multimodal**2
        
        # Add noise with adaptive strength based on dimension
        noise = 0.005 * np.sum(np.sin(x * 15) * self.conditioning)
        result += noise
        
        return result