import numpy as np

class PolynomialTrigonometricPerturbationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave parameters and stochastic coefficients
        self.wave_frequencies = np.random.uniform(1.0, 4.0, dim)
        self.stochastic_coefficients = np.random.uniform(-0.3, 0.3, dim)
        self.coupling_weights = np.random.uniform(0.5, 1.5, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with enhanced nonlinearity
        f_val = np.sum(x**4) * (1.0 + 0.2 * np.sin(np.sum(x) * 0.3))
        
        # Trigonometric wave components with adaptive frequencies and amplitudes
        for i in range(self.dim):
            f_val += 3.0 * np.sin(self.wave_frequencies[i] * x[i]) * \
                     np.cos(self.wave_frequencies[i] * x[i] * 0.5) + \
                     2.0 * np.sin(self.wave_frequencies[i] * x[i] * 1.5)
        
        # Enhanced polynomial coupling terms with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range
                weight = self.coupling_weights[i, j] * np.exp(-0.2 * (j - i))
                coupling = weight * (x[i]**2 + x[j]**2) * (1.0 + 0.1 * np.sin(x[i] * x[j]))
                f_val += 0.8 * coupling
        
        # Improved stochastic perturbations with better distribution
        for i in range(self.dim):
            f_val += self.stochastic_coefficients[i] * np.sin(x[i] * 12) * \
                     np.cos(x[i] * 9) + \
                     0.4 * np.random.uniform(-1, 1) * np.exp(-0.3 * x[i]**2)
        
        # Enhanced cross-dimensional interactions with dynamic modulation
        for i in range(self.dim):
            f_val += 0.6 * np.sin(x[i] * 2.5 + np.sum(x) * 0.15) * \
                     np.cos(x[i] * 1.8 + np.sum(x) * 0.07)
        
        # Higher-order interaction terms with improved structure
        for i in range(self.dim):
            f_val += 0.4 * (x[i]**5) + \
                     0.2 * np.sin(x[i]**3) * np.cos(x[i]**2) + \
                     0.1 * x[i]**6
        
        # Asymmetric coupling with frequency-dependent weights
        for i in range(1, self.dim):
            weight = 0.7 + 0.3 * np.sin(i * 0.5) * np.cos(i * 0.2)
            f_val += weight * (x[i] - x[i-1])**4
        
        # Additional cubic cross-dimensional interactions with variable coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_strength = 0.4 + 0.2 * np.sin(i * 0.3) * np.cos(j * 0.4)
                f_val += coupling_strength * (x[i]**3) * x[j]
        
        # Global sinusoidal modulation with improved scaling
        f_val += 0.8 * np.sin(np.sum(x**2) * 0.15) + \
                 0.5 * np.cos(np.prod(x)) + \
                 0.4 * np.sin(np.sum(np.abs(x))) + \
                 0.2 * np.exp(-0.1 * np.sum(x**2))
        
        return f_val