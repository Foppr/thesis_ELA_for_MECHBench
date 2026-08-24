import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive scaling
        rbfs = []
        for i in range(1, min(6, self.dim + 1)):
            center = np.linspace(-4.0, 4.0, min(5, self.dim))[i-1] if self.dim > 1 else 0.0
            sigma = 0.5 + 0.3 * np.sin(i * 1.5)
            rbfs.append(np.exp(-np.sum((x - center)**2) / (2 * sigma**2)))
        
        # Sinusoidal oscillation component with frequency modulation
        sin_term = np.sum(np.sin(2 * np.pi * x * (1 + 0.3 * np.sin(x))) * 
                         np.cos(3 * np.pi * x * (1 + 0.2 * np.cos(x))) * 
                         np.sin(4 * np.pi * x * (1 + 0.1 * np.sin(x))) * 
                         np.cos(5 * np.pi * x * (1 + 0.1 * np.cos(x))) * 
                         np.sin(6 * np.pi * x * (1 + 0.05 * np.sin(x))))
        
        # Adaptive conditioning component
        cond_term = np.sum((1 + 0.5 * np.sin(self.dim * 0.8)) * x**2 + 
                          (0.8 + 0.3 * np.cos(self.dim * 1.2)) * x**3 + 
                          (0.6 + 0.2 * np.sin(self.dim * 1.6)) * x**4)
        
        # Cross-dimensional coupling with adaptive weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.0 + 0.5 * np.sin(i * 0.7 + self.dim * 0.3)
                cross_term += weight * np.abs(x[i] - x[i+1])**2
        
        # Multimodal component with multiple local minima
        multi_term = np.sum(np.sin(10 * x) * np.cos(5 * x) * 
                           np.sin(7 * x) * np.cos(3 * x) * 
                           np.sin(9 * x) * np.cos(4 * x) * 
                           np.sin(6 * x) * np.cos(2 * x) * 
                           np.sin(8 * x) * np.cos(1 * x))
        
        # Combine all terms with dynamic weights
        weights = [0.25 + 0.05 * np.sin(self.dim * 0.5),
                  0.30 + 0.06 * np.cos(self.dim * 0.7),
                  0.20 + 0.04 * np.sin(self.dim * 0.9),
                  0.15 + 0.03 * np.cos(self.dim * 1.1),
                  0.10 + 0.02 * np.sin(self.dim * 1.3)]
        
        result = (weights[0] * np.sum(rbfs) + 
                 weights[1] * sin_term + 
                 weights[2] * cond_term + 
                 weights[3] * cross_term + 
                 weights[4] * multi_term)
        
        # Add small random noise
        noise = 0.001 * np.random.rand()
        
        return result + noise