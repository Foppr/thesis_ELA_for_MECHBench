import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Add multiple quadratic terms with different scales and offsets
        for i in range(self.dim):
            # Main quadratic term with varying coefficients
            result += (x[i] - 1.0)**2 * (1.0 + 0.5 * np.sin(i))
            
            # Additional terms to create multimodality with cross-dimensional coupling
            if i < self.dim - 1:
                result += 0.3 * (x[i]**2 + x[i+1]**2) * np.cos(2 * x[i] * x[i+1])
            
            # Add sinusoidal perturbations with exponentially increasing frequencies
            for k in range(1, 6):
                result += 0.2 * np.sin(k**2 * x[i]) * np.cos(k * x[i])
            
            # Add a complex polynomial term to increase landscape complexity
            result += 0.1 * x[i]**6 * np.sin(x[i]**2)
            
            # Add a highly oscillatory component for extreme multimodality
            result += 0.05 * np.sin(100 * x[i]) * np.cos(50 * x[i])
        
        # Add a high-dimensional coupling term to increase conditioning difficulty
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.01 * np.sin(10 * x[i]) * np.cos(10 * x[j])
        result += coupling_term
        
        # Add a small noise term to make it non-convex
        result += 0.005 * np.sum(x**8)
        
        return result