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
            result += (xi**6 - 10 * xi**4 + 35 * xi**2 - 30) * np.sin(0.7 * xi) + 0.5 * xi**5 * np.cos(1.2 * xi)
            
        # Add extended cross-dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):  # Increased coupling range
                # Introduce highly non-linear dependencies with dynamic interaction strength
                distance = (x[i] - x[j])**2
                result += 0.8 * np.exp(-0.3 * distance) * np.sin(4 * (x[i] + x[j])) * np.cos(0.6 * (x[i] - x[j]))
                
        # Add a global scaling term with enhanced conditioning difficulty
        result += 0.04 * np.sum(x**9) + 0.05 * np.sum(np.cos(6 * x)) + 0.02 * np.sum(np.sin(3 * x))
        
        # Add a highly non-separable interaction term involving all dimensions with cubic coupling
        result += 0.6 * np.exp(-0.15 * np.sum((x - np.mean(x))**2)) * np.cos(0.7 * np.sum(x**4))
        
        # Add a novel high-order interaction term for increased complexity
        result += 0.35 * np.sum(np.sin(2.5 * x) * np.cos(1.2 * x)) + 0.25 * np.sum(x**3 * np.exp(-0.1 * x**2))
        
        # Add additional quartic and quintic interaction terms for enhanced multimodality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.12 * (x[i]**3 + x[j]**3) * np.sin(1.5 * (x[i] - x[j])) * np.cos(1.1 * (x[i] + x[j]))
                
        # Add a highly non-separable term with exponential decay and multiple trigonometric components
        result += 0.2 * np.exp(-0.08 * np.sum(np.abs(x))) * np.sin(0.8 * np.sum(x**2)) * np.cos(0.3 * np.sum(x**5))
        
        return result