import numpy as np

class FractalRBFMixtureLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.fractal_factors = [np.sqrt(i + 1) for i in range(dim)]
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial Basis Function components with varying widths and heights
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.5 / (i + 1)
            height = 1.0 / (i + 1)**1.5
            distance = np.sum((x_norm - center)**2)
            rbf_sum += height * np.exp(-distance / (2 * width**2))
        
        # Fractal-like curvature with dimension-dependent scaling
        fractal_curvature = 0.0
        for i in range(self.dim):
            scaled_x = x_norm[i] * self.fractal_factors[i % len(self.fractal_factors)]
            fractal_curvature += np.sin(scaled_x**3) * np.cos(scaled_x**2)
        
        # Asymmetric saddle points with varying steepness
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                diff = x_norm[i] - x_norm[j]
                saddle += diff**2 * np.exp(-abs(diff)) * (i + j) / (self.dim + 1)
        
        # Peak attraction regions with non-uniform distribution
        peak_attraction = 0.0
        for i in range(self.dim):
            # Create asymmetric peaks
            peak_pos = np.sin(i * np.pi / self.dim) * 0.5
            dist_from_peak = abs(x_norm[i] - peak_pos)
            peak_attraction += np.exp(-dist_from_peak**2 * 2) * (1 + np.sin(i))
        
        # Cross-dimensional interaction with polynomial coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**2 + x_norm[j]**2) * \
                                   np.sin(x_norm[i] * x_norm[j]) * \
                                   (i + j) / (self.dim**2)
        
        # Combine all terms with dynamic weights
        result = 0.25 * rbf_sum + 0.3 * fractal_curvature + 0.15 * saddle + \
                 0.2 * peak_attraction + 0.1 * cross_interaction
        
        # Add conditioning through higher-order polynomial terms
        conditioning = 0.03 * np.sum(np.abs(x_norm)**4)
        
        return result + conditioning