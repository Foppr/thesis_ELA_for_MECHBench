import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add polynomial and sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Complex combination of polynomial and trigonometric terms
            result += (xi**7 - 12 * xi**5 + 50 * xi**3 - 40 * xi) * np.sin(0.8 * xi) + 0.4 * xi**6 * np.cos(1.5 * xi)
            
        # Add extended cross-dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+12, self.dim)):  # Increased coupling range
                # Introduce highly non-linear dependencies with dynamic interaction strength
                distance = (x[i] - x[j])**2
                result += 1.2 * np.exp(-0.4 * distance) * np.sin(5 * (x[i] + x[j])) * np.cos(0.7 * (x[i] - x[j]))
                
        # Add a global scaling term with enhanced conditioning difficulty
        result += 0.05 * np.sum(x**9) + 0.06 * np.sum(np.cos(7 * x)) + 0.03 * np.sum(np.sin(4 * x))
        
        # Add a highly non-separable interaction term involving all dimensions with cubic coupling
        result += 0.8 * np.exp(-0.2 * np.sum((x - np.mean(x))**2)) * np.cos(0.8 * np.sum(x**4))
        
        # Add a novel high-order interaction term for increased complexity
        result += 0.5 * np.sum(np.sin(3.0 * x) * np.cos(1.5 * x)) + 0.4 * np.sum(x**2 * np.exp(-0.15 * x**2))
        
        # Add additional high-frequency oscillatory components for increased multimodality
        result += 0.3 * np.sum(np.sin(8 * x) * np.cos(3 * x)) + 0.2 * np.sum(np.tan(0.5 * x) / (1 + x**2))
        
        # Add a complex multi-modal term that creates many local minima
        result += 0.6 * np.sum((x**2 - 4*x + 3)**2 * np.sin(2 * x))
        
        return result