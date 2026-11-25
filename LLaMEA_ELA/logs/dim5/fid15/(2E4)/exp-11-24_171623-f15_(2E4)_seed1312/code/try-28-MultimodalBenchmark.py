import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with radial and angular components
        exp_term = np.exp(-0.3 * np.sum(x_norm**2, axis=0)) * (1.0 + 0.3 * np.cos(2 * np.sum(x_norm, axis=0)))
        
        # Modified trigonometric wave with multiple frequencies and interaction terms
        wave_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * 
                          np.exp(-0.2 * np.sum(x_norm**2, axis=0)))
        
        # Improved spherical harmonic-like interaction with higher frequency components
        if self.dim > 1:
            r = np.sqrt(np.sum(x_norm**2, axis=0))
            theta = np.arctan2(x_norm[1], x_norm[0])
            sph_harm_term = np.sin(5 * r) * np.cos(3 * theta) + 0.5 * np.sin(7 * r) * np.sin(4 * theta)
        else:
            sph_harm_term = np.sin(5 * np.abs(x_norm[0]))
        
        # Enhanced cross-dimensional interaction with multiple Gaussian peaks
        peak_term = 0
        if self.dim > 1:
            for i in range(min(3, self.dim)):
                for j in range(i+1, min(4, self.dim)):
                    peak_term += np.exp(-0.5 * ((x_norm[i] - 0.5)**2 + (x_norm[j] + 0.3)**2)) * \
                                np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[j])
        
        # Modified polynomial interaction with higher-order terms
        poly_interaction = 0
        if self.dim > 1:
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    poly_interaction += (x_norm[i] + x_norm[j])**3 + (x_norm[i] - x_norm[j])**2
        
        # Combine all terms with optimized weights
        result = 0.4 * exp_term + 0.25 * wave_term + 0.2 * sph_harm_term + 0.1 * peak_term + 0.05 * poly_interaction
        
        return result