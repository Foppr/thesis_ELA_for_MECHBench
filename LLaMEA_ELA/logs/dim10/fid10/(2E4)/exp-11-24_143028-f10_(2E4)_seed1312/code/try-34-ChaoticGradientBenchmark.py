import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for periodic components
        self.freqs = np.arange(1, dim + 1) * 0.5
        self.amp = 1.0 / (1.0 + np.arange(1, dim + 1) * 0.1)
    
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += self.amp[i] * np.sin(self.freqs[i] * x[i]) * np.cos(self.freqs[i] * x[i])
        
        # Introduce periodic attractor landscape using multi-modal sine waves
        for i in range(self.dim):
            result += 0.3 * np.sin(5 * x[i])**2 + 0.2 * np.cos(7 * x[i])**2
        
        # Add gradient-based non-smoothness with exponential decay
        grad_smooth = 0.0
        for i in range(self.dim):
            grad_smooth += np.exp(-0.1 * np.abs(x[i])) * np.sin(3 * x[i])
        result += 0.1 * grad_smooth**2
        
        # Introduce adaptive condition number via weighted sum of squared variables
        cond_weight = np.linspace(1, 10, self.dim)
        cond_term = np.sum(cond_weight * x**2)
        result += 0.05 * cond_term
        
        # Add boundary proximity penalty with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 0.2 * np.exp(-0.2 * (5.0 - np.abs(x[i]))**2)
        result += boundary_penalty
        
        return result