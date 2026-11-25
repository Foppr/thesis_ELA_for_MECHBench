import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with different scales
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1)
            
        # Add multiple local minima using sine waves with chaotic frequency modulation
        for i in range(self.dim):
            freq = 2 ** (i % 4) * np.sin(x[i]) + 1.5  # Chaotic frequency modulation
            result += 0.7 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Add a complex penalty term with multiple local optima using hybrid functions
        penalty = 0.0
        for i in range(self.dim):
            # Hybrid penalty combining polynomial, exponential, and trigonometric terms
            penalty += (x[i] ** 9 + x[i] ** 6 + x[i] ** 4) * (i + 1) * np.exp(-0.1 * abs(x[i]))
            
        # Add enhanced cross-dimensional interactions with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction with sine-cosine coupling and exponential decay
                coupling = np.sin(x[i]) * np.cos(x[j]) * (i + j) * np.exp(-0.3 * abs(x[i] - x[j]))
                cross_term += coupling * np.sin(2 * x[i] + x[j]) * np.cos(x[i] - 2 * x[j])
                
        return result + 0.2 * penalty + 0.3 * cross_term