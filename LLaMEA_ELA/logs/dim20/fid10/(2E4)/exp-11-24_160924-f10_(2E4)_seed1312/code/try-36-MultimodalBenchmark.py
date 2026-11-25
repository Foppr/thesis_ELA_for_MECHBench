import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add polynomial and sinusoidal components with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            # Combine polynomial and sinusoidal terms to create complex landscape
            result += (xi**6 - 10 * xi**4 + 35 * xi**2 - 30) * np.sin(0.7 * xi) + 0.3 * xi**5 * np.cos(1.3 * xi)
            
        # Add cross-dimensional coupling with non-separable interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling for increased complexity
                # Introduce highly non-linear dependencies between dimensions
                result += 0.5 * np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(3 * (x[i] + x[j]))
                
        # Add a global scaling term to increase conditioning difficulty
        result += 0.02 * np.sum(x**8) + 0.03 * np.sum(np.cos(5 * x)) + 0.01 * np.sum(np.sin(2 * x))
        
        # Add a highly non-separable interaction term involving all dimensions
        result += 0.4 * np.exp(-0.1 * np.sum((x - np.mean(x))**2)) * np.cos(0.5 * np.sum(x**3))
        
        # Add novel high-order polynomial and trigonometric coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * (x[i]**3 + x[j]**3) * np.sin(2.5 * (x[i] - x[j])) * np.cos(1.7 * (x[i] + x[j]))
                
        # Add a complex multi-modal component with multiple interacting peaks
        result += 0.6 * np.sum(np.sin(4 * x) * np.cos(3 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Add a term that heavily penalizes deviation from the global optimum at origin
        result += 0.1 * np.sum((x - 0.1 * np.sin(x))**4)
        
        return result