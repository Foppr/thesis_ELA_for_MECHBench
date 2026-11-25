import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic gradient component with richer harmonic content and dynamic coupling
        for i in range(self.dim):
            # Multi-frequency chaotic terms with varying amplitudes, phases, and dynamic modulation
            chaos_term = (np.exp(-0.1 * x[i]**2) * 
                         (np.sin(25 * x[i]) + 
                          0.7 * np.sin(70 * x[i]) + 
                          0.4 * np.sin(190 * x[i]) + 
                          0.2 * np.sin(370 * x[i]) + 
                          0.05 * np.sin(730 * x[i]) +
                          0.02 * np.sin(1460 * x[i])))
            result += chaos_term**2
        
        # Enhanced cross-dimensional interference with non-linear coupling and dynamic strength
        for i in range(self.dim - 1):
            # Non-linear coupling strength based on variable interactions with dynamic modulation
            coupling_strength = 1.0 / (1.0 + np.exp(-0.6 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(10 * (x[i] + x[i+1])) * np.cos(7 * (x[i] - x[i+1]))
            result += 1.0 * interference
        
        # Enhanced ridge structure with sharper curvature and multi-scale modulation
        for i in range(self.dim):
            # Enhanced quadratic ridges with more pronounced peaks, valleys, and multi-scale harmonics
            ridge = (np.sin(35 * x[i]) + 
                    0.7 * np.sin(65 * x[i]) + 
                    0.4 * np.sin(125 * x[i]) + 
                    0.2 * np.sin(245 * x[i]) + 
                    0.05 * np.sin(485 * x[i]) +
                    0.02 * np.sin(970 * x[i]))
            result += 0.6 * ridge**2
        
        # Improved saddle point configuration with stronger curvature variation and dynamic behavior
        for i in range(self.dim):
            # Enhanced saddle behavior with more pronounced directional differences and time-like modulation
            if i < self.dim - 1:
                saddle = (x[i]**5 - x[i+1]**5) * np.exp(-0.06 * (x[i]**2 + x[i+1]**2))
                result += 0.7 * saddle
        
        # Enhanced multi-scale modulation with more complex frequency progression and phase coupling
        for i in range(self.dim):
            # Advanced periodic modulation with varying frequency, amplitude, and phase coupling
            modulated = np.sin(2 * np.pi * x[i] * (1 + 0.9 * np.sin(x[i]**2))) * np.exp(-0.03 * x[i]**2)
            result += 1.1 * modulated**3
        
        # Refined adaptive conditioning based on position and dimensionality with enhanced dynamic scaling
        conditioning_factor = 1.0 + 0.7 * np.tanh(np.sum(x**2) / self.dim)
        result *= conditioning_factor
        
        # Enhanced noise-like perturbations for increased complexity with chaotic phase coupling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(25 * x[i] + i * 0.25) * np.cos(12 * x[i] + i * 0.35)
        result += 0.5 * noise
        
        # Add dimensionality-dependent scaling with enhanced logarithmic growth
        result *= (1.0 + 0.3 * np.log(self.dim + 1))
        
        # Normalize by dimension and add final regularization with enhanced quartic term
        result /= self.dim
        result += 0.03 * np.sum(x**4) / self.dim
        
        return result