import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive conditioning parameters
        self.conditioning = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        # Precompute coupling strengths
        self.coupling_strengths = np.array([0.3 + 0.2 * np.cos(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with adaptive conditioning
        for i in range(self.dim):
            exp_term = self.conditioning[i] * np.exp(-0.1 * x[i]**2) * np.cos(0.5 * x[i])
            result += exp_term
            
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                trig_coupling = coupling * np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i] + x[j]))
                result += trig_coupling
                
        # Add multi-modal harmonic terms
        for i in range(self.dim):
            harmonic = 0.2 * np.sin(3 * x[i]) * np.cos(2 * x[i])
            result += harmonic
            
        # Add saddle-point like structure with polynomial interaction
        poly_interaction = 0.05 * np.sum(x**4) - 0.1 * np.sum(x**2)
        result += poly_interaction
        
        # Add adaptive noise based on dimension
        noise = 0.02 * np.sum(np.sin(x * (1 + 0.1 * np.arange(self.dim))))
        result += noise
        
        return result