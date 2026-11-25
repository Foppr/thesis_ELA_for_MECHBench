import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add chaotic sinusoidal interactions with non-integer frequencies
        for i in range(self.dim):
            f += 0.5 * np.sin(7.3 * x[i]) * np.cos(6.1 * x[(i + 1) % self.dim]) * np.sin(4.7 * x[(i + 2) % self.dim])
            
        # Add saddle point contributions with asymmetric penalty terms
        for i in range(self.dim):
            f += 0.25 * (np.sin(3.2 * x[i])**2 - 0.5) * (np.cos(2.8 * x[(i + 1) % self.dim])**2 - 0.3)
            
        # Add higher-order interaction terms with exponential decay
        for i in range(self.dim):
            f += 0.1 * np.exp(-0.1 * np.abs(x[i])) * np.sin(9.5 * x[(i + 1) % self.dim]) * np.cos(7.8 * x[(i + 3) % self.dim])
            
        # Add modified penalty terms with discontinuous components
        f += 0.05 * np.sum(np.abs(x)**1.5) + 0.02 * np.sum(x**6) + 0.3 * np.sum(np.sin(0.7 * x) * np.cos(0.4 * x))
        
        # Add a chaotic component using logistic map-like behavior
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(10 * x[i] + np.sin(5 * x[(i + 1) % self.dim]))
        f += 0.1 * chaos
        
        return f