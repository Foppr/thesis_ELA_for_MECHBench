import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos terms with varying exponents and mixed interactions
        f1 = np.sum(0.5 * x_norm**8 + 0.3 * x_norm**6 + 0.2 * x_norm**4)
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-1, 1, 5)
        rb_f = np.zeros_like(x_norm)
        for c in centers:
            rb_f += np.exp(-5 * (x_norm - c)**2) * np.sin(3 * np.pi * (x_norm - c))
        
        # Competitive sine waves with varying amplitudes and frequencies
        f2 = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) + 
                   0.8 * np.sin(13 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm))
        
        # Cross-terms creating complex interaction between dimensions
        f3 = np.sum((x_norm[:-1] - x_norm[1:])**4 + 0.5 * (x_norm[:-1] + x_norm[1:])**2)
        
        # Combined function with competing forces and multiple local optima
        return 0.3 * f1 + 0.4 * rb_f + 0.2 * f2 + 0.1 * f3