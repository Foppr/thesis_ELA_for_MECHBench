import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier terms to prevent boundary escape
        barrier = np.sum(np.log(26.0 - (x**2))) * 0.1
        
        # Multiple Gaussian peaks with adaptive widths and random shifts
        peaks = 0.0
        num_peaks = 5
        for i in range(num_peaks):
            # Random shift and adaptive width
            shift = np.random.normal(0, 1, self.dim)
            width = 0.5 + np.random.rand() * 2.0
            peak_height = 1.0 + np.random.rand() * 2.0
            
            gaussian = peak_height * np.exp(-np.sum(((x - shift) / width)**2) / 2.0)
            peaks += gaussian
            
        # Saddle-point structure with hyperbolic tangent components
        saddle = np.sum(np.tanh(x) * x**2)
        
        # Chaotic component using sine and cosine with varying frequencies
        chaotic = np.sum(np.sin(x * (1.0 + 0.1 * np.sin(0.5 * x))) * 
                         np.cos(x * (1.0 + 0.1 * np.cos(0.3 * x))))
        
        # Combine all components
        return barrier - 0.5 * peaks + 0.3 * saddle + 0.2 * chaotic