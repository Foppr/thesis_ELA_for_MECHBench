import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute centers for radial basis functions
        self.centers = np.random.uniform(-3.0, 3.0, (10, dim))
        
    def f(self, x):
        x = np.array(x)
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Gaussian radial basis functions with varying widths
        rbf_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            sigma = 0.5 + 0.5 * np.random.random()
            rbf_sum += np.exp(-np.sum(((x_norm - center) / sigma) ** 2))
        
        # Fractional polynomial interactions with non-integer exponents
        poly_frac = 0.0
        for i in range(self.dim - 1):
            poly_frac += (x_norm[i] ** 1.5) * (x_norm[i + 1] ** 2.5)
            
        # Sine-wave modulation with varying frequencies
        sine_mod = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Cross-dimensional coupling with asymmetric weights
        cross_coupling = 0.0
        for i in range(self.dim - 2):
            cross_coupling += (x_norm[i] ** 2) * (x_norm[i + 1] ** 1.3) * (x_norm[i + 2] ** 0.7)
            
        # Add noise for robustness
        noise = np.random.normal(0, 0.01, self.dim)
        
        return rbf_sum + poly_frac + sine_mod + cross_coupling + np.sum(noise)