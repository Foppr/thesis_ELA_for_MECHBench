import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Main quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic sinusoidal interactions with varying amplitudes and frequencies
        for i in range(self.dim):
            f_val += 0.2 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
            
        # Add exponentially weighted local optima to increase complexity
        for i in range(self.dim):
            f_val += 0.1 * np.exp(-0.5 * x[i]**2) * np.sin(5 * x[i])**2
            
        # Add higher-order polynomial interactions with cross-terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * (x[i]**3) * (x[j]**2) * np.sin(x[i] + x[j])
                
        # Add shifted and scaled sinusoidal components for scattered local minima
        for i in range(self.dim):
            f_val += 0.12 * np.sin(8 * (x[i] - 2.0)) * np.cos(6 * (x[i] + 2.0)) * np.exp(-0.1 * (x[i] - 2.0)**2)
            
        # Add a chaotic component using a logistic-like map for enhanced nonlinearity
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.sin(9 * x[i])
        f_val += 0.08 * chaotic_term
        
        return f_val