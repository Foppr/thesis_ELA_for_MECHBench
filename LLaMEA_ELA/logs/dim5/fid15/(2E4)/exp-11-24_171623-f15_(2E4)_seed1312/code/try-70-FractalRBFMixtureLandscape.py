import numpy as np

class FractalRBFMixtureLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors with more varied spacing
        self.fractal_factors = [np.sqrt(i + 1) * np.sin(i * 0.5) for i in range(dim)]
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced Radial Basis Function components with dynamic widths and heights
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(15, self.dim))
        for i in range(min(15, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.3 / (i + 1) ** 0.7
            height = 1.5 / (i + 1)**1.2
            distance = np.sum((x_norm - center)**2)
            rbf_sum += height * np.exp(-distance / (2 * width**2))
        
        # Modified fractal-like curvature with asymmetric scaling
        fractal_curvature = 0.0
        for i in range(self.dim):
            scaled_x = x_norm[i] * self.fractal_factors[i % len(self.fractal_factors)]
            fractal_curvature += np.sin(scaled_x**4) * np.cos(scaled_x**3) * (1 + 0.5 * np.sin(i))
        
        # Enhanced asymmetric saddle points with non-linear coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling
                diff = x_norm[i] - x_norm[j]
                saddle += (diff**3) * np.exp(-abs(diff)) * (i + j) / (self.dim + 2)
        
        # Improved peak attraction regions with directional bias
        peak_attraction = 0.0
        for i in range(self.dim):
            # Create asymmetric peaks with directional preference
            peak_pos = np.sin(i * np.pi / self.dim) * 0.4 + 0.1 * np.cos(i)
            dist_from_peak = abs(x_norm[i] - peak_pos)
            peak_attraction += np.exp(-dist_from_peak**2 * 3) * (1 + 0.5 * np.sin(i) * np.cos(i))
        
        # Enhanced cross-dimensional interaction with multi-scale coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-scale polynomial coupling
                cross_interaction += (x_norm[i]**3 + x_norm[j]**3) * \
                                   np.sin(x_norm[i] * x_norm[j]) * \
                                   (i + j) / (self.dim**1.5)
        
        # Combine all terms with adjusted weights for better balance
        result = 0.25 * rbf_sum + 0.2 * fractal_curvature + 0.25 * saddle + \
                 0.15 * peak_attraction + 0.15 * cross_interaction
        
        # Enhanced conditioning through mixed polynomial terms
        conditioning = 0.03 * np.sum(np.abs(x_norm)**4) + 0.02 * np.sum(x_norm**2)
        
        return result + conditioning