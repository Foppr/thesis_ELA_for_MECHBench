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
        
        # Base quadratic + exponential decay terms
        for i in range(self.dim):
            result += 0.5 * x[i]**2 + 0.1 * np.exp(-0.1 * x[i]**2)
            
        # Add chaotic gradient components with varying frequencies
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(0.3 * i)
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.1 * (x[i]**2 + x[j]**2))
                result += 0.2 * coupling * np.sin(1.5 * x[i] + 0.8 * x[j])
                
        # Add saddle point structure with hyperbolic tangent interactions
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.tanh(x[i])**2
            
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                saddle_term += 0.1 * np.tanh(x[i]) * np.tanh(x[j])
                
        result += 0.5 * saddle_term
        
        # Add non-linear frequency modulation
        mod_freq = 1.0 + 0.3 * np.sin(0.5 * np.sum(x))
        result *= mod_freq
        
        return result