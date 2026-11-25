import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.polynomial_order = 5
        self.fractal_dimension = 1.3
        self.ridge_strength = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_term = 0.0
        for i in range(self.dim):
            coord = x[i]
            for n in range(1, self.polynomial_order + 1):
                poly_term += (coord ** n) / (n * (n + 1))
        
        # Fractal Brownian motion component using fractional Brownian motion
        fbm_term = 0.0
        for i in range(self.dim):
            # Fractional Brownian motion approximation using Hurst parameter
            hurst = self.fractal_dimension
            # Simple fractal-like scaling based on coordinate magnitude
            scale = np.abs(coord) ** hurst
            fbm_term += scale * np.sin(coord * 2.0)
        
        # Adaptive ridge interactions with chaotic modulation
        ridge_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation using logistic map
            chaos_param = 3.9  # chaotic regime
            # Simple chaotic sequence generation (first few iterations)
            logistic_val = 0.5
            for _ in range(10):
                logistic_val = chaos_param * logistic_val * (1 - logistic_val)
            
            ridge_mod = 1.0 + self.ridge_strength * np.sin(x[i] * logistic_val)
            ridge_term += ridge_mod * (x[i] ** 2) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with chaotic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction term
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                cross_term += interaction / (1.0 + np.abs(x[i] - x[j]))
        
        # Global chaotic scaling factor
        global_scale = 1.0 + 0.5 * np.sin(np.sum(x) * 0.2) * np.cos(self.dim * 0.1)
        
        return global_scale * (0.3 * poly_term + 0.25 * fbm_term + 0.25 * ridge_term + 0.2 * cross_term)