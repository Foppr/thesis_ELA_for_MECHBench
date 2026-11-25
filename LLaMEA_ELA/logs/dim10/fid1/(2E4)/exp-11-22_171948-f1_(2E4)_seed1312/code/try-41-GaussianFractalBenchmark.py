import numpy as np

class GaussianFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random centers for Gaussian components
        self.centers = np.random.uniform(-3.0, 3.0, (10, dim))
        # Fractal parameters
        self.hurst = 0.3 + 0.4 * np.random.rand()
        self.fractal_scale = 1.0 + 0.5 * np.random.rand()
        # Penalty weights
        self.penalty_weights = np.random.rand(dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture component
        gaussian_sum = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            distance_sq = np.sum(diff**2)
            gaussian_sum += np.exp(-0.5 * distance_sq) / (1.0 + distance_sq)
        
        # Fractal Brownian motion component
        fbm_term = 0.0
        for i in range(self.dim):
            # Simple fractal-like scaling with Hurst parameter
            scale = self.fractal_scale * (i + 1)**(-self.hurst)
            fbm_term += scale * np.sin(2 * np.pi * x[i] / (1.0 + np.abs(x[i])))
        
        # Adaptive penalty based on distance from origin
        penalty = 0.0
        dist_from_origin = np.linalg.norm(x)
        for i in range(self.dim):
            penalty += self.penalty_weights[i] * (dist_from_origin - 3.0)**2
        
        # Cross-dimension coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * np.sin(5 * (x[i] - x[i+1]))
        
        # Multi-scale sinusoidal modulation
        modulation = 0.0
        for i in range(self.dim):
            modulation += np.sin(10 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Final combined function
        result = 0.5 * gaussian_sum + 0.3 * fbm_term + 0.2 * coupling + 0.1 * modulation + 0.4 * penalty
        
        # Normalize and return
        return result / self.dim