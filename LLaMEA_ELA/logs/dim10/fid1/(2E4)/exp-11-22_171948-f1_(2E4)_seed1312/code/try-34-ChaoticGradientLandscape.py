import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic gradient component with richer harmonic content
        for i in range(self.dim):
            # Multi-frequency chaotic terms with varying amplitudes and phases
            chaos_term = (np.exp(-0.1 * x[i]**2) * 
                         (np.sin(15 * x[i]) + 
                          0.6 * np.sin(45 * x[i]) + 
                          0.3 * np.sin(135 * x[i]) + 
                          0.1 * np.sin(270 * x[i])))
            result += chaos_term**2
        
        # Enhanced cross-dimensional interference with non-linear coupling
        for i in range(self.dim - 1):
            # Non-linear coupling strength based on variable interactions
            coupling_strength = 1.0 / (1.0 + np.exp(-0.3 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(7 * (x[i] + x[i+1])) * np.cos(4 * (x[i] - x[i+1]))
            result += 0.6 * interference
        
        # Enhanced ridge structure with sharper curvature
        for i in range(self.dim):
            # Enhanced quadratic ridges with more pronounced peaks and valleys
            ridge = (np.sin(25 * x[i]) + 
                    0.6 * np.sin(50 * x[i]) + 
                    0.3 * np.sin(100 * x[i]) + 
                    0.1 * np.sin(200 * x[i]))
            result += 0.4 * ridge**2
        
        # Improved saddle point configuration with stronger curvature variation
        for i in range(self.dim):
            # Enhanced saddle behavior with more pronounced directional differences
            if i < self.dim - 1:
                saddle = (x[i]**3 - x[i+1]**3) * np.exp(-0.03 * (x[i]**2 + x[i+1]**2))
                result += 0.5 * saddle
        
        # Enhanced multi-scale modulation with more complex frequency progression
        for i in range(self.dim):
            # Advanced periodic modulation with varying frequency and amplitude
            modulated = np.sin(2 * np.pi * x[i] * (1 + 0.7 * np.sin(x[i]**2))) * np.exp(-0.01 * x[i]**2)
            result += 0.7 * modulated**3
        
        # Refined adaptive conditioning based on position and dimensionality
        conditioning_factor = 1.0 + 0.4 * np.tanh(np.sum(x**2) / self.dim)
        result *= conditioning_factor
        
        # Enhanced noise-like perturbations for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(17 * x[i] + i * 0.15) * np.cos(9 * x[i] + i * 0.25)
        result += 0.3 * noise
        
        # Add dimensionality-dependent scaling
        result *= (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Normalize by dimension and add final regularization
        result /= self.dim
        result += 0.01 * np.sum(x**4) / self.dim
        
        return result