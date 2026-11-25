import numpy as np

class ChaoticTentSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for tent map
        self.chebyshev_roots = np.cos(np.pi * np.arange(1, dim + 1) / (dim + 1))
        # Saddle point intensities
        self.saddle_intensities = np.linspace(1.0, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component
        tent_map = 0.0
        a = 1.5  # Chaotic parameter
        for i in range(self.dim):
            xi = x[i]
            if xi < 0.5:
                tent_map += a * xi
            else:
                tent_map += a * (1 - xi)
                
        # Radial basis function with Gaussian kernels
        rbf_term = 0.0
        for i in range(self.dim):
            center = self.chebyshev_roots[i]
            sigma = 0.5 + 0.5 * np.sin(i)  # Varying widths
            rbf_term += np.exp(-0.5 * ((x[i] - center) / sigma)**2)
            
        # Saddle-point enhanced gradient field
        saddle_term = 0.0
        for i in range(self.dim):
            # Enhanced with sine modulation to create saddle points
            saddle_term += self.saddle_intensities[i] * np.sin(x[i]) * np.cos(2 * x[i])
            
        # Cross-dimensional interaction with cosine coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_term += np.cos(0.3 * x[i] + 0.7 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
            
        # Combine all terms with dynamic weights
        result = 0.3 * tent_map + 0.4 * rbf_term + 0.2 * saddle_term + 0.1 * cross_term
        
        return result