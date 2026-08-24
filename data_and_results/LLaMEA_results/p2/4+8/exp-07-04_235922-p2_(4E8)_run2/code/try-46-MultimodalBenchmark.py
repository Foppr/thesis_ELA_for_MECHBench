import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic exponential terms with polynomial chaos
        for i in range(self.dim):
            xi = x[i]
            result += np.exp(-0.5 * xi**2) * (xi**6 - 15*xi**4 + 75*xi**2 - 125) * np.sin(3 * xi) + 0.3 * np.exp(-0.1 * xi**2) * (xi**5 - 10*xi**3 + 25*xi) * np.cos(2 * xi)
        
        # Add higher-order polynomial coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * (x[i]**2 + x[j]**2)**3 * np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
        
        # Add multi-scale sinusoidal modulation with adaptive frequency
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * np.sin(5 * xi) * np.cos(7 * xi) * np.exp(-0.05 * xi**2) + 0.4 * np.sin(11 * xi) * np.cos(13 * xi) * np.exp(-0.03 * xi**2)
        
        # Add cross-dimensional exponential barriers
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(-0.2 * (x[i] - 2)**2) + np.exp(-0.2 * (x[i] + 2)**2)
        result += 0.8 * barrier
        
        # Add dynamic conditioning based on dimensionality and interaction
        conditioning = 1.0 + 0.2 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.3)
        result *= conditioning
        
        # Add a complex multi-modal noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.1 * x[i]**2)
        result += 0.02 * noise
        
        return result