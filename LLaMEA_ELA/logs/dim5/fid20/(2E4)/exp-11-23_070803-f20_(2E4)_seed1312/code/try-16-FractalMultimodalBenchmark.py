import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Spherical basin term with exponential decay
        basin_term = np.sum(np.exp(-np.abs(x_norm)) * x_norm**2)
        
        # Trigonometric wave interference pattern with varying frequencies
        wave_term = 0
        for i in range(self.dim):
            wave_term += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) + \
                        np.sin(15 * x_norm[i]**2) * np.cos(12 * x_norm[i]**2) + \
                        np.sin(20 * x_norm[i]**3) * np.cos(18 * x_norm[i]**3)
        
        # Fractal-like interaction terms with recursive frequency components
        fractal_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add complex coupling with exponential scaling
                scale = np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
                fractal_term += scale * np.sin(25 * x_norm[i] * x_norm[j]) * np.cos(20 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Mixed polynomial and exponential components for varied conditioning
        mixed_term = 0
        for i in range(self.dim):
            mixed_term += 0.5 * x_norm[i]**4 + 0.3 * np.exp(-2 * x_norm[i]**2) + 0.2 * np.abs(x_norm[i])
        
        # Combined result with small perturbation for non-determinism
        result = basin_term + wave_term + fractal_term + mixed_term
        
        # Add small random noise to make it non-deterministic
        noise = np.random.normal(0, 0.001)
        
        return result + noise