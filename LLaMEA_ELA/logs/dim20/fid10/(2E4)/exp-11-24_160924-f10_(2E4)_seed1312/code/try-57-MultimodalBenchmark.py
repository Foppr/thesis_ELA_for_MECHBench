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
            # Slight modification to the base polynomial and trigonometric terms
            result += (xi**7 - 13 * xi**5 + 48 * xi**3 - 39 * xi) * np.sin(0.85 * xi) + 0.42 * xi**6 * np.cos(1.4 * xi)
            
        # Add extended cross-dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+10, self.dim)):  # Reduced coupling range for increased difficulty
                # Slight change in interaction strength and frequency
                distance = (x[i] - x[j])**2
                result += 0.95 * np.exp(-0.35 * distance) * np.sin(4.8 * (x[i] + x[j])) * np.cos(0.75 * (x[i] - x[j]))
                
        # Add a global scaling term with enhanced conditioning difficulty
        result += 0.055 * np.sum(x**10) + 0.065 * np.sum(np.cos(7.2 * x)) + 0.035 * np.sum(np.sin(4.1 * x))
        
        # Add a highly non-separable interaction term involving all dimensions with cubic coupling
        result += 0.72 * np.exp(-0.22 * np.sum((x - np.mean(x))**2)) * np.cos(0.82 * np.sum(x**5))
        
        # Add a novel high-order interaction term for increased complexity
        result += 0.42 * np.sum(np.sin(3.1 * x) * np.cos(1.4 * x)) + 0.32 * np.sum(x**2 * np.exp(-0.16 * x**2))
        
        # Add additional quartic and quintic interaction terms for enhanced multimodality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.16 * (x[i]**4 + x[j]**4) * np.sin(2.1 * (x[i] - x[j])) * np.cos(1.35 * (x[i] + x[j]))
                
        # Add a highly non-separable term with exponential decay and multiple trigonometric components
        result += 0.26 * np.exp(-0.11 * np.sum(np.abs(x))) * np.sin(0.92 * np.sum(x**3)) * np.cos(0.42 * np.sum(x**6))
        
        return result