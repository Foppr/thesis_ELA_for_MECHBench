import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic component with varying exponents and sinusoidal modulation
        for i in range(self.dim):
            # Use chaotic logistic map-like behavior with sinusoidal modulation
            chaotic_term = np.sin(x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            # Add varying polynomial terms with chaotic coefficients
            result += 0.5 * x[i]**2 + 0.1 * x[i]**4 + 0.02 * x[i]**6 + chaotic_term
            
        # Cross-dimensional coupling with exponential decay and chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponential decay interaction with chaotic modulation
                coupling = np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(3.0 * (x[i] + x[j]))
                result += 0.3 * coupling * (1.0 + 0.1 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[j]))
                
        # Add a non-uniform scaling factor based on dimension
        scaling = 1.0
        for i in range(self.dim):
            scaling += 0.2 * np.sin(0.5 * i) * np.cos(0.3 * x[i]) + 0.05 * np.sin(2.0 * x[i])**2
            
        result = result * scaling
        
        # Add a global chaotic perturbation to increase complexity
        global_perturbation = 0.0
        for i in range(self.dim):
            global_perturbation += 0.1 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) + 0.05 * np.sin(15.0 * x[i])
            
        result = result + global_perturbation
        
        return result