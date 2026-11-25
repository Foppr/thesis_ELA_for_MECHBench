import numpy as np

class MultimodalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        rbf_term = 0.0
        for i in range(len(centers)):
            if i < self.dim:
                rbf_term += np.exp(-10 * (x_scaled[i] - centers[i%len(centers)])**2)
        
        # Sinusoidal waves with varying frequencies and amplitudes
        wave_term = np.sum(np.sin(5 * x_scaled) * np.cos(3 * x_scaled) + 
                          0.5 * np.sin(7 * x_scaled) * np.cos(4 * x_scaled))
        
        # Gradient-based attraction term creating valleys and ridges
        grad_attraction = np.sum((x_scaled**2) * np.exp(-0.5 * x_scaled**2))
        
        # Cross-term interactions creating complex coupling between dimensions
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x_scaled[i] * x_scaled[i+1]) * np.sin(x_scaled[i] + x_scaled[i+1])
        
        # Polynomial with mixed powers to introduce non-convexity
        poly_term = np.sum(0.3 * x_scaled**6 + 0.7 * x_scaled**4 + 1.2 * x_scaled**2)
        
        # Combined result with carefully tuned weights
        return 0.2 * rbf_term + 0.3 * wave_term + 0.25 * grad_attraction + 0.15 * cross_term + 0.1 * poly_term + 1.0