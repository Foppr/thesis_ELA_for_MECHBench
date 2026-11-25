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
        
        # Trigonometric wave components with dynamic amplitudes and frequencies
        for i in range(self.dim):
            amplitude = 2.5 + 0.5 * np.sin(i * 0.5)
            f_val += amplitude * np.sin(self.wave_frequencies[i] * x[i]) * \
                     np.cos(self.wave_frequencies[i] * x[i] * 0.8) + \
                     1.2 * np.sin(self.wave_frequencies[i] * x[i] * 1.5)
        
        # Enhanced polynomial coupling terms with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling range
                weight = self.coupling_weights[i][j] * np.exp(-0.2 * (j - i))
                coupling = weight * (x[i]**2 + x[j]**2) * (1.0 + 0.3 * np.sin(x[i] * x[j]))
                f_val += 0.8 * coupling
        
        # Stochastic perturbations with enhanced randomness
        for i in range(self.dim):
            f_val += self.stochastic_coefficients[i] * np.sin(x[i] * 12) * \
                     np.cos(x[i] * 9) + \
                     0.4 * np.random.uniform(-1, 1) * np.exp(-0.3 * x[i]**2)
        
        # Cross-dimensional interactions with dynamic modulation
        for i in range(self.dim):
            f_val += 0.6 * np.sin(x[i] * 2.5 + np.sum(x) * 0.15) * \
                     np.cos(x[i] * 1.8 + np.sum(x) * 0.08)
        
        # High-order interaction terms with modified exponents
        for i in range(self.dim):
            f_val += 0.4 * (x[i]**5) + \
                     0.2 * np.sin(x[i]**3) * np.cos(x[i]**2.5)
        
        # Asymmetric coupling with dynamic weights and enhanced nonlinearity
        for i in range(1, self.dim):
            weight = 0.7 + 0.3 * np.sin(i * 0.6)  # Modified weight function
            f_val += weight * (x[i] - x[i-1])**4
        
        # Additional cubic cross-dimensional interactions with variable coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_strength = 0.4 + 0.2 * np.sin(i * 0.3)
                f_val += coupling_strength * (x[i]**3) * x[j]
        
        # Global sinusoidal modulation with enhanced complexity
        f_val += 0.8 * np.sin(np.sum(x**2) * 0.15) + \
                 0.5 * np.cos(np.prod(x)) + \
                 0.4 * np.sin(np.sum(np.abs(x))) + \
                 0.3 * np.cos(np.sum(x**3) * 0.05)
        
        # Additional multimodal component to increase landscape complexity
        f_val += 0.2 * np.sum(np.sin(2 * x) * np.cos(3 * x))
        
        return f_val