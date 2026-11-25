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
        
        # Base polynomial term with enhanced complexity
        f_val = np.sum(x**4) * (1.0 + 0.1 * np.sin(np.sum(x) * 0.2))
        
        # Trigonometric wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 2.0 * np.sin(self.wave_frequencies[i] * x[i]) * \
                     np.cos(self.wave_frequencies[i] * x[i] * 0.7) + \
                     1.5 * np.sin(self.wave_frequencies[i] * x[i] * 1.3)
        
        # Polynomial coupling terms with modified exponential decay and increased strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling
                coupling = np.exp(-0.3 * (j - i)) * (x[i]**2 + x[j]**2)
                f_val += 1.0 * coupling  # Increased coupling strength
        
        # Stochastic perturbations with modified structure
        for i in range(self.dim):
            f_val += self.stochastic_coefficients[i] * np.sin(x[i] * 10) * \
                     np.cos(x[i] * 7) + \
                     0.3 * np.random.uniform(-1, 1) * np.exp(-0.5 * x[i]**2)
        
        # Cross-dimensional interactions with sinusoidal modulation (enhanced)
        for i in range(self.dim):
            f_val += 0.8 * np.sin(x[i] * 2 + np.sum(x) * 0.1) * \
                     np.cos(x[i] * 1.5 + np.sum(x) * 0.05)
        
        # High-order interaction terms (enhanced)
        for i in range(self.dim):
            f_val += 0.4 * (x[i]**5) + \
                     0.2 * np.sin(x[i]**3) * np.cos(x[i]**2)
        
        # Asymmetric coupling with dynamic weights (enhanced)
        for i in range(1, self.dim):
            weight = 0.7 + 0.3 * np.sin(i * 0.5)  # Modified weight function
            f_val += weight * (x[i] - x[i-1])**3
        
        # Additional cubic cross-dimensional interactions (enhanced)
        for i in range(self.dim):
            for j in range(i+1, min(i+2, self.dim)):
                f_val += 0.4 * (x[i]**3) * x[j]  # Enhanced cubic coupling term
        
        # Global sinusoidal modulation (enhanced)
        f_val += 1.0 * np.sin(np.sum(x**2) * 0.1) + \
                 0.5 * np.cos(np.prod(x)) + \
                 0.4 * np.sin(np.sum(np.abs(x)))
        
        # Additional quadratic cross-dimensional terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f_val += 0.2 * (x[i] * x[j])**2
        
        return f_val