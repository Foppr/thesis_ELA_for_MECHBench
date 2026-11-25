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
                result += 0.9 * np.exp(-0.4 * distance) * np.sin(5 * (x[i] + x[j])) * np.cos(0.7 * (x[i] - x[j]))
                
        # Add a global scaling term with enhanced conditioning difficulty
        result += 0.05 * np.sum(x**10) + 0.06 * np.sum(np.cos(7 * x)) + 0.03 * np.sum(np.sin(4 * x))
        
        # Add a highly non-separable interaction term involving all dimensions with cubic coupling
        result += 0.7 * np.exp(-0.2 * np.sum((x - np.mean(x))**2)) * np.cos(0.8 * np.sum(x**5))
        
        # Add a novel high-order interaction term for increased complexity
        result += 0.4 * np.sum(np.sin(3 * x) * np.cos(1.5 * x)) + 0.3 * np.sum(x**2 * np.exp(-0.15 * x**2))
        
        # Add additional quartic and quintic interaction terms for enhanced multimodality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * (x[i]**4 + x[j]**4) * np.sin(2 * (x[i] - x[j])) * np.cos(1.3 * (x[i] + x[j]))
                
        # Add a highly non-separable term with exponential decay and multiple trigonometric components
        result += 0.25 * np.exp(-0.1 * np.sum(np.abs(x))) * np.sin(0.9 * np.sum(x**3)) * np.cos(0.4 * np.sum(x**6))
        
        return result