import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with chaotic modulation
        freqs = np.arange(1, self.dim + 1) * np.pi / 2.0
        sinusoidal = np.sum(np.sin(freqs * x) * np.cos(freqs * x * 0.7) * np.exp(-0.1 * np.abs(x)))
        
        # Add cubic and quartic terms with cross-terms for increased complexity
        cubic = 0.1 * np.sum(x**3)
        quartic = 0.05 * np.sum(x**4)
        
        # Cross-terms between dimensions to create interaction
        cross_term = 0.02 * np.sum(x[:-1] * x[1:] * np.sin(2.0 * x[:-1] + x[1:]))
        
        # Add a chaotic component with exponential decay
        chaotic = 0.3 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-6)))
        
        # Combine all components
        result = result + sinusoidal + cubic + quartic + cross_term + chaotic
        
        return result