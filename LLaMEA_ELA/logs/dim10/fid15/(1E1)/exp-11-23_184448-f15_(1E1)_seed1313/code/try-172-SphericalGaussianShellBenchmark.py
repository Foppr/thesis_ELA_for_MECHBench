import numpy as np

class SphericalGaussianShellBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize input to unit sphere
        norm = np.linalg.norm(x)
        if norm < 1e-12:
            return 0.0
            
        # Scale to spherical shell of radius 3
        scaled_x = x * (3.0 / norm)
        
        # Base quadratic term
        quadratic_term = 0.5 * np.sum(x**2)
        
        # Multi-modal Gaussian peaks on spherical shell
        peak_term = 0.0
        num_peaks = max(1, self.dim // 2)
        
        for i in range(num_peaks):
            # Peak positions distributed on sphere
            peak_radius = 3.0
            peak_angle = 2.0 * np.pi * i / num_peaks
            
            # Create peak center in spherical coordinates
            peak_center = np.zeros(self.dim)
            if self.dim >= 1:
                peak_center[0] = peak_radius * np.cos(peak_angle)
            if self.dim >= 2:
                peak_center[1] = peak_radius * np.sin(peak_angle)
            
            # Add additional dimensions using fibonacci spiral
            for j in range(min(self.dim - 2, num_peaks)):
                angle = 2.0 * np.pi * j / num_peaks
                if j + 2 < self.dim:
                    peak_center[j + 2] = peak_radius * np.sin(angle)
            
            # Gaussian decay with exponential scaling
            dist = np.linalg.norm(scaled_x - peak_center)
            amplitude = np.exp(-0.5 * (i + 1))
            width = 0.5 + 0.5 * np.sin(i * np.pi / (num_peaks + 1))
            
            peak_term += amplitude * np.exp(-0.5 * (dist / width)**2)
        
        # Add correlation between dimensions
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_term += 0.1 * x[i] * x[j] * np.sin(0.5 * (x[i] + x[j]))
        
        # Add sinusoidal modulation
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(x[i]) * np.cos(2 * x[i])
        
        # Combine all terms with dimensionality scaling
        dim_scaling = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return dim_scaling * (quadratic_term + peak_term + corr_term + 0.5 * sin_term)