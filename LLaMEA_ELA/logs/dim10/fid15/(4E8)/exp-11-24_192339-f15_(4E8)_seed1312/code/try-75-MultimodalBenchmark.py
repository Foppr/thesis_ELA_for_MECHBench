import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic spiral component for irregular gradient directions
        spiral = 0
        for i in range(self.dim):
            r = np.sqrt(x[i]**2 + 1e-8)
            angle = np.arctan2(x[i], 1.0) if i == 0 else np.arctan2(x[i], x[i-1]) if i > 0 else 0
            spiral += r * np.sin(3 * angle + 0.5 * i) ** 2
        
        # Trigonometric coupling with varying frequencies and amplitudes
        trig_coupling = 0
        for i in range(self.dim):
            freq = 2.0 * (i + 1) / self.dim
            trig_coupling += np.sin(freq * x[i]) * np.cos(freq * x[i] ** 2)
        
        # Polynomial cross-terms with dynamic exponents
        poly_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_i = 1.5 + 0.5 * np.sin(i / self.dim * np.pi)
                exp_j = 1.5 + 0.5 * np.cos(j / self.dim * np.pi)
                poly_cross += (x[i] ** exp_i) * (x[j] ** exp_j)
        
        # Adaptive noise component based on spatial density
        noise = 0
        for i in range(self.dim):
            noise += 0.3 * np.sin(x[i] * 10) * np.exp(-0.1 * np.sum((x - x[i])**2))
        
        # Combined function with dimensionality scaling
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        return scale_factor * (0.2 * spiral + 0.3 * trig_coupling + 0.1 * poly_cross) + noise