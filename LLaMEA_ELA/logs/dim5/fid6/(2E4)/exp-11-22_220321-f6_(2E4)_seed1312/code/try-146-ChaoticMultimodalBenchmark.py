import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.polynomial_order = 6
        self.fractal_dimension = 1.4
        self.ridge_strength = 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with weighted terms
        poly_term = 0.0
        weights = np.linspace(0.5, 1.5, self.polynomial_order)
        for i in range(self.dim):
            coord = x[i]
            for n in range(1, self.polynomial_order + 1):
                poly_term += (coord ** n) / (n * (n + 1)) * weights[n-1]
        
        # Improved fractal Brownian motion with multi-scale interaction
        fbm_term = 0.0
        for i in range(self.dim):
            hurst = self.fractal_dimension
            # Multi-scale fractal scaling
            scale = np.abs(coord) ** hurst + 0.1 * np.sin(coord * 3.0)
            fbm_term += scale * np.cos(coord * 1.5)
        
        # Refined adaptive ridge interactions with dynamic modulation
        ridge_term = 0.0
        for i in range(self.dim):
            # Dynamic chaotic modulation using sine-based sequence
            mod_val = np.sin(i * 0.7 + 1.0) * np.cos(x[i] * 0.3)
            ridge_mod = 1.0 + self.ridge_strength * (np.sin(x[i] * mod_val) + 0.5 * np.cos(x[i] * 2.0))
            ridge_term += ridge_mod * (x[i] ** 2) * np.exp(-0.05 * x[i]**2)
        
        # Enhanced cross-dimensional coupling with asymmetric interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric chaotic interaction term
                asym_interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                distance = np.abs(x[i] - x[j])
                cross_term += asym_interaction / (1.0 + distance ** 1.5)
        
        # Improved global scaling with multi-frequency modulation
        sum_x = np.sum(x)
        global_scale = 1.0 + 0.3 * np.sin(sum_x * 0.3) * np.cos(self.dim * 0.2) * np.exp(-0.1 * sum_x**2)
        
        # Balanced weighted combination
        return global_scale * (0.25 * poly_term + 0.3 * fbm_term + 0.2 * ridge_term + 0.25 * cross_term)