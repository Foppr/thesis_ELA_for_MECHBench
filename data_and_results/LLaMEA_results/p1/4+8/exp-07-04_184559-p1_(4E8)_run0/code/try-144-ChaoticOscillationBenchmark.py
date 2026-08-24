import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic phase parameters
        self.chaotic_params = np.random.uniform(0.5, 2.0, dim)
        self.oscillation_frequencies = np.linspace(1, 3, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with chaotic modulation
        oscillation = np.sum(np.sin(self.oscillation_frequencies * x_norm) * 
                           np.exp(-0.5 * self.chaotic_params * x_norm**2))
        
        # Radial basis function with chaotic center distribution
        centers = np.sin(np.linspace(0, 4*np.pi, self.dim)) * 0.5
        rbf = np.sum(np.exp(-3 * (x_norm - centers)**2) * 
                    (1 + 0.4 * np.cos(5 * x_norm)))
        
        # Polynomial chaos term with cross-terms
        poly_chaos = np.sum(x_norm**4 + 0.3 * x_norm**3 - 0.2 * x_norm**2 + 0.1 * x_norm)
        
        # Cross-dimensional interaction with chaotic coupling
        cross_interaction = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * 
                                 np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive conditioning with chaotic scaling
        adaptive_cond = 1 + 0.5 * np.sin(2 * x_norm) + 0.2 * np.cos(3 * x_norm)
        conditioning = np.sum(adaptive_cond * x_norm**3)
        
        # Combined objective with dynamic weighting
        return 1.5 * oscillation + 1.2 * rbf + 0.8 * poly_chaos + 0.6 * cross_interaction + 1.0 * conditioning