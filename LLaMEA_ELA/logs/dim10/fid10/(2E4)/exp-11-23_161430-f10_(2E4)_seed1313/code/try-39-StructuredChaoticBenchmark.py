import numpy as np

class StructuredChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency and amplitude parameters for sinusoidal components
        self.freqs = np.linspace(1.0, 3.0, dim)
        self.amps = np.linspace(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential term with varying exponents
        poly_term = np.sum((x**3 + 0.5 * x**2 - x)**2)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += self.amps[i] * np.sin(self.freqs[i] * x[i]) * np.cos(0.5 * x[i])
            
        # Gradient-dependent conditioning: modify based on local gradient magnitude
        grad_magnitude = np.sum(np.abs(x))  # Simplified gradient approximation
        condition_factor = 1.0 + 0.3 * np.exp(-0.1 * grad_magnitude)
        
        # Cross-dimensional coupling with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_term += np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(2.0 * x[i] + x[j])
            
        # Combine all terms with adaptive weights
        result = 0.4 * poly_term + 0.3 * sin_term + 0.2 * cross_term + 0.1 * condition_factor
        
        return result