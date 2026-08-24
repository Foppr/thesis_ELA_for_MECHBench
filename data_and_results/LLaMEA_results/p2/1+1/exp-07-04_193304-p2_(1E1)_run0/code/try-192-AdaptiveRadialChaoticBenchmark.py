import numpy as np

class AdaptiveRadialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for radial basis functions
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial terms with adaptive exponents
        poly_term = np.sum((x_norm**2 + 0.3 * x_norm**3 + 0.05 * x_norm**4))
        
        # Trigonometric components with varying frequencies
        trig_term = np.sum(np.sin(2 * np.pi * x_norm) + 0.5 * np.cos(3 * np.pi * x_norm))
        
        # Radial basis function components
        rbf_sum = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            rbf_sum += np.exp(-np.sum(((x_norm - center) / width)**2))
        
        # Chaotic sine-cosine interaction
        chaotic_term = np.sum(np.sin(x_norm * np.cos(x_norm * 1.5)) * np.cos(x_norm * np.sin(x_norm * 0.8)))
        
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Localized valleys with Gaussian peaks
        valley_term = 0.0
        for i in range(5):
            peak_x = np.random.uniform(-1.0, 1.0, self.dim)
            peak_val = np.exp(-np.sum(((x_norm - peak_x) / 0.3)**2))
            valley_term += peak_val
        
        # Cross-dimensional coupling with power-law interactions
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += (x_norm[i] * x_norm[i+1])**1.5
        
        # Asymmetric penalty for large values
        penalty = np.sum(0.2 * np.abs(x_norm)**3.5 * (x_norm > 0) + 0.1 * np.abs(x_norm)**2.5 * (x_norm < 0))
        
        # Final combined function
        return cond_factor * (poly_term + trig_term + rbf_sum + chaotic_term + valley_term + coupling_term + penalty)