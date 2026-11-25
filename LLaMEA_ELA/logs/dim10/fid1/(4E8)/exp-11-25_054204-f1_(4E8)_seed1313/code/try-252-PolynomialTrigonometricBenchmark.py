import numpy as np

class PolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute angular frequencies for trigonometric components
        self.freqs = np.arange(1, dim + 1) * np.pi / 4.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive exponents
        base_poly = np.sum((x**3) * (1.0 + 0.1 * np.sin(self.freqs)))
        
        # Trigonometric interference pattern with radial coupling
        trig_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_interference += np.sin(x[i] * x[j]) * np.cos((x[i] + x[j]) / 2.0)
        
        # Radial symmetry with adaptive scaling
        radial_term = np.sum(np.exp(-0.5 * (x**2)) * np.cos(self.freqs * np.sqrt(np.sum(x**2))))
        
        # Cross-dimensional polynomial interactions
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**2) * (x[j]**3) * np.sin((x[i] + x[j]) / 3.0)
        
        # Adaptive harmonic modulation
        harmonic_mod = 0.0
        for i in range(self.dim):
            harmonic_mod += np.sin(self.freqs[i] * x[i]) * np.cos(self.freqs[i] * x[i])
        
        # Multi-scale periodic component with fractal-like behavior
        periodic_component = 0.0
        for i in range(self.dim):
            periodic_component += np.sin(2.0 * self.freqs[i] * x[i]) * np.cos(3.0 * self.freqs[i] * x[i])
        
        # Radial polynomial with exponential decay
        radial_poly = np.sum(x**4 * np.exp(-0.1 * np.abs(x)))
        
        # Sine-cosine coupled interactions
        coupling_term = 0.0
        for i in range(self.dim):
            coupling_term += np.sin(x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.5 * (x[i]**2))
        
        # Multi-dimensional Gaussian-like modulation
        gaussian_mod = np.sum(np.exp(-0.5 * (x**2) / (1.0 + 0.2 * np.abs(x))))
        
        # Adaptive polynomial with exponential weights
        adaptive_poly = np.sum((x**5) * np.exp(-0.3 * np.abs(x)) * np.cos(self.freqs))
        
        # Final combined function with dimension-dependent scaling
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale_factor * (base_poly + trig_interference + radial_term + 
                              poly_interaction + harmonic_mod + periodic_component + 
                              radial_poly + coupling_term + gaussian_mod + adaptive_poly)