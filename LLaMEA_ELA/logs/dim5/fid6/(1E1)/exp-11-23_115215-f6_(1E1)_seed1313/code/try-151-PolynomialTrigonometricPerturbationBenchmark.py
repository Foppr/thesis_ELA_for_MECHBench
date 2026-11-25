import numpy as np

class PolynomialTrigonometricPerturbationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave parameters and stochastic coefficients
        self.wave_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.stochastic_coefficients = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        f_val = np.sum(x**4) * (1.0 + 0.1 * np.sin(np.sum(x) * 0.2))
        
        # Trigonometric wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 2.0 * np.sin(self.wave_frequencies[i] * x[i]) * \
                     np.cos(self.wave_frequencies[i] * x[i] * 0.7) + \
                     1.5 * np.sin(self.wave_frequencies[i] * x[i] * 1.3)
        
        # Polynomial coupling terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.exp(-0.2 * (j - i)) * (x[i]**2 + x[j]**2)
                f_val += 0.5 * coupling
        
        # Stochastic perturbations
        for i in range(self.dim):
            f_val += self.stochastic_coefficients[i] * np.sin(x[i] * 10) * \
                     np.cos(x[i] * 7) + \
                     0.3 * np.random.uniform(-1, 1) * np.exp(-0.5 * x[i]**2)
        
        # Cross-dimensional interactions with sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.4 * np.sin(x[i] * 2 + np.sum(x) * 0.1) * \
                     np.cos(x[i] * 1.5 + np.sum(x) * 0.05)
        
        # High-order interaction terms
        for i in range(self.dim):
            f_val += 0.2 * (x[i]**5) + \
                     0.1 * np.sin(x[i]**3) * np.cos(x[i]**2)
        
        # Asymmetric coupling with dynamic weights
        for i in range(1, self.dim):
            weight = 0.5 + 0.5 * np.sin(i * 0.3)
            f_val += weight * (x[i] - x[i-1])**3
        
        # Global sinusoidal modulation
        f_val += 0.6 * np.sin(np.sum(x**2) * 0.1) + \
                 0.3 * np.cos(np.prod(x)) + \
                 0.2 * np.sin(np.sum(np.abs(x)))
        
        return f_val