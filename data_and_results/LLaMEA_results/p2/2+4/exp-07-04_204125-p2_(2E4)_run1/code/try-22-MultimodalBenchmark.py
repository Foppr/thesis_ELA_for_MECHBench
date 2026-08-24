import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base with alternating coefficients
        for i in range(self.dim):
            result += 0.1 * x[i]**6 + 0.3 * x[i]**4 - 0.5 * x[i]**2
        
        # Trigonometric modulation with frequency scaling
        for i in range(self.dim):
            result += 0.2 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function component with varying centers
        for i in range(self.dim):
            center = 2.0 * np.sin(i * np.pi / self.dim)
            result += 0.15 * np.exp(-0.5 * (x[i] - center)**2) * np.cos(4.0 * (x[i] - center))
        
        # Asymmetric saddle points with directional coupling
        for i in range(self.dim):
            if i < self.dim - 1:
                # Directional coupling with asymmetry
                coupling = (x[i] - x[i+1])**2 * np.exp(-0.05 * (x[i]**2 + x[i+1]**2))
                result += 0.25 * coupling * np.sin(2.0 * (x[i] + x[i+1]))
        
        # Variable coupling strength based on dimension index
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.1 * (1.0 + 0.5 * np.sin(0.5 * (i + j)))
                result += strength * np.sin(0.5 * (x[i]**2 + x[j]**2)) * np.cos(0.3 * (x[i] - x[j]))
        
        # Add noise-like perturbations with non-uniform distribution
        for i in range(self.dim):
            result += 0.02 * np.sin(10.0 * x[i]) * np.exp(-0.01 * np.abs(x[i]))
        
        # Global scaling and offset
        result = result * (1.0 + 0.1 * np.sum(np.abs(x)))
        
        return result