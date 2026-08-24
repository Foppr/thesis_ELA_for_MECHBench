import numpy as np

class RuggedCorrelationValley:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base quadratic with sinusoidal modulation
        f = 0.5 * np.sum(x**2) + 0.3 * np.sum(np.sin(3 * x_norm))
        
        # Add ruggedness through high-frequency oscillations
        for i in range(self.dim):
            f += 0.2 * np.sin(10 * x[i]) * np.cos(15 * x[i]) + 0.1 * np.sin(20 * x[i])
            
        # Non-separable correlation structure
        correlation = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling based on dimension indices
                coupling_strength = 0.1 * np.sin(i * 0.3) * np.cos(j * 0.4) + 0.05 * np.sin(i + j * 0.2)
                correlation += coupling_strength * (x[i] - x[j])**2
                
        f += correlation
        
        # Multi-modal structure with irregular peaks
        modal = 0.0
        for i in range(self.dim):
            # Multiple peaks with varying heights and positions
            peak1 = 0.5 * np.sin(4 * x[i]) * np.cos(6 * x[i])
            peak2 = 0.3 * np.sin(8 * x[i]) * np.cos(10 * x[i])
            peak3 = 0.2 * np.sin(12 * x[i]) * np.cos(14 * x[i])
            modal += peak1 + peak2 + peak3
            
        f += modal
        
        # Add chaotic-like perturbations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.1 * np.sin(25 * x[i]) * np.cos(30 * x[i]) * np.sin(35 * x[i])
        f += chaotic
        
        # Introduce varying curvature and saddle points
        curvature = 0.0
        for i in range(self.dim):
            # Varying curvature based on position
            curvature += 0.1 * (x[i]**2) * np.sin(x[i]) + 0.05 * (x[i]**3) * np.cos(x[i])
        f += curvature
        
        # Add exponential decay terms for additional complexity
        decay = 0.0
        for i in range(self.dim):
            decay += 0.15 * np.exp(-0.1 * x[i]**2) * np.sin(5 * x[i])
        f += decay
        
        # Final adjustment for better conditioning and scaling
        f = f * (1.0 + 0.05 * np.sum(np.abs(x)) + 0.02 * np.sum(x**4))
        
        return f