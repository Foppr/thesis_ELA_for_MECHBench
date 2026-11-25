import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components
        gaussian = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) < self.dim else x[i]
            gaussian += np.exp(-0.5 * ((x[i] - center) / 1.5)**2)
        
        # Sinusoidal modulation with varying frequencies
        sinusoidal = 0
        for i in range(self.dim):
            sinusoidal += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Saddle-point structure with polynomial interactions
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1)**2
            
        # Cross-terms creating complex interaction patterns
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-interaction
                cross_terms += 0.5 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
        
        # Add a unique component with exponential decay and oscillation
        oscillatory = 0
        for i in range(self.dim):
            oscillatory += np.exp(-x[i]**2/10) * np.sin(5 * x[i])
            
        # Combine all components with carefully chosen weights
        return 0.3 * gaussian + 0.4 * sinusoidal + 0.2 * saddle + 0.1 * cross_terms + 0.5 * oscillatory + 5 * np.sum(np.abs(x))