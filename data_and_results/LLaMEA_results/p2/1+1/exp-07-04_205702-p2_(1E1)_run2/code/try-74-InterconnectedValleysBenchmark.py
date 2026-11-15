import numpy as np

class InterconnectedValleysBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with varying weights
        weights = 1.0 + 0.5 * np.sin(np.arange(self.dim) * 0.5)
        f1 = 0.5 * np.sum(weights * x**2)
        
        # Asymmetric plateaus with varying heights
        f2 = 0.0
        for i in range(self.dim):
            plateau_height = 2.0 + 1.5 * np.cos(0.3 * i)
            plateau_width = 0.5 + 0.3 * np.sin(0.4 * i)
            f2 += plateau_height * np.exp(-0.5 * ((x[i] - 1.0) / plateau_width)**2)
        
        # Interconnected ridges with varying frequencies
        f3 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.6 * i)
            f3 += 1.5 * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Dynamic saddle points with time-varying parameters
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                saddle_strength = 0.8 + 0.4 * np.sin(0.5 * (i + j))
                f4 += saddle_strength * x[i] * x[j] * np.sin(0.3 * (x[i] + x[j]))
        
        # Varying curvature and asymmetric basin structures
        f5 = 0.0
        for i in range(self.dim):
            curvature = 1.0 + 0.3 * np.cos(0.7 * i)
            basin_depth = 1.0 + 0.5 * np.sin(0.4 * i)
            f5 += curvature * (x[i] - 2.0)**2 * np.exp(-0.5 * basin_depth * x[i]**2)
        
        # Cross-dimensional interactions with varying coupling strengths
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.3 * np.cos(0.2 * (i + j))
                f6 += coupling * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add noise term for robustness
        noise = 0.02 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise