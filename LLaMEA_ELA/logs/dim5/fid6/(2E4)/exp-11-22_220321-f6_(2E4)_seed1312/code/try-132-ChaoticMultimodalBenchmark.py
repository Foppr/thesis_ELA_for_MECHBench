import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.polynomial_degree = 5
        self.fractal_dimension = 1.3
        self.ridge_adaptation = 0.7
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_term = 0.0
        for i in range(self.dim):
            coord = x[i]
            for deg in range(1, self.polynomial_degree + 1):
                poly_term += (coord ** deg) * np.sin(deg * coord)
        
        # Fractal Brownian motion component with Hurst parameter
        fbm_term = 0.0
        hurst = self.fractal_dimension / self.dim
        for i in range(self.dim):
            fbm_term += np.sin(x[i] * (1.0 + hurst * np.cos(i))) * np.cos(x[i] * (1.0 + hurst * np.sin(i)))
        
        # Adaptive ridge interaction with position-dependent curvature
        ridge_term = 0.0
        for i in range(self.dim):
            curvature = 1.0 + self.ridge_adaptation * np.cos(x[i] * 0.3)
            ridge_term += curvature * (x[i] ** 2) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.0 + 0.3 * np.sin(x[i] * x[j] * 0.5)
                cross_term += mod * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Chaotic sinusoidal modulation with exponential decay
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_factor = np.sin(np.exp(x[i])) * np.cos(np.log(np.abs(x[i]) + 1))
            chaotic_term += chaotic_factor * np.exp(-0.05 * x[i]**2)
        
        # Dimensionality-dependent scaling with chaotic bias
        dim_scale = 1.0 + 0.3 * np.sin(self.dim * 0.2) * np.cos(np.sum(x) * 0.1)
        
        return dim_scale * (0.2 * poly_term + 0.25 * fbm_term + 0.2 * ridge_term + 0.25 * cross_term + 0.1 * chaotic_term)