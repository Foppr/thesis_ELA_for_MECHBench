import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Logarithmic barrier terms to create narrow valleys and steep walls
        for i in range(self.dim):
            result += 10.0 * np.log(1.0 + np.exp(2.0 * (abs(x[i]) - 4.5)))
            
        # Complex harmonic interactions with varying phases and amplitudes
        for i in range(self.dim):
            phase = 0.1 * i * np.pi
            amp = 2.0 + np.sin(i * 0.3)
            result += amp * np.sin(3 * x[i] + phase) * np.cos(2 * x[i] - phase) * np.exp(-0.1 * x[i]**2)
            
        # Asymmetric saddle points with varying curvature
        for i in range(self.dim):
            result += 0.5 * (x[i]**2 - 4.0)**2 * np.sin(0.5 * x[i])**2
            
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
                result += 0.3 * coupling
                
        # Multi-peak structure with varying heights and widths
        for i in range(self.dim):
            result += 0.8 * np.exp(-0.5 * ((x[i] - 2.0) / 0.5)**2) + \
                      0.6 * np.exp(-0.5 * ((x[i] + 2.0) / 0.4)**2) + \
                      0.4 * np.exp(-0.5 * ((x[i]) / 0.3)**2)
            
        # Final chaotic modulation using a logistic map-like function
        chaos_factor = 1.0
        for i in range(self.dim):
            chaos_factor *= (4.0 * abs(x[i] % 1.0) * (1 - abs(x[i] % 1.0)))
        result += 0.2 * chaos_factor
        
        return result