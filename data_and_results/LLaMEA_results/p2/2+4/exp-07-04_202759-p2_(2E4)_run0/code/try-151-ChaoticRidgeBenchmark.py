import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with varying exponents and coefficients
        poly_chaos = 0
        for i in range(self.dim):
            poly_chaos += (i + 1) * np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 1) * 0.5) * (x[i]**(i % 5 + 2))
        
        # Sinusoidal wave interference with dynamic frequencies and amplitudes
        wave = 0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(x[i] * 0.7)
            amp = 3 + 2 * np.cos(x[i] * 0.3)
            wave += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Gradient-based attraction fields towards multiple local minima
        attraction = 0
        centers = np.linspace(-4.5, 4.5, min(10, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            attraction += 10 * np.exp(-0.5 * (x[i] - center)**2) * np.sin(5 * (x[i] - center))
        
        # Sharp ridge and valley structure using hyperbolic tangent and exponential terms
        ridge_valley = 0
        for i in range(self.dim):
            ridge_valley += np.tanh(10 * x[i]) * np.exp(-0.3 * x[i]**2) + np.exp(-0.5 * (x[i] - 2)**2) * np.sin(15 * x[i])
        
        # Cross-dimensional coupling with chaotic modulation
        coupling = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Combined weighted sum of all components
        return 0.25 * poly_chaos + 0.30 * wave + 0.20 * attraction + 0.15 * ridge_valley + 0.10 * coupling