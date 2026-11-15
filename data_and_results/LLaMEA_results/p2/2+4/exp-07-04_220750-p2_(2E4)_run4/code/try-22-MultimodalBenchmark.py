import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of squares term
        sum_squares = np.sum(x_norm**2)
        
        # Exponentially weighted product of cosines with varying frequencies
        freqs = np.arange(1, self.dim + 1)
        product_term = np.prod(np.cos(freqs * x_norm))
        
        # Chaotic sine-wave interaction term with enhanced nonlinearity
        chaotic_term = np.sum(np.sin(np.exp(x_norm * np.sin(x_norm)) * np.pi))
        
        # Polynomial interaction with mixed exponents and cross-terms
        poly_term = np.sum(x_norm**3 + 0.5 * x_norm**5 + 0.1 * np.sum(x_norm[:, None] * x_norm[None, :], axis=0))
        
        # Additional high-frequency oscillation with dynamic modulation
        high_freq = np.sum(np.sin(15 * x_norm**2 + 5 * np.sin(x_norm)))
        
        # Novel frequency modulation term
        freq_mod = np.sum(np.sin(freqs * x_norm * np.cos(x_norm)))
        
        # Additional multimodal component with Gaussian peaks
        gaussian_peaks = np.sum(np.exp(-5 * (x_norm - 0.5)**2) + np.exp(-5 * (x_norm + 0.5)**2))
        
        # Combine all terms with varying weights to create complex landscape
        return sum_squares + 0.3 * product_term + 0.1 * chaotic_term + 0.05 * poly_term + 0.15 * high_freq + 0.08 * freq_mod + 0.03 * gaussian_peaks