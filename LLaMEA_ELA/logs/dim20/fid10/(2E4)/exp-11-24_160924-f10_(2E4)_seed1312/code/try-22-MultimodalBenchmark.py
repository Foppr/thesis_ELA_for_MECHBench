import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term with exponential decay
        for i in range(self.dim):
            result += (x[i]**2) * np.exp(-0.1 * np.abs(x[i]))
            
        # Add multi-modal sinusoidal components
        for i in range(self.dim):
            result += 3.0 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            
        # Include cross-dimensional interactions with varying strengths
        for i in range(self.dim):
            if i > 0:
                result += 0.8 * x[i] * x[i-1] * np.exp(-0.5 * (x[i]**2 + x[i-1]**2))
                
        # Add multiple global minima with different shapes
        peaks = np.array([[2.0]*self.dim, [-2.0]*self.dim, [0.0]*self.dim])
        for peak in peaks:
            dist = np.sum((x - peak)**2)
            result += 2.5 * np.exp(-0.3 * dist) + 1.0 * np.exp(-0.1 * dist)
            
        # Add a noise-like perturbation term
        result += 0.2 * np.sum(np.sin(7 * x) * np.cos(4 * x))
        
        return result