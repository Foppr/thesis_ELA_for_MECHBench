import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add enhanced chaotic exponential terms with modified polynomial chaos
        for i in range(self.dim):
            xi = x[i]
            result += np.exp(-0.3 * xi**2) * (xi**7 - 21*xi**5 + 175*xi**3 - 525*xi) * np.sin(2.5 * xi) + 0.4 * np.exp(-0.15 * xi**2) * (xi**4 - 8*xi**2 + 16) * np.cos(1.5 * xi)
        
        # Add higher-order polynomial coupling terms with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.3 * np.sin(0.2 * (i + j)) * np.cos(0.1 * (i - j))
                result += weight * (x[i]**3 + x[j]**3)**2 * np.sin(0.4 * (x[i] + x[j])) * np.cos(0.2 * (x[i] - x[j]))
        
        # Add refined multi-scale sinusoidal modulation with adaptive frequency
        for i in range(self.dim):
            xi = x[i]
            result += 0.6 * np.sin(6 * xi) * np.cos(8 * xi) * np.exp(-0.04 * xi**2) + 0.3 * np.sin(12 * xi) * np.cos(15 * xi) * np.exp(-0.02 * xi**2)
        
        # Add enhanced cross-dimensional exponential barriers
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(-0.25 * (x[i] - 2.5)**2) + np.exp(-0.25 * (x[i] + 2.5)**2) + 0.5 * np.exp(-0.1 * x[i]**2)
        result += 1.0 * barrier
        
        # Add dynamic conditioning based on dimensionality and interaction
        conditioning = 1.0 + 0.15 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4)
        result *= conditioning
        
        # Add refined complex multi-modal noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(9 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.12 * x[i]**2) + 0.2 * np.sin(14 * x[i]) * np.cos(16 * x[i]) * np.exp(-0.08 * x[i]**2)
        result += 0.015 * noise
        
        return result