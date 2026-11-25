import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic tent map parameters
        self.chebyshev_roots = np.cos(np.linspace(0, np.pi, dim) * (dim - 1) / dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for tent map
        scaled_x = x / 5.0
        
        # Chaotic tent map component with varying parameter
        tent_map = 0.0
        a = 1.8
        for i in range(10):  # Iterate tent map 10 times
            tent_map = np.where(scaled_x < 0.5, a * scaled_x, a * (1 - scaled_x))
            scaled_x = tent_map
            
        # Radial basis function component with multiple centers
        rbfs = 0.0
        centers = np.linspace(-1, 1, self.dim)
        for i in range(self.dim):
            rbf = np.exp(-20 * (x - centers[i])**2)
            rbfs += rbf
            
        # Polynomial interaction terms with varying degrees
        poly_interaction = 0.0
        for i in range(self.dim - 1):
            poly_interaction += (x[i]**3) * x[i+1] + x[i] * (x[i+1]**3)
            
        # Sinusoidal modulation based on chaotic sequence
        modulator = np.sin(10 * tent_map)
        sinusoidal_mod = 0.5 * np.sum(modulator * x**2)
        
        # Cross-dimensional exponential interaction
        exp_interaction = 0.0
        for i in range(self.dim - 1):
            exp_interaction += np.exp(-x[i]**2) * x[i+1] + x[i] * np.exp(-x[i+1]**2)
            
        # Chebyshev polynomial component for varied curvature
        chebyshev = 0.0
        for i in range(self.dim):
            chebyshev += np.cos((i + 1) * np.arccos(np.clip(x[i], -1, 1)))
            
        # Fractional power component for non-smooth features
        fractional = 0.05 * np.sum(np.abs(x)**1.7)
        
        # Combined chaotic and RBF landscape
        return (rbfs + poly_interaction + sinusoidal_mod + exp_interaction + 
                chebyshev + fractional + 0.3 * np.sum(tent_map**2))