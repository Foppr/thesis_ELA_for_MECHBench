import numpy as np

class AdaptiveRadialSinusoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scaling factors based on dimension
        self.scaling_factors = np.array([1.0 + 0.1 * i for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with adaptive scaling
        for i in range(self.dim):
            result += 0.5 * (x[i] ** 4) * self.scaling_factors[i]
            
        # Sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 2.0 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * (1.0 + 0.2 * np.sin(0.5 * x[i]))
            
        # Radial basis function components with adaptive centers and widths
        for i in range(self.dim):
            center = 2.0 * np.sin(0.7 * i)
            width = 0.5 + 0.3 * np.cos(0.4 * i)
            result += 1.5 * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
            
        # Cross-dimensional coupling with exponential interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                result += 0.8 * np.exp(-dist) * np.sin(4.0 * (x[i] + x[j]))
                
        # Asymmetric terms with threshold-based modifications
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.3 * x[i]**2.5 * np.exp(-0.1 * x[i])
            else:
                result += 0.6 * x[i]**3.2 * np.exp(-0.2 * np.abs(x[i]))
                
        # High-frequency noise component
        for i in range(self.dim):
            result += 0.1 * np.sin(25.0 * x[i]) * np.cos(13.0 * x[i])
            
        # Adaptive dimensionality penalty
        result += 0.05 * np.sum(self.scaling_factors)
        
        return result