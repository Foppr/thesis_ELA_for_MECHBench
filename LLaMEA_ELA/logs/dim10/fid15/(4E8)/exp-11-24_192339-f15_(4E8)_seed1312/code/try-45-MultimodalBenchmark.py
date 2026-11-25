import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_term = np.sum(x_normalized**2)
        
        # Multiple sinusoidal modulations with varying frequencies and amplitudes
        freq1 = 2 * np.pi
        freq2 = 5 * np.pi
        freq3 = 8 * np.pi
        freq4 = 12 * np.pi
        
        sin_term1 = np.sum(np.sin(freq1 * x_normalized)**3)
        sin_term2 = np.sum(np.sin(freq2 * x_normalized)**4)
        sin_term3 = np.sum(np.sin(freq3 * x_normalized)**2)
        sin_term4 = np.sum(np.sin(freq4 * x_normalized)**5)
        
        # Cosine modulation for additional complexity
        cos_term = np.sum(np.cos(3 * np.pi * x_normalized) * np.sin(7 * np.pi * x_normalized))
        
        # Exponential decay terms to create varied landscape curvature
        exp_term1 = np.sum(np.exp(-x_normalized**2) - 1.0)
        exp_term2 = np.sum(np.exp(-2 * x_normalized**2) - 1.0)
        exp_term3 = np.sum(np.exp(-0.5 * x_normalized**2) - 1.0)
        
        # Additional polynomial interaction term for increased complexity
        poly_interaction = np.sum((x_normalized**3) * np.sin(4 * np.pi * x_normalized))
        
        # Novel interaction term: product of sinusoidal and exponential components
        novel_interaction = np.sum(np.sin(6 * np.pi * x_normalized) * np.exp(-0.5 * x_normalized**2))
        
        # Additional cross-term interaction for increased complexity
        cross_term = np.sum(x_normalized * np.cos(9 * np.pi * x_normalized))
        
        # Radial basis function component for multi-modal structure
        rbf_term = np.sum(np.exp(-np.sum((x_normalized[:, None] - x_normalized[None, :])**2, axis=2)) / (2 * 0.5**2))
        
        # Adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim)
        
        # Combine all terms with carefully tuned weights
        return adaptive_scale * (quadratic_term + 
                               0.4 * sin_term1 + 
                               0.3 * sin_term2 + 
                               0.2 * sin_term3 + 
                               0.15 * sin_term4 + 
                               0.08 * cos_term + 
                               0.12 * exp_term1 + 
                               0.1 * exp_term2 + 
                               0.08 * exp_term3 + 
                               0.03 * poly_interaction + 
                               0.04 * novel_interaction + 
                               0.05 * cross_term + 
                               0.02 * rbf_term)