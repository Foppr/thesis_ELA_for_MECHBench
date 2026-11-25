import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random centers and widths for RBF components
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Normalize to [-1, 1] for stability
        x_norm = x / 5.0
        
        # RBF components with varying widths and centers
        rbf_sum = 0.0
        for i in range(10):
            diff = x_norm - self.centers[i]
            rbf_sum += np.exp(-0.5 * np.sum((diff / self.widths[i])**2))
        
        # Trigonometric modulation with adaptive frequency
        trig_mod = np.sum(np.sin(10 * x_norm * np.cos(3 * x_norm))**3)
        
        # Polynomial conditioning with mixed degrees
        poly_cond = np.sum(x_norm**8 + 0.7 * x_norm**5 - 0.3 * x_norm**3 + 0.1 * x_norm)
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * self.dim
        
        # Combine all components with carefully tuned weights
        return (0.5 * rbf_sum + 
                0.3 * trig_mod + 
                0.2 * poly_cond + 
                0.05 * np.sum(x_norm**6) + 
                0.1 * np.sum(np.abs(x_norm)**1.5)) * scale_factor