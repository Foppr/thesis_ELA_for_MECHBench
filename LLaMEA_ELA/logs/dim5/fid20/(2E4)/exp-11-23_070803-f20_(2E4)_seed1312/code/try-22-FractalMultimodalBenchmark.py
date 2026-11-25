import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Spherical basin term with modified exponential decay
        basin_term = np.sum(np.exp(-0.7 * np.abs(x_norm)) * x_norm**2)
        
        # Trigonometric wave interference pattern with altered frequencies
        wave_term = 0
        for i in range(self.dim):
            wave_term += 1.5 * np.sin(12 * x_norm[i]) * np.cos(9 * x_norm[i]) + \
                        0.8 * np.sin(18 * x_norm[i]**2) * np.cos(15 * x_norm[i]**2) + \
                        1.2 * np.sin(25 * x_norm[i]**3) * np.cos(22 * x_norm[i]**3)
        
        # Fractal-like interaction terms with enhanced coupling
        fractal_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add stronger coupling with modified exponential scaling
                scale = np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2))
                fractal_term += scale * np.sin(30 * x_norm[i] * x_norm[j]) * np.cos(25 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Mixed polynomial and exponential components with increased nonlinearity
        mixed_term = 0
        for i in range(self.dim):
            mixed_term += 0.7 * x_norm[i]**4 + 0.4 * np.exp(-3 * x_norm[i]**2) + 0.3 * np.abs(x_norm[i])
        
        # Combined result with small perturbation for non-determinism
        result = basin_term + wave_term + fractal_term + mixed_term
        
        # Add small random noise to make it non-deterministic
        noise = np.random.normal(0, 0.001)
        
        return result + noise