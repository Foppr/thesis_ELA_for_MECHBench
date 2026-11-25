import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.5 * np.sin(2 * x[i]) * np.cos(3 * x[(i + 1) % self.dim]) * np.sin(4 * x[(i + 2) % self.dim])
            
        # Add polynomial coupling terms with varying exponents
        for i in range(self.dim):
            f += 0.2 * x[i]**3 * x[(i + 1) % self.dim]**2 + 0.15 * x[i]**2 * x[(i + 2) % self.dim]**3
            
        # Add adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        f *= scale_factor
        
        # Add chaotic interaction terms with phase shifts
        for i in range(self.dim):
            f += 0.3 * np.sin(5 * x[i] + 0.5) * np.cos(7 * x[(i + 3) % self.dim] - 1.2)
            
        # Add irregular penalty terms with exponential scaling
        f += 0.2 * np.sum(np.exp(0.5 * np.abs(x)) - 1)
        
        # Add cross-dimensional cubic interactions
        for i in range(self.dim):
            f += 0.1 * x[i]**3 * x[(i + 1) % self.dim] * x[(i + 2) % self.dim]
            
        # Add multi-modal sinusoidal components with varying intensities
        for i in range(self.dim):
            f += 0.4 * np.sin(6 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            
        # Add higher-order polynomial interactions
        f += 0.1 * np.sum(x**4)
        
        return f