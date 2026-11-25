import numpy as np

class StructuredChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency and amplitude parameters for sinusoidal components
        self.freqs = np.linspace(1.5, 4.0, dim)
        self.amps = np.linspace(0.3, 2.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential term with varying exponents to create sharper saddles
        poly_term = np.sum((x**4 + 0.3 * x**3 - 0.8 * x**2 + 0.1 * x)**2)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += self.amps[i] * np.sin(self.freqs[i] * x[i]) * np.cos(0.7 * x[i])
            
        # Gradient-dependent conditioning: modify based on local gradient magnitude with stronger effect
        grad_magnitude = np.sum(np.abs(x))  # Simplified gradient approximation
        condition_factor = 1.0 + 0.5 * np.exp(-0.15 * grad_magnitude)
        
        # Cross-dimensional coupling with enhanced exponential decay and additional nonlinear interaction
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_term += np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(2.5 * x[i] + 1.2 * x[j]) * np.cos(0.5 * x[i] * x[j])
            
        # Combine all terms with modified weights
        result = 0.35 * poly_term + 0.35 * sin_term + 0.25 * cross_term + 0.05 * condition_factor
        
        return result