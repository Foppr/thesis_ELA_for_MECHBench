import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with mixed degrees
        polynomial = np.sum(x**4 + 0.5 * x**3 + 2 * x**2)
        
        # Radial basis function component with multiple centers
        rbfs = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                rbfs += np.exp(-0.5 * (x[i] - centers[i])**2) * np.sin(2 * np.pi * x[i])
                
        # Trigonometric coupling between dimensions
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(x[i] + x[j]) * np.cos(0.5 * x[i] * x[j])
                
        # High-frequency oscillatory component
        oscillatory = 0
        for i in range(self.dim):
            oscillatory += np.sin(10 * x[i]) * np.cos(7 * x[i]) + 0.3 * np.sin(15 * x[i])
            
        # Saddle-like structure with exponential modulation
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.3 * x[i]**2) + 0.5 * (x[i]**4 - 2 * x[i]**2)
            
        # Cross-term interaction with varying weights
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                cross_terms += (x[i] * x[j])**2 * np.sin(0.3 * (x[i]**2 + x[j]**2))
                
        # Add a global scaling factor and noise-like perturbation
        noise = 0.1 * np.sum(np.sin(x)**2)
        
        return (0.4 * polynomial + 
                0.3 * rbfs + 
                0.2 * trig_coupling + 
                0.15 * oscillatory + 
                0.25 * saddle + 
                0.3 * cross_terms + 
                noise)