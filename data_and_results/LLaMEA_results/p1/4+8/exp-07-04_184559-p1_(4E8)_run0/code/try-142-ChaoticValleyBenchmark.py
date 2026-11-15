import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for varying landscape characteristics
        self.chaotic_seq = np.sin(np.arange(dim) * np.pi / 4.0)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic center placement
        centers = np.sin(np.arange(self.dim) * self.chaotic_seq[0])
        rbf = np.sum(np.exp(-10 * (x_norm - centers)**2))
        
        # Sinusoidal modulation creating complex valley structures
        sin_mod = np.sum(np.sin(5 * x_norm + self.chaotic_seq) * 
                        np.cos(3 * x_norm + self.chaotic_seq))
        
        # Polynomial term with chaotic coefficient variation
        poly_coeffs = 1 + 0.5 * np.sin(np.arange(self.dim) * self.chaotic_seq[1])
        poly_term = np.sum((x_norm * poly_coeffs)**3)
        
        # Cross-term creating rugged terrain with chaotic coupling
        cross_term = np.sum(np.sin(2 * (x_norm[:-1] + x_norm[1:])) * 
                           np.cos(4 * (x_norm[:-1] - x_norm[1:])) * 
                           np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive conditioning based on chaotic input scaling
        adapt_cond = 1 + 0.3 * np.sin(np.sum(x_norm) * self.chaotic_seq[2])
        cond_term = np.sum(adapt_cond * x_norm**6)
        
        # Chaotic phase shift creating non-uniform landscape topology
        phase_shift = np.sin(np.sum(x_norm) * self.chaotic_seq[3])
        phase_term = np.sum(np.exp(-0.5 * (x_norm - phase_shift)**2) * 
                           np.cos(7 * x_norm + phase_shift))
        
        # Combine all components with varying weights
        return 1.2 * rbf + 0.9 * sin_mod + 1.1 * poly_term + 0.7 * cross_term + 1.3 * cond_term + 0.8 * phase_term