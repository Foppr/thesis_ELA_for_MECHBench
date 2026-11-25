import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with non-linear frequency modulation
        chaotic_wave = 0
        for i in range(self.dim):
            freq = 2 + np.sin(x[i]) * (i + 1) * 0.3
            chaotic_wave += np.sin(freq * x[i] + np.cos(x[i] * 0.5)) * np.exp(-0.05 * x[i]**2)
        
        # Radial basis function component with multiple centers
        radial_basis = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            radial_basis += np.exp(-0.5 * ((x[i] - center) / (0.5 + abs(center)))**2)
        
        # Cross-term interaction component
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * (i + j) / (self.dim * (self.dim + 1))
        
        # Polynomial penalty with higher-order terms and mixed signs
        poly_penalty = np.sum((x**5 - 5 * x**3 + 4 * x)**2)
        
        # Combined function with dynamic scaling factors
        return 0.3 * chaotic_wave + 0.4 * radial_basis + 0.2 * cross_term + 0.005 * poly_penalty + 15 * self.dim