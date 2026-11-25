import numpy as np

class StructuredChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency and amplitude parameters for multi-scale sinusoidal components
        self.freqs = np.linspace(0.5, 6.0, dim)
        self.amps = np.linspace(0.1, 3.0, dim)
        # Fractional exponents for enhanced saddle-point complexity
        self.exponents = np.linspace(2.1, 5.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional polynomial potential term with varying non-integer exponents
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**self.exponents[i] + 0.4 * x[i]**(self.exponents[i]-1) - 0.6 * x[i]**2 + 0.2 * x[i])**2
            
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += self.amps[i] * np.sin(self.freqs[i] * x[i]) * np.cos(0.5 * x[i]**2) * np.exp(-0.1 * np.abs(x[i]))
            
        # Gradient-dependent conditioning with exponential decay and dynamic scaling
        grad_magnitude = np.sum(np.abs(x))
        condition_factor = 1.0 + 0.8 * np.exp(-0.2 * grad_magnitude) * np.sin(0.3 * grad_magnitude)
        
        # Enhanced cross-dimensional coupling with fractional powers and multi-scale interactions
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            cross_term += np.exp(-0.5 * (x[i] - x[j])**3) * np.sin(3.0 * x[i] + 1.5 * x[j]) * np.cos(0.7 * x[i] * x[k])
            
        # Additional chaotic component with time-delayed feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            if i > 0:
                chaotic_term += 0.3 * np.sin(x[i-1] + 0.5 * x[i]) * np.cos(2.0 * x[i])
                
        # Combine all terms with modified weights and introduce additional nonlinearity
        result = 0.4 * poly_term + 0.3 * sin_term + 0.2 * cross_term + 0.08 * condition_factor + 0.02 * chaotic_term
        
        return result