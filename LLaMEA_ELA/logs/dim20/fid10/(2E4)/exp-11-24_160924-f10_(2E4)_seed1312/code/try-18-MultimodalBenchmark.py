import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add nested periodic structure with varying amplitudes and frequencies
        for i in range(self.dim):
            xi = x[i]
            # Create nested oscillations with different scales
            result += (xi**2 * np.sin(5 * xi) + 0.5 * xi * np.cos(3 * xi) + 
                      0.1 * np.sin(10 * xi) * np.cos(7 * xi))**2
            
        # Add asymmetric saddle points with directional dependency
        for i in range(self.dim):
            xi = x[i]
            # Introduce asymmetric quadratic terms
            result += 0.3 * (xi - 1)**2 * (xi + 1)**2 * np.sin(2 * xi)
            
        # Add non-separable cross-terms with gradient-dependent conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Introduce coupling with varying strength based on dimension indices
                strength = (i + 1) * (j + 1) / (self.dim * (self.dim + 1))
                result += strength * np.sin(2 * (x[i]**2 + x[j]**2)) * np.cos(3 * x[i] * x[j])
                
        # Add a conditioning component that changes based on gradient magnitude
        grad_magnitude = 0.0
        for i in range(self.dim):
            xi = x[i]
            grad_magnitude += (2 * xi * np.sin(5 * xi) + 0.5 * np.cos(3 * xi) + 
                             0.1 * 10 * np.cos(10 * xi) * np.cos(7 * xi))**2
        result += 0.01 * grad_magnitude
        
        # Add global shaping term to encourage convergence towards specific regions
        result += 0.5 * np.sum(np.abs(x)**3) + 0.2 * np.sum(np.sin(0.5 * x))
        
        return result