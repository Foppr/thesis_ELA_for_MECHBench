import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic gradient component with modified harmonic content
        for i in range(self.dim):
            # Modified multi-frequency chaotic terms with altered amplitudes and phases
            chaos_term = (np.exp(-0.1 * x[i]**2) * 
                         (np.sin(18 * x[i]) + 
                          0.5 * np.sin(54 * x[i]) + 
                          0.25 * np.sin(162 * x[i]) + 
                          0.08 * np.sin(324 * x[i])))
            result += chaos_term**2
        
        # Modified cross-dimensional interference with altered coupling
        for i in range(self.dim - 1):
            # Altered non-linear coupling strength based on variable interactions
            coupling_strength = 1.0 / (1.0 + np.exp(-0.4 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(9 * (x[i] + x[i+1])) * np.cos(5 * (x[i] - x[i+1]))
            result += 0.7 * interference
        
        # Enhanced ridge structure with sharper curvature
        for i in range(self.dim):
            # Modified quadratic ridges with more pronounced peaks and valleys
            ridge = (np.sin(30 * x[i]) + 
                    0.5 * np.sin(60 * x[i]) + 
                    0.25 * np.sin(120 * x[i]) + 
                    0.08 * np.sin(240 * x[i]))
            result += 0.5 * ridge**2
        
        # Improved saddle point configuration with stronger curvature variation
        for i in range(self.dim):
            # Enhanced saddle behavior with more pronounced directional differences
            if i < self.dim - 1:
                saddle = (x[i]**3 - x[i+1]**3) * np.exp(-0.04 * (x[i]**2 + x[i+1]**2))
                result += 0.6 * saddle
        
        # Modified multi-scale modulation with altered frequency progression
        for i in range(self.dim):
            # Advanced periodic modulation with varying frequency and amplitude
            modulated = np.sin(2 * np.pi * x[i] * (1 + 0.8 * np.sin(x[i]**2))) * np.exp(-0.015 * x[i]**2)
            result += 0.8 * modulated**3
        
        # Refined adaptive conditioning based on position and dimensionality
        conditioning_factor = 1.0 + 0.5 * np.tanh(np.sum(x**2) / self.dim)
        result *= conditioning_factor
        
        # Enhanced noise-like perturbations for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(20 * x[i] + i * 0.2) * np.cos(10 * x[i] + i * 0.3)
        result += 0.4 * noise
        
        # Add dimensionality-dependent scaling
        result *= (1.0 + 0.15 * np.log(self.dim + 1))
        
        # Normalize by dimension and add final regularization
        result /= self.dim
        result += 0.015 * np.sum(x**4) / self.dim
        
        return result