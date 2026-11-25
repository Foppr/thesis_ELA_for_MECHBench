import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Chaotic exponential decay with sinusoidal modulation
        for i in range(self.dim):
            f += np.exp(-0.1 * np.abs(x[i])) * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[(i + 1) % self.dim])
            
        # Adaptive dimensional coupling with exponentially decaying weights
        for i in range(self.dim):
            weight = np.exp(-0.05 * i)
            f += weight * (x[i]**4 + x[(i + 1) % self.dim]**3) * np.sin(5 * x[i])
            
        # Multi-scale chaotic oscillations with varying amplitudes
        for i in range(self.dim):
            f += 0.5 * np.sin(10 * x[i]) * np.cos(7 * x[(i + 2) % self.dim]) * np.sin(4 * x[(i + 3) % self.dim])
            
        # Exponentially increasing penalty terms
        for i in range(self.dim):
            f += 0.1 * np.exp(0.2 * np.abs(x[i])) * x[i]**2
            
        # Cross-dimensional interaction with phase-shifted chaotic components
        for i in range(self.dim):
            f += 0.3 * np.sin(6 * x[i] + np.pi/4) * np.cos(8 * x[(i + 1) % self.dim] - np.pi/3) * np.sin(2 * x[(i + 3) % self.dim])
            
        # Asymmetric penalty with cubic and quartic terms
        f += 0.2 * np.sum(np.abs(x)**3.5) + 0.15 * np.sum(x**4)
        
        # Non-uniform chaotic modulation with dimension-dependent frequencies
        for i in range(self.dim):
            freq = 2 + 0.5 * np.sin(i)
            f += 0.25 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Additional chaotic gradient-like interactions
        for i in range(self.dim):
            f += 0.18 * (x[i] - 0.5)**3 * np.sin(4 * x[(i + 2) % self.dim])
            
        return f