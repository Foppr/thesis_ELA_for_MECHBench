import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with chaotic scaling
        rbfs = np.sum(np.exp(-np.sum((x[:, None] - np.linspace(-5, 5, 20))**2, axis=0) / (2 * 0.5**2)))
        
        # Sinusoidal modulation with chaotic frequency
        freqs = 1 + 2 * np.sin(np.arange(self.dim) * np.pi / 4.0)
        sin_mod = np.sum(np.sin(freqs * x) * np.cos(2 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Asymmetric penalty with exponential growth
        penalty = np.sum(np.where(x >= 0, 2.0 * np.exp(0.5 * x), 0.5 * np.exp(-0.3 * x)))
        
        # Chaotic logistic map component
        logistic = 0.0
        r = 3.9
        for i in range(10):
            logistic += np.sum((r * x * (1 - x))**2)
            
        # Mixed polynomial and hyperbolic tangent
        poly_tanh = np.sum(0.5 * x**2 + 0.1 * x**3 + np.tanh(x) * np.sin(0.5 * x))
        
        # Coupled oscillators with phase coupling
        phases = np.arange(self.dim) * np.pi / 3.0
        oscillators = np.sum(np.sin(x + phases) * np.cos(x - phases))
        
        # Final combined function
        result = rbfs + sin_mod + penalty + logistic + poly_tanh + oscillators
        
        return result