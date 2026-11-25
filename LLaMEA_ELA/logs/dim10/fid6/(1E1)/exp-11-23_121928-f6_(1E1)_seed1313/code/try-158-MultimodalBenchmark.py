import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos component with mixed degrees
        poly_chaos = np.sum((x_norm**3 + 0.5 * x_norm**4 + 0.2 * x_norm**5) * np.sin(2.0 * np.pi * x_norm))
        
        # Radial basis function inspired landscape with dynamic centers
        rbfs = 0.0
        for i in range(self.dim):
            center = np.sin(0.3 * i * np.pi / self.dim)
            rbfs += np.exp(-10.0 * (x_norm[i] - center)**2) * np.cos(5.0 * np.pi * x_norm[i])
        
        # Dynamic sine-wave interference pattern
        wave_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                wave_interference += np.sin(3.0 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(2.0 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Fractional Brownian motion inspired term with Hurst parameter
        hurst = 0.7
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += np.sin(2.5 * np.pi * x_norm[i]) * (np.abs(x_norm[i])**hurst)
        
        # Adaptive scaling based on dimensionality and input magnitude
        adaptive_scale = 1.0 + 0.5 * np.log(self.dim + 1) + 0.3 * np.mean(np.abs(x_norm))
        
        # Combined function with carefully weighted components
        return adaptive_scale * (0.6 * poly_chaos + 0.3 * rbfs + 0.2 * wave_interference + 0.15 * fbm_term + 0.05 * np.sum(x_norm**6))