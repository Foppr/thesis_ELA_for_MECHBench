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
        
        # Add higher-order polynomial coupling terms with dynamic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**2 + x[j]**2)**4 * np.sin(0.7 * (x[i] + x[j])) * np.cos(0.4 * (x[i] - x[j])) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        # Add multi-scale sinusoidal modulation with adaptive frequency and amplitude
        for i in range(self.dim):
            xi = x[i]
            result += 0.6 * np.sin(5 * xi) * np.cos(7 * xi) * np.exp(-0.05 * xi**2) + 0.5 * np.sin(11 * xi) * np.cos(13 * xi) * np.exp(-0.03 * xi**2) + 0.4 * np.sin(17 * xi) * np.cos(19 * xi) * np.exp(-0.01 * xi**2)
        
        # Add cross-dimensional exponential barriers with enhanced complexity
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(-0.3 * (x[i] - 2)**2) + np.exp(-0.3 * (x[i] + 2)**2) + 0.5 * np.exp(-0.1 * (x[i] - 3)**2) + 0.5 * np.exp(-0.1 * (x[i] + 3)**2)
        result += 1.0 * barrier
        
        # Add dynamic conditioning based on dimensionality and interaction with phase shifts
        conditioning = 1.0 + 0.3 * np.sin(self.dim * 0.7) * np.cos(self.dim * 0.4) * np.exp(-0.01 * self.dim)
        result *= conditioning
        
        # Add a complex multi-modal noise component with additional chaotic elements
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.1 * x[i]**2) + 0.2 * np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += 0.03 * noise
        
        # Add a novel chaotic coupling term between all dimensions
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling += np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2)) + np.cos(4 * x[i]) * np.sin(5 * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        result += 0.1 * chaotic_coupling
        
        return result