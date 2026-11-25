import numpy as np

class PolynomialTrigonometricPerturbationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave frequencies and stochastic parameters
        self.wave_frequencies = np.linspace(0.5, 3.0, dim)
        self.stochastic_params = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with trigonometric modulation
        f_val = np.sum(x**4) * (1.0 + 0.3 * np.cos(np.sum(x) * 0.2))
        
        # Trigonometric wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.7 * np.sin(self.wave_frequencies[i] * x[i]) * \
                     np.cos(self.wave_frequencies[i] * x[i] * 0.4) + \
                     0.5 * np.sin(self.wave_frequencies[i] * x[i] * 1.5)
        
        # Polynomial interactions with dynamic exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exponent = 2 + 0.5 * np.sin(i * 0.3 + j * 0.4)
                f_val += 0.3 * (x[i]**exponent) * (x[j]**(exponent + 0.5)) + \
                         0.2 * np.cos(x[i] + x[j])
        
        # Stochastic perturbations with chaotic-like behavior
        for i in range(self.dim):
            stochastic_term = self.stochastic_params[i] * np.sin(x[i] * 10 + i) * \
                              np.cos(x[i] * 7 + i) + \
                              0.1 * np.random.normal(0, 1)
            f_val += 0.4 * stochastic_term * (1.0 + 0.2 * np.sin(i * 0.5))
        
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.exp(-0.2 * (j - i)) * np.cos(x[i] * x[j])
                f_val += 0.3 * coupling * (x[i]**2 + x[j]**2)
        
        # Asymmetric polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.25 * (diff**4 + 0.4 * np.abs(diff)**3) + \
                         0.15 * np.sin(x[i]) * np.sin(x[i-1])
        
        # Final global modulation with multi-wave interference
        f_val += 0.2 * np.sin(np.sum(np.cos(x))) + \
                 0.25 * np.cos(np.sum(np.sin(x))) + \
                 0.1 * np.sin(np.prod(np.abs(x)) * 0.3)
        
        return f_val