import numpy as np

class PolynomialWaveRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave parameters and ridge coefficients
        self.wave_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.ridge_coefficients = np.random.uniform(-1.0, 1.0, dim)
        self.interaction_strengths = np.random.uniform(0.1, 2.0, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive scaling
        f_val = 0.5 * np.sum(x**4) + 0.3 * np.sum(x**2)
        
        # Trigonometric wave interference patterns
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += np.sin(self.wave_frequencies[i] * x[i]) * \
                       np.cos(self.wave_frequencies[i] * x[i] * 1.5) + \
                       0.5 * np.sin(self.wave_frequencies[i] * x[i] * 3.0)
        f_val += 0.8 * wave_sum
        
        # Adaptive ridge structures with varying steepness
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += self.ridge_coefficients[i] * np.exp(-0.5 * (x[i] - 2.0)**2) + \
                         0.3 * np.sin(x[i] * 2.0)
        f_val += 0.6 * ridge_term
        
        # Multi-scale interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                interaction = self.interaction_strengths[i,j] * np.exp(-distance * 0.5)
                f_val += 0.2 * interaction * (x[i]**2 + x[j]**2)
        
        # Polynomial chaos expansion with mixed terms
        chaos_terms = 0.0
        for i in range(self.dim):
            chaos_terms += 0.1 * x[i]**3 + 0.05 * x[i]**5 + \
                          0.2 * np.sin(x[i] * 4.0) * np.cos(x[i] * 2.0)
        f_val += 0.4 * chaos_terms
        
        # Cross-dimensional coupling with varying weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.interaction_strengths[i,j] * np.sin(x[i] + x[j]) * \
                               np.cos(x[i] - x[j])
        f_val += 0.3 * coupling
        
        # Asymmetric scaling with global interaction
        global_interaction = np.sum(np.sin(x)) * np.sum(np.cos(x))
        f_val += 0.25 * global_interaction + 0.1 * np.abs(np.sum(x)**3)
        
        return f_val