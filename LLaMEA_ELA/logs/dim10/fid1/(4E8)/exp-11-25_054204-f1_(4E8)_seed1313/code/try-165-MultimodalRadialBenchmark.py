import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights and frequencies for multi-scale interactions
        self.weights = np.exp(-np.arange(dim) / (dim * 0.5))
        self.frequencies = 2.0 + 3.0 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic term with varying weights
        radial_term = np.sum(self.weights * x**2)
        
        # Multi-scale sinusoidal oscillations
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i])
        sin_term *= 0.5
        
        # Cross-dimensional interaction with radial coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        cross_term *= 0.3
        
        # Gaussian radial basis functions with varying centers and widths
        rbfs = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * np.pi / (self.dim + 1))
            width = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 1))
            rbfs += np.exp(-((x[i] - center)**2) / (2 * width**2))
        rbfs *= 0.4
        
        # Polynomial coupling with alternating signs
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += ((-1)**i) * x[i]**3 * np.sin(x[i])
        poly_term *= 0.25
        
        # Scaled harmonic interaction
        harmonic_term = 0.0
        for i in range(1, self.dim):
            harmonic_term += (x[i-1] + x[i])**2 * np.cos(x[i-1] * x[i])
        harmonic_term *= 0.35
        
        # Asymmetric exponential decay with directional coupling
        exp_term = 0.0
        for i in range(self.dim - 1):
            exp_term += np.exp(-np.abs(x[i]) * x[i+1]) * np.sin(x[i] + x[i+1])
        exp_term *= 0.2
        
        # Fourth-order polynomial with sinusoidal modulation
        quartic_term = 0.0
        for i in range(self.dim):
            quartic_term += (x[i]**4) * np.cos(0.5 * x[i])
        quartic_term *= 0.15
        
        # Combined scaling factor based on problem dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale_factor * (radial_term + sin_term + cross_term + rbfs + poly_term + 
                              harmonic_term + exp_term + quartic_term)