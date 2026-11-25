import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple local minima
        radial = np.sum((x**2 + 1) * np.exp(-0.1 * x**2))
        
        # Sinusoidal chaotic component with varying frequencies
        sinusoidal = 0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)
            sinusoidal += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2) + np.sin(freq * x[i] / 3)
        
        # Polynomial interaction terms with high-degree cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-terms to avoid overfitting
                polynomial += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
        
        # Exponential decay component with random coefficients
        exp_decay = 0
        for i in range(self.dim):
            exp_decay += np.exp(-0.5 * (x[i] - np.sin(i))**2) * np.cos(3 * x[i])
        
        # Multiscale oscillation component
        multiscale = 0
        for i in range(self.dim):
            multiscale += np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.sin(x[i]**2)
        
        # Combine all components with carefully tuned weights
        return 0.8 * radial + 0.3 * sinusoidal + 0.4 * polynomial + 0.6 * exp_decay + 0.5 * multiscale + 10 * np.sum(np.abs(x)**0.5)