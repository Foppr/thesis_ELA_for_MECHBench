import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion with Hermite polynomials
        poly_chaos = np.sum(x_norm**2 + 0.5 * x_norm**4 + 0.1 * x_norm**6)
        
        # Fractal-like sinusoidal components with varying frequencies and amplitudes
        fractal_sin = 0.0
        for i in range(self.dim):
            for j in range(1, 6):
                fractal_sin += (0.1 / j) * np.sin(j**2 * x_norm[i]) * np.cos(j**1.5 * x_norm[i])
        
        # Multi-scale interaction terms with exponential decay
        multi_scale = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multi_scale += np.exp(-10 * (x_norm[i] - x_norm[j])**2) * np.sin(50 * (x_norm[i] + x_norm[j]))
        
        # Coupled oscillatory components with phase shifts
        oscillatory = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                oscillatory += np.sin(20 * x_norm[i] + 0.5 * np.pi) * np.cos(15 * x_norm[i+1] + 0.3 * np.pi) + \
                              0.3 * np.cos(25 * x_norm[i] + 0.7 * np.pi) * np.sin(18 * x_norm[i+1] + 0.9 * np.pi)
        
        # Fractional Brownian motion inspired term with Hurst parameter
        fbm_term = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                fbm_term += (x_norm[i]**1.3 + x_norm[i+1]**1.7) * np.sin(30 * x_norm[i] * x_norm[i+1])
        
        # Non-separable high-order polynomial with cross-terms
        high_order = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                high_order += x_norm[i]**3 * x_norm[i+1]**2 * x_norm[i+2]**1.5 + \
                             0.5 * x_norm[i]**2 * x_norm[i+1]**3 * x_norm[i+2]**2
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.25 * poly_chaos + 
                0.2 * fractal_sin + 
                0.15 * multi_scale + 
                0.15 * oscillatory + 
                0.1 * fbm_term + 
                0.1 * high_order + 
                noise)