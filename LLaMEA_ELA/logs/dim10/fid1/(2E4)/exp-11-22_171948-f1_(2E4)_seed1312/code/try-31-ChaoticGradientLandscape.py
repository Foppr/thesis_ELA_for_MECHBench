import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic gradient component with exponential decay
        for i in range(self.dim):
            # Exponentially decaying harmonic terms with chaotic phase shifts
            chaos_term = np.exp(-0.1 * x[i]**2) * (np.sin(10 * x[i]) + 
                                                  0.7 * np.sin(30 * x[i]) + 
                                                  0.3 * np.sin(90 * x[i]))
            result += chaos_term**2
        
        # Cross-dimensional interference with adaptive coupling
        for i in range(self.dim - 1):
            # Adaptive coupling strength based on distance between variables
            coupling_strength = 1.0 / (1.0 + np.exp(-0.5 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(5 * (x[i] + x[i+1])) * np.cos(3 * (x[i] - x[i+1]))
            result += 0.5 * interference
        
        # Sharp ridge structure with multiple local minima
        for i in range(self.dim):
            # Multiple overlapping quadratic ridges with different orientations
            ridge = (np.sin(20 * x[i]) + 
                    0.5 * np.sin(40 * x[i]) + 
                    0.2 * np.sin(80 * x[i]))
            result += 0.3 * ridge**2
        
        # Saddle point configuration with varying curvature
        for i in range(self.dim):
            # Adaptive saddle behavior based on neighboring dimensions
            if i < self.dim - 1:
                saddle = (x[i]**2 - x[i+1]**2) * np.exp(-0.05 * (x[i]**2 + x[i+1]**2))
                result += 0.4 * saddle
        
        # Multi-scale periodic modulation with varying amplitudes
        for i in range(self.dim):
            # Periodic modulation with exponentially increasing frequency
            modulated = np.sin(2 * np.pi * x[i] * (1 + 0.5 * np.sin(x[i]))) * np.exp(-0.02 * x[i]**2)
            result += 0.6 * modulated**3
        
        # Adaptive conditioning based on position
        conditioning_factor = 1.0 + 0.3 * np.tanh(np.sum(x) / self.dim)
        result *= conditioning_factor
        
        # Add noise-like perturbations for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(13 * x[i] + i * 0.1) * np.cos(7 * x[i] + i * 0.2)
        result += 0.2 * noise
        
        # Normalize by dimension
        result /= self.dim
        
        return result