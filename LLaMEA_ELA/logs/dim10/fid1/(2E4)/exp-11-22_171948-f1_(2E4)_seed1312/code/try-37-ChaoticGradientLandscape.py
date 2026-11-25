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
            # Modified harmonic terms with different frequencies and amplitudes
            chaos_term = np.exp(-0.1 * x[i]**2) * (np.sin(15 * x[i]) + 
                                                  0.6 * np.sin(45 * x[i]) + 
                                                  0.2 * np.sin(100 * x[i]))
            result += chaos_term**2
        
        # Cross-dimensional interference with modified coupling
        for i in range(self.dim - 1):
            # Changed coupling strength and interaction type
            coupling_strength = 1.0 / (1.0 + np.exp(-0.3 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.cos(7 * (x[i] + x[i+1])) * np.sin(4 * (x[i] - x[i+1]))
            result += 0.6 * interference
        
        # Modified ridge structure with different orientations
        for i in range(self.dim):
            # Changed ridge configuration with new sinusoidal components
            ridge = (np.cos(25 * x[i]) + 
                    0.4 * np.cos(50 * x[i]) + 
                    0.1 * np.cos(100 * x[i]))
            result += 0.4 * ridge**2
        
        # Saddle point configuration with modified curvature
        for i in range(self.dim):
            # Adjusted saddle behavior
            if i < self.dim - 1:
                saddle = (x[i]**2 - x[i+1]**2) * np.exp(-0.03 * (x[i]**2 + x[i+1]**2))
                result += 0.5 * saddle
        
        # Modified multi-scale periodic modulation
        for i in range(self.dim):
            # Changed modulation with different frequency progression
            modulated = np.cos(2 * np.pi * x[i] * (1 + 0.3 * np.cos(x[i]))) * np.exp(-0.01 * x[i]**2)
            result += 0.7 * modulated**3
        
        # Adaptive conditioning with modified factor
        conditioning_factor = 1.0 + 0.4 * np.tanh(np.sum(x) / self.dim)
        result *= conditioning_factor
        
        # Added perturbations with different frequencies
        noise = 0.0
        for i in range(self.dim):
            noise += np.cos(15 * x[i] + i * 0.15) * np.sin(8 * x[i] + i * 0.25)
        result += 0.25 * noise
        
        # Normalize by dimension
        result /= self.dim
        
        return result