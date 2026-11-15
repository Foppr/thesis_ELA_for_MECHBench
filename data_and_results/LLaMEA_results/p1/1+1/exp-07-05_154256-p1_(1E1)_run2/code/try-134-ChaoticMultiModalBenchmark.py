import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.a = 1.0
        self.b = 2.0
        self.c = 0.5
        self.d = 3.0
        self.e = 0.8
        self.f = 1.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component
        r = np.sqrt(np.sum(x**2))
        radial_poly = self.a * r**2 + self.b * r**4 + self.c * r**6
        
        # Sinusoidal oscillations in each dimension
        sin_component = 0
        for i in range(self.dim):
            sin_component += np.sin(self.d * x[i]) * np.cos(self.e * x[i]) + np.sin(self.f * x[i]**2)
        
        # Chaotic cross-terms between dimensions
        chaotic_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_cross += np.sin(self.f * x[i] * x[j]) * np.cos(self.f * x[i] * x[j] * 0.3) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Additional multi-scale polynomial interaction
        poly_interaction = 0
        for i in range(self.dim):
            poly_interaction += (x[i]**3 + x[i]**5) * np.sin(2 * x[i]) + 0.1 * x[i]**7
        
        # Combined landscape with exponential modulation
        result = radial_poly + 2.5 * sin_component + 1.2 * chaotic_cross + 0.8 * poly_interaction
        
        # Add a global scaling factor based on dimensionality
        result *= (1.0 + 0.1 * self.dim)
        
        return result