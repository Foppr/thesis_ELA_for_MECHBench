import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Enhanced sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 1.5 * np.sin(5 * x[i]) * np.cos(2 * x[i]) + 0.8 * np.sin(7 * x[i])
            
        # Improved radial basis function interactions with multi-scale decay and correlation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x[i] - x[j])**2 + 0.05)
                f_val += 0.4 * np.exp(-2.0 * distance**2) * np.sin(3 * np.pi * (x[i] + x[j])) * np.cos(0.5 * (x[i] - x[j]))
                
        # Modified polynomial penalties with stronger conditioning
        for i in range(self.dim):
            f_val += 0.3 * (x[i]**4) * np.cos(0.7 * x[i]) + 0.2 * (x[i]**5) * np.sin(0.4 * x[i])
            
        # Enhanced cross-dimensional polynomial interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.15 * (x[i] * x[j])**3 * np.exp(-0.3 * (x[i]**2 + x[j]**2)) * np.sin(2 * x[i] * x[j])
                
        # Additional harmonic terms with higher frequency components and phase shifts
        for i in range(self.dim):
            f_val += 0.5 * np.sin(9 * x[i]) * np.cos(3 * x[i]) + 0.4 * np.sin(11 * x[i]) + 0.3 * np.cos(5 * x[i])
            
        # Global conditioning with stronger polynomial terms and improved scaling
        f_val += 0.025 * np.sum(x**8) + 0.02 * np.sum(x**10)
        
        # Add a small noise term to break symmetries and increase challenge
        f_val += 0.001 * np.sum(np.sin(100 * x))
        
        return f_val