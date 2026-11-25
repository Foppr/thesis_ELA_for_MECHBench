import numpy as np

class PolynomialTrigonometricPerturbationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave parameters and stochastic coefficients
        self.wave_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.stochastic_coefficients = np.random.uniform(-1.0, 1.0, dim)
        self.coupling_weights = np.random.uniform(0.5, 2.0, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with enhanced nonlinearity
        f_val = np.sum(x**6) * (1.0 + 0.2 * np.sin(np.sum(x) * 0.3))
        
        # Trigonometric wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 3.0 * np.sin(self.wave_frequencies[i] * x[i]) * \
                     np.cos(self.wave_frequencies[i] * x[i] * 0.5) + \
                     2.0 * np.sin(self.wave_frequencies[i] * x[i] * 1.5)
        
        # Polynomial coupling terms with dynamic weights and higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                coupling = self.coupling_weights[i,j] * (x[i]**3 + x[j]**3) * np.exp(-0.2 * (j - i))
                f_val += 1.0 * coupling
        
        # Stochastic perturbations with enhanced variability
        for i in range(self.dim):
            f_val += self.stochastic_coefficients[i] * np.sin(x[i] * 15) * \
                     np.cos(x[i] * 11) + \
                     0.5 * np.random.uniform(-2, 2) * np.exp(-0.3 * x[i]**2)
        
        # Cross-dimensional interactions with higher-order sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.8 * np.sin(x[i] * 3 + np.sum(x**2) * 0.15) * \
                     np.cos(x[i] * 2.5 + np.sum(x) * 0.07)
        
        # High-order interaction terms with complex nonlinearities
        for i in range(self.dim):
            f_val += 0.5 * (x[i]**7) + \
                     0.25 * np.sin(x[i]**4) * np.cos(x[i]**3)
        
        # Asymmetric coupling with dynamic weights and cubic interactions
        for i in range(1, self.dim):
            weight = 0.8 + 0.6 * np.sin(i * 0.6) * np.cos(i * 0.3)
            f_val += weight * (x[i] - x[i-1])**4
        
        # Additional complex cubic cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f_val += 0.5 * (x[i]**4) * x[j]**2 + \
                         0.2 * x[i] * (x[j]**4)
        
        # Global sinusoidal modulation with multiple frequencies
        f_val += 1.0 * np.sin(np.sum(x**3) * 0.15) + \
                 0.6 * np.cos(np.prod(x)) + \
                 0.5 * np.sin(np.sum(np.abs(x)**2))
        
        # Additional noise and irregularity terms
        f_val += 0.3 * np.random.uniform(-1, 1) * np.sin(np.sum(x**4) * 0.2)
        
        return f_val