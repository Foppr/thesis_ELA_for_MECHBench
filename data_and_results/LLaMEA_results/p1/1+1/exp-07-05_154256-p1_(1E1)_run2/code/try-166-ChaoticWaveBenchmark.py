import numpy as np

class ChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 2.0
        self.c2 = 3.0
        self.c3 = 0.5
        self.c4 = 1.5
        self.chaos_factor = 4.1
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component
        r = np.sqrt(np.sum(x**2))
        radial_poly = self.c1 * r**2 + self.c2 * r**4 + self.c3 * r**6
        
        # Sinusoidal wave component with varying frequencies
        wave = 0
        for i in range(self.dim):
            wave += np.sin(self.chaos_factor * x[i]) * np.cos(self.chaos_factor * x[i] * 0.7) + \
                    np.sin(self.chaos_factor * x[i] * 1.3) * np.cos(self.chaos_factor * x[i] * 0.4)
        
        # Chaotic cross-term interactions
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(self.chaos_factor * x[i] * x[j]) * np.cos(self.chaos_factor * x[i] * x[j] * 0.3) + \
                         np.sin(self.chaos_factor * x[i] * x[j] * 0.8) * np.cos(self.chaos_factor * x[i] * x[j] * 0.6)
        
        # Additional radial cosine component
        radial_cos = self.c4 * np.cos(self.chaos_factor * r)
        
        # Polynomial interaction terms
        poly_interaction = 0
        for i in range(self.dim):
            poly_interaction += x[i]**3 + x[i]**5 + x[i]**7
        
        # Combine all components
        return radial_poly + wave + cross + radial_cos + poly_interaction