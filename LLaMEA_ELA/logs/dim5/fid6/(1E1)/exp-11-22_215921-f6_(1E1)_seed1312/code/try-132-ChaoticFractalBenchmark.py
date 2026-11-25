import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map seeds for chaos generation
        self.seeds = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component with dynamic parameter
        chaos = 0.0
        r = 3.99  # High chaos parameter
        for i in range(self.dim):
            if i == 0:
                logistic_val = self.seeds[i]
            else:
                logistic_val = self.seeds[i-1]
            chaos += np.log(1 + np.abs(logistic_val * (1 - logistic_val) * r))
        
        # Fractal Brownian motion component with Hurst parameter
        fbm = 0.0
        hurst = 0.3  # Sub-diffusive fractal
        for i in range(self.dim):
            # Simple fractal-like term using sinusoids and powers
            fbm += np.sin(x_norm[i] ** (2 * hurst)) * np.cos(x_norm[i] ** (1 + hurst))
        
        # Adaptive gradient field with directional coupling
        grad_field = 0.0
        for i in range(self.dim - 1):
            dx = x_norm[i+1] - x_norm[i]
            dy = x_norm[i] - x_norm[i+1]
            grad_field += (dx**2 + dy**2) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Multi-scale sinusoidal modulation with varying frequencies
        multi_freq = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4)  # Frequencies: 1, 2, 4, 8
            multi_freq += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Asymmetric saddle with hyperbolic cosine interactions
        saddle = 0.0
        for i in range(self.dim - 1):
            saddle += np.cosh(x_norm[i] + x_norm[i+1]) - 2.0
        
        # Dimension-dependent conditioning factor
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combine all terms with appropriate weights
        return condition_factor * (0.5 * chaos + 0.3 * fbm + 0.4 * grad_field + 
                                 0.6 * multi_freq + 0.7 * saddle)