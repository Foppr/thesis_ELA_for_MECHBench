import numpy as np

class HybridAsymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical component with adaptive radius
        spherical = np.sum(x_norm**2) * (1 + 0.1 * np.sin(self.dim))
        
        # Saddle-like structure with varying curvature
        saddle = np.sum((x_norm**2 - 1)**2 * (1 + 0.3 * np.cos(3 * x_norm)))
        
        # Asymmetric basin structure
        asym_basin = np.sum(np.abs(x_norm)**1.5 * (1 + 0.2 * np.sin(2 * x_norm) * np.cos(2 * x_norm)))
        
        # Noise component with dimension-dependent amplitude
        noise = np.sum(0.05 * np.random.randn(self.dim) * (1 + 0.1 * np.abs(x_norm)))
        
        # Cross-dimensional interaction with asymmetric coupling
        cross_interaction = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * 
                                  (1 + 0.2 * np.sin(2 * x_norm[:-1]) * np.cos(2 * x_norm[1:])))
        
        # Dimension-dependent conditioning
        conditioning = np.sum((1 + 0.5 * np.sin(np.arange(self.dim) * 0.5)) * x_norm**2)
        
        # Peak structure with varying heights
        peaks = np.sum(2.0 * np.exp(-0.5 * (x_norm - 0.5)**2) + 
                      1.5 * np.exp(-0.5 * (x_norm + 0.3)**2) + 
                      1.0 * np.exp(-0.5 * (x_norm - 0.8)**2))
        
        # Combined function with weighted components
        return 0.8 * spherical + 0.6 * saddle + 0.7 * asym_basin + 0.3 * noise + \
               0.9 * cross_interaction + 1.1 * conditioning + 0.5 * peaks