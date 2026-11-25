import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add exponential repulsion fields centered at non-uniform points
        center_offsets = np.linspace(0, 2*np.pi, self.dim)
        for i in range(self.dim):
            center_x = 2.0 * np.sin(center_offsets[i])
            center_y = 2.0 * np.cos(center_offsets[i])
            dist = np.sqrt((x[i] - center_x)**2 + (x[(i+1)%self.dim] - center_y)**2)
            f += 2.0 * np.exp(-dist**2 / 2.0) * np.sin(3 * dist)
        
        # Add trigonometric modulation with varying frequencies
        for i in range(self.dim):
            f += 0.5 * np.sin(7 * x[i]) * np.cos(4 * x[(i+1)%self.dim]) * np.sin(2 * x[(i+2)%self.dim])
            
        # Add cubic gradient terms with chaotic phase shifts
        for i in range(self.dim):
            f += 0.3 * x[i]**3 * np.sin(5 * x[(i+1)%self.dim] + np.pi/4) + 0.2 * x[i]**2 * np.cos(3 * x[(i+2)%self.dim])
            
        # Add chaotic harmonic interactions across all dimensions
        for i in range(self.dim):
            f += 0.15 * np.sin(9 * x[i]) * np.cos(6 * x[(i+1)%self.dim]) * np.sin(4 * x[(i+3)%self.dim]) * np.cos(2 * x[(i+4)%self.dim])
            
        # Add irregular penalty terms with exponential scaling
        f += 0.2 * np.sum(np.exp(0.5 * np.abs(x)) - 1) + 0.1 * np.sum(x**6)
        
        # Add multi-scale sinusoidal interference patterns
        for i in range(self.dim):
            f += 0.4 * np.sin(11 * x[i]) * np.cos(8 * x[(i+2)%self.dim]) * np.sin(5 * x[(i+3)%self.dim])
            
        return f