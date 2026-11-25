import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Enhanced sinusoidal oscillations with modified frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.8 * np.sin(4 * x[i]) * (x[i]**2) + 0.6 * np.cos(5 * x[i]) * (x[i]**3)
            
        # Radial basis function interactions with modified decay rates
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x[i] - x[j])**2 + 0.05)
                f_val += 0.4 * np.exp(-2 * distance**2) * np.sin(3 * np.pi * (x[i] + x[j]))
                
        # Multi-scale conditioning with adjusted penalty strengths
        for i in range(self.dim):
            f_val += 0.3 * (x[i]**4) * np.cos(0.7 * x[i]) + 0.15 * (x[i]**6) * np.sin(0.4 * x[i])
            
        # Cross-dimensional polynomial interactions with modified exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * (x[i] * x[j])**2.5 * np.exp(-0.15 * (x[i]**2 + x[j]**2))
                
        # Additional harmonic terms with altered frequencies
        for i in range(self.dim):
            f_val += 0.5 * np.sin(7 * x[i]) * np.cos(2.5 * x[i]) + 0.4 * np.sin(9 * x[i])
            
        # Global conditioning term with modified exponents
        f_val += 0.015 * np.sum(x**11) + 0.008 * np.sum(x**13)
        
        return f_val