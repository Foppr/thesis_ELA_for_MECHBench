import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        radial = np.sum(x**2)
        radial_exp = np.exp(-0.1 * radial)
        
        # Trigonometric coupling between dimensions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(0.5 * x[i] * x[j]) * np.cos(0.3 * (x[i]**2 + x[j]**2))
                
        # Multimodal sine components with varying frequencies
        multimodal = 0
        for i in range(self.dim):
            multimodal += (np.sin(3 * x[i]) + 0.5 * np.sin(7 * x[i]) + 
                          0.3 * np.sin(11 * x[i])) * np.exp(-0.2 * x[i]**2)
                          
        # Radial symmetry with polynomial terms
        symmetry = 0
        for i in range(self.dim):
            symmetry += (x[i]**4 - 2 * x[i]**2 + 1) * np.cos(0.5 * radial)
            
        # Cross-dimensional interaction with exponential modulation
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                cross_interaction += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(2 * x[i] + x[j])
                
        # Gaussian-like local minima with varying depths
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.exp(-0.5 * (x[i] - 1)**2) + 0.5 * np.exp(-0.5 * (x[i] + 1)**2)
            
        # Combine all components with carefully tuned weights
        return (0.4 * radial_exp + 
                0.3 * coupling + 
                0.2 * multimodal + 
                0.15 * symmetry + 
                0.25 * cross_interaction + 
                0.1 * local_minima + 
                0.5 * np.sum(np.sin(x)**2))