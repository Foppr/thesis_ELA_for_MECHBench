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
            result += (xi**6 - 15 * xi**4 + 75 * xi**2 - 125) * np.sin(0.35 * xi) + 0.75 * xi**4 * np.cos(0.75 * xi)
            
        # Add cross-dimensional coupling with non-separable interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range
                # Introduce highly non-linear dependencies between dimensions
                result += 0.9 * np.exp(-0.35 * (x[i] - x[j])**2) * np.sin(4.5 * (x[i] + x[j]))
                
        # Add a global scaling term to increase conditioning difficulty
        result += 0.04 * np.sum(x**9) + 0.05 * np.sum(np.cos(5.0 * x)) + 0.025 * np.sum(np.sin(2.5 * x))
        
        # Add a complex interaction term that creates multiple local minima
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * np.sin(6.5 * (x[i]**2 + x[j]**2)) * np.exp(-0.2 * (x[i] - x[j])**2)
                
        # Add higher-order coupling terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, min(j+4, self.dim)):
                    result += 0.35 * np.cos(2.5 * (x[i]**3 + x[j]**3 + x[k]**3)) * np.exp(-0.25 * (x[i] - x[j])**2 - 0.15 * (x[j] - x[k])**2)
                    
        # Add a novel fourth-order interaction term
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, min(k+3, self.dim)):
                        result += 0.2 * np.sin(3.0 * (x[i]**4 + x[j]**4 + x[k]**4 + x[l]**4)) * np.exp(-0.1 * (x[i] - x[j])**2 - 0.05 * (x[k] - x[l])**2)
                        
        return result