import numpy as np

class PolynomialTrigonometricPerturbationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave parameters and stochastic coefficients
        self.wave_frequencies = np.random.uniform(0.3, 2.5, dim)
        self.stochastic_coefficients = np.random.uniform(-0.3, 0.3, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        f_val = np.sum(x**4) * (1.0 + 0.05 * np.sin(np.sum(x) * 0.1))
        
        # Trigonometric wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 1.5 * np.sin(self.wave_frequencies[i] * x[i]) * \
                     np.cos(self.wave_frequencies[i] * x[i] * 0.6) + \
                     1.2 * np.sin(self.wave_frequencies[i] * x[i] * 1.2)
        
        # Polynomial coupling terms with modified exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range
                coupling = np.exp(-0.2 * (j - i)) * (x[i]**2 + x[j]**2)
                f_val += 0.5 * coupling  # Reduced coupling strength
        
        # Stochastic perturbations
        for i in range(self.dim):
            f_val += self.stochastic_coefficients[i] * np.sin(x[i] * 8) * \
                     np.cos(x[i] * 6) + \
                     0.2 * np.random.uniform(-1, 1) * np.exp(-0.4 * x[i]**2)
        
        # Cross-dimensional interactions with sinusoidal modulation (modified)
        for i in range(self.dim):
            f_val += 0.4 * np.sin(x[i] * 1.5 + np.sum(x) * 0.08) * \
                     np.cos(x[i] * 1.2 + np.sum(x) * 0.03)
        
        # High-order interaction terms (modified)
        for i in range(self.dim):
            f_val += 0.2 * (x[i]**5) + \
                     0.1 * np.sin(x[i]**3) * np.cos(x[i]**2)
        
        # Asymmetric coupling with dynamic weights (modified)
        for i in range(1, self.dim):
            weight = 0.5 + 0.3 * np.sin(i * 0.3)  # Modified weight function
            f_val += weight * (x[i] - x[i-1])**3
        
        # Additional cubic cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+2, self.dim)):
                f_val += 0.2 * (x[i]**3) * x[j]  # New cubic coupling term
        
        # Global sinusoidal modulation (modified)
        f_val += 0.5 * np.sin(np.sum(x**2) * 0.08) + \
                 0.3 * np.cos(np.prod(x)) + \
                 0.2 * np.sin(np.sum(np.abs(x)))
        
        return f_val