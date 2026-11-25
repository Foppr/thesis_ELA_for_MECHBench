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
            for order in range(1, self.polynomial_order + 1):
                poly_term += (coord ** order) * np.sin(order * coord)
        
        # Fractal Brownian motion component with Hurst parameter
        fbm_term = 0.0
        hurst = self.fractal_dimension / 2.0
        for i in range(self.dim):
            # Simple fractal-like scaling
            scale = np.exp(-hurst * np.abs(x[i]))
            fbm_term += scale * np.sin(x[i] * (1.0 + 0.1 * np.sin(i)))
        
        # Adaptive ridge interactions with position-dependent curvature
        ridge_term = 0.0
        for i in range(self.dim):
            # Ridge interaction with neighboring dimensions
            curvature = self.ridge_strength * np.cos(x[i] * 0.5)
            neighbor_interaction = 0.0
            for j in range(max(0, i-1), min(self.dim, i+2)):
                if i != j:
                    neighbor_interaction += (x[i] - x[j]) ** 2
            ridge_term += curvature * neighbor_interaction
        
        # Cross-dimensional coupling with chaotic mixing
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction term
                chaos_factor = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                cross_term += chaos_factor * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Position-dependent time-varying modulation
        time_mod = 1.0 + 0.3 * np.sin(np.sum(x) * 0.2)
        
        # Global scaling and normalization
        global_scale = 1.0 + 0.1 * np.sin(self.dim * 0.3)
        
        return global_scale * (0.3 * poly_term + 0.25 * fbm_term + 0.2 * ridge_term + 0.25 * cross_term) * time_mod