import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive scaling
        rbf_term = 0.0
        centers = np.linspace(-4.0, 4.0, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            sigma = 0.5 + 0.3 * np.sin(i * 0.7)
            rbf_term += np.exp(-np.sum((x - center)**2) / (2 * sigma**2))
        
        # Sinusoidal oscillation component with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            sin_term += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Adaptive conditioning component
        cond_term = 0.0
        for i in range(self.dim):
            cond = 1.0 + 0.5 * np.sin(i * 0.3)
            cond_term += cond * x[i]**2
        
        # Cross-dimensional coupling with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                weight = np.exp(-dist / (1.0 + 0.1 * i))
                cross_term += weight * np.sin(dist)
        
        # Global shaping term with polynomial and trigonometric components
        shape_term = np.sum(x**4) + 0.5 * np.sum(np.sin(x)) + 0.3 * np.sum(np.cos(x))
        
        # Combine all terms with dynamic weights
        weights = [0.3 + 0.1 * np.sin(self.dim * 0.5), 
                  0.25 + 0.1 * np.cos(self.dim * 0.7),
                  0.2 + 0.1 * np.sin(self.dim * 0.9),
                  0.15 + 0.1 * np.cos(self.dim * 1.1),
                  0.1 + 0.1 * np.sin(self.dim * 1.3)]
        
        result = (weights[0] * rbf_term + 
                 weights[1] * sin_term + 
                 weights[2] * cond_term + 
                 weights[3] * cross_term + 
                 weights[4] * shape_term)
        
        # Add small noise for additional complexity
        noise = 0.001 * np.random.rand()
        
        return result + noise