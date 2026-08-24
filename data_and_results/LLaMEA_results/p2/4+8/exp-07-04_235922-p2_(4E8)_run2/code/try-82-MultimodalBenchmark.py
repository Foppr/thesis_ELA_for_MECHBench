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
            result += np.exp(-0.25 * xi**2) * (xi**7 - 21*xi**5 + 175*xi**3 - 525*xi) * np.sin(4 * xi) + 0.35 * np.exp(-0.15 * xi**2) * (xi**6 - 15*xi**4 + 75*xi**2 - 125) * np.cos(3 * xi)
        
        # Add higher-order polynomial coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * (x[i]**3 + x[j]**3)**2 * np.sin(0.7 * (x[i] + x[j])) * np.cos(0.4 * (x[i] - x[j]))
        
        # Add multi-scale sinusoidal modulation with adaptive frequency
        for i in range(self.dim):
            xi = x[i]
            result += 0.55 * np.sin(6 * xi) * np.cos(8 * xi) * np.exp(-0.08 * xi**2) + 0.45 * np.sin(13 * xi) * np.cos(17 * xi) * np.exp(-0.06 * xi**2)
        
        # Add cross-dimensional exponential barriers
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(-0.25 * (x[i] - 2.5)**2) + np.exp(-0.25 * (x[i] + 2.5)**2) + 0.25 * np.exp(-0.1 * (x[i] - 1)**2) + 0.25 * np.exp(-0.1 * (x[i] + 1)**2)
        result += 0.95 * barrier
        
        # Add dynamic conditioning based on dimensionality and interaction
        conditioning = 1.0 + 0.25 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4) + 0.08 * np.sin(self.dim * 0.8)
        result *= conditioning
        
        # Add a complex multi-modal noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(12 * x[i]) * np.cos(10 * x[i]) * np.exp(-0.12 * x[i]**2) + 0.18 * np.sin(15 * x[i]) * np.cos(18 * x[i]) * np.exp(-0.08 * x[i]**2)
        result += 0.025 * noise
        
        # Add cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(2 * (x[i] + x[j])) * np.cos(1.5 * (x[i] - x[j]))
        result += 0.22 * coupling
        
        # Add a new complex interaction term to improve landscape quality
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * np.sin(3 * x[i]) * np.cos(5 * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        result += interaction
        
        return result