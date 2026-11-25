import numpy as np

class MultimodalConditioningBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dimension-specific conditioning parameters
        self.conditioning_params = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        self.coupling_freq = np.array([0.5 + 0.3 * np.cos(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with dimension-specific conditioning
        for i in range(self.dim):
            result += self.conditioning_params[i] * np.exp(-0.1 * x[i]**2) * (1 + 0.2 * np.sin(x[i]))
            
        # Trigonometric coupling between dimensions with adaptive frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(self.coupling_freq[i] * x[i]) * np.cos(self.coupling_freq[j] * x[j])
                result += 0.3 * coupling * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Add adaptive conditioning with polynomial terms
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**3 * np.cos(0.4 * x[i]) * self.conditioning_params[i]
            result += poly_term
            
        # Create complex valleys using composite sinusoidal functions
        valley_terms = 0.0
        for i in range(self.dim):
            valley_terms += np.sin(2 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.02 * x[i]**2)
        result += 0.5 * valley_terms**2
        
        # Add cross-dimensional interaction with varying strengths
        interaction_strength = np.zeros(self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_strength[i] += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
        
        result += 0.2 * np.sum(interaction_strength**2)
        
        # Add noise to increase irregularity
        noise = 0.005 * np.sum(np.sin(x * 15) * np.cos(x * 8))
        result += noise
        
        return result