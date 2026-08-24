import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Higher-degree polynomial terms with cross-terms
        for i in range(self.dim):
            result += 0.8 * x[i]**6 - 3.0 * x[i]**5 + 2.5 * x[i]**4 - 1.0 * x[i]**3
            
        # Enhanced sinusoidal coupling with more dimensions and frequencies
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling
                result += 0.5 * np.sin(5 * np.pi * x[i]) * np.cos(3 * np.pi * x[j]) * np.sin(2 * np.pi * (x[i] + x[j]))
                
        # Multi-modal radial basis function with multiple centers
        centers = np.linspace(-4.0, 4.0, self.dim)
        for i in range(self.dim):
            result += 0.4 * np.exp(-0.2 * (x[i] - centers[i])**2) + 0.2 * np.exp(-0.05 * (x[i] - centers[i])**2)
            
        # High-frequency oscillation with exponential decay
        for i in range(self.dim):
            result += 0.2 * np.sin(15 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Cross-dimensional interaction with cubic terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * (x[i]**3) * (x[j]**2) * np.sin(np.pi * (x[i] + x[j]))
                
        # Add a global minimum at origin with strong penalty
        result += 0.1 * np.sum(x**2) + 0.05 * np.sum(x**4)
        
        # Add a secondary global optimum at a distant location
        distant_center = np.ones(self.dim) * 3.0
        result += 0.15 * np.sum((x - distant_center)**2)
        
        return result