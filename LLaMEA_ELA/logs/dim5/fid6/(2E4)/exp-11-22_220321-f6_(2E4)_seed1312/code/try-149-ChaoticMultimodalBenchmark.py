import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.polynomial_order = 6
        self.fractal_dimension = 1.6
        self.ridge_strength = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with modified weights
        poly_term = 0.0
        weights = np.linspace(0.3, 1.7, self.polynomial_order)
        for i in range(self.dim):
            coord = x[i]
            for n in range(1, self.polynomial_order + 1):
                poly_term += (coord ** n) / (n * (n + 2)) * weights[n-1]
        
        # Modified fractal Brownian motion with altered scaling
        fbm_term = 0.0
        for i in range(self.dim):
            hurst = self.fractal_dimension
            scale = np.abs(coord) ** hurst + 0.15 * np.sin(coord * 4.0)
            fbm_term += scale * np.cos(coord * 2.0)
        
        # Refined adaptive ridge interactions with enhanced modulation
        ridge_term = 0.0
        for i in range(self.dim):
            mod_val = np.sin(i * 0.9 + 1.2) * np.cos(x[i] * 0.4)
            ridge_mod = 1.0 + self.ridge_strength * (np.sin(x[i] * mod_val) + 0.3 * np.cos(x[i] * 2.5))
            ridge_term += ridge_mod * (x[i] ** 2) * np.exp(-0.07 * x[i]**2)
        
        # Enhanced cross-dimensional coupling with modified interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j] * 1.5)
                distance = np.abs(x[i] - x[j])
                cross_term += asym_interaction / (1.0 + distance ** 2.0)
        
        # Modified global scaling with multi-frequency modulation
        sum_x = np.sum(x)
        global_scale = 1.0 + 0.4 * np.sin(sum_x * 0.4) * np.cos(self.dim * 0.25) * np.exp(-0.15 * sum_x**2)
        
        # Balanced weighted combination
        return global_scale * (0.3 * poly_term + 0.25 * fbm_term + 0.25 * ridge_term + 0.2 * cross_term)