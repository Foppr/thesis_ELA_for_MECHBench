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
                         (np.sin(35 * x[i]) + 
                          0.7 * np.sin(90 * x[i]) + 
                          0.4 * np.sin(220 * x[i]) + 
                          0.2 * np.sin(450 * x[i]) + 
                          0.05 * np.sin(850 * x[i]) +
                          0.02 * np.sin(1700 * x[i])))
            result += chaos_term**2
        
        # Enhanced cross-dimensional interference with non-linear coupling and dynamic strength
        for i in range(self.dim - 1):
            # Non-linear coupling strength based on variable interactions with dynamic modulation
            coupling_strength = 1.0 / (1.0 + np.exp(-0.8 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(15 * (x[i] + x[i+1])) * np.cos(10 * (x[i] - x[i+1]))
            result += 1.5 * interference
        
        # Enhanced ridge structure with sharper curvature and multi-scale modulation
        for i in range(self.dim):
            # Enhanced quadratic ridges with more pronounced peaks, valleys, and multi-scale harmonics
            ridge = (np.sin(45 * x[i]) + 
                    0.7 * np.sin(75 * x[i]) + 
                    0.4 * np.sin(140 * x[i]) + 
                    0.2 * np.sin(270 * x[i]) + 
                    0.05 * np.sin(550 * x[i]) +
                    0.02 * np.sin(1100 * x[i]))
            result += 0.8 * ridge**2
        
        # Improved saddle point configuration with stronger curvature variation and dynamic behavior
        for i in range(self.dim):
            # Enhanced saddle behavior with more pronounced directional differences and time-like modulation
            if i < self.dim - 1:
                saddle = (x[i]**7 - x[i+1]**7) * np.exp(-0.08 * (x[i]**2 + x[i+1]**2))
                result += 0.9 * saddle
        
        # Enhanced multi-scale modulation with more complex frequency progression and phase coupling
        for i in range(self.dim):
            # Advanced periodic modulation with varying frequency, amplitude, and phase coupling
            modulated = np.sin(2 * np.pi * x[i] * (1 + 1.2 * np.sin(x[i]**2))) * np.exp(-0.05 * x[i]**2)
            result += 1.5 * modulated**3
        
        # Refined adaptive conditioning based on position and dimensionality with enhanced dynamic scaling
        conditioning_factor = 1.0 + 0.9 * np.tanh(np.sum(x**2) / self.dim)
        result *= conditioning_factor
        
        # Enhanced noise-like perturbations for increased complexity with chaotic phase coupling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(35 * x[i] + i * 0.35) * np.cos(17 * x[i] + i * 0.45)
        result += 0.7 * noise
        
        # Add dimensionality-dependent scaling with enhanced logarithmic growth
        result *= (1.0 + 0.5 * np.log(self.dim + 1))
        
        # Normalize by dimension and add final regularization with enhanced quartic term
        result /= self.dim
        result += 0.05 * np.sum(x**4) / self.dim
        
        return result