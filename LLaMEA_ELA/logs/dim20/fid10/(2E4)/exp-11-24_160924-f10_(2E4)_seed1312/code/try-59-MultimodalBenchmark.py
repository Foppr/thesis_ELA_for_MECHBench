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
            # Increased complexity in base polynomial and trigonometric terms
            result += (xi**9 - 17 * xi**6 + 72 * xi**4 - 58 * xi**2) * np.sin(1.1 * xi) + 0.6 * xi**7 * np.cos(1.8 * xi)
            
        # Add extended cross-dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):  # Further reduced coupling range
                # Increased interaction strength and frequency
                distance = (x[i] - x[j])**2
                result += 1.2 * np.exp(-0.45 * distance) * np.sin(6.2 * (x[i] + x[j])) * np.cos(1.1 * (x[i] - x[j]))
                
        # Add a global scaling term with enhanced conditioning difficulty
        result += 0.08 * np.sum(x**12) + 0.09 * np.sum(np.cos(9.5 * x)) + 0.05 * np.sum(np.sin(5.8 * x))
        
        # Add a highly non-separable interaction term involving all dimensions with quintic coupling
        result += 0.9 * np.exp(-0.3 * np.sum((x - np.mean(x))**2)) * np.cos(1.1 * np.sum(x**7))
        
        # Add a novel high-order interaction term for increased complexity
        result += 0.6 * np.sum(np.sin(4.3 * x) * np.cos(1.9 * x)) + 0.5 * np.sum(x**3 * np.exp(-0.2 * x**2))
        
        # Add additional sextic and septic interaction terms for enhanced multimodality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.22 * (x[i]**6 + x[j]**6) * np.sin(3.5 * (x[i] - x[j])) * np.cos(1.8 * (x[i] + x[j]))
                
        # Add a highly non-separable term with exponential decay and multiple trigonometric components
        result += 0.35 * np.exp(-0.15 * np.sum(np.abs(x))) * np.sin(1.2 * np.sum(x**4)) * np.cos(0.6 * np.sum(x**8))
        
        # Add a new high-dimensional interaction term with cubic coupling and dynamic scaling
        result += 0.48 * np.exp(-0.25 * np.sum((x - np.mean(x))**3)) * np.sin(0.9 * np.sum(x**6))
        
        return result