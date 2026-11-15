import numpy as np

class MultiscaleOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with multiple centers
        rbfs = 0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i, center in enumerate(centers):
            if i < self.dim:
                rbfs += np.exp(-np.sum((x - center)**2) / 2.0) * np.sin(2 * np.pi * (x[i] - center))
        
        # High-frequency sinusoidal oscillations
        oscillations = np.sum(np.sin(10 * x) * np.cos(5 * x) * np.sin(3 * x)) / self.dim
        
        # Gradient-based attraction fields with varying strengths
        attractions = 0
        for i in range(self.dim):
            attractions += (x[i] - np.sin(x[i]))**2 * (1 + 0.5 * np.sin(i))
        
        # Multi-scale periodic components with varying frequencies
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(2**i * x[i]) * np.cos(3**i * x[i]) / (1 + i)
        
        # Cross-dimensional interaction terms with exponential coupling
        cross_interaction = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_interaction += np.exp(-np.abs(x[i] - x[i+1]) / (1 + i)) * np.sin(x[i] * x[i+1])
        cross_interaction /= (self.dim - 1)
        
        # Add noise component
        noise = 0.01 * np.random.rand()
        
        # Combine all components
        result = 0.3 * rbfs + 0.25 * oscillations + 0.2 * attractions + 0.15 * periodic + 0.1 * cross_interaction
        
        return result + noise