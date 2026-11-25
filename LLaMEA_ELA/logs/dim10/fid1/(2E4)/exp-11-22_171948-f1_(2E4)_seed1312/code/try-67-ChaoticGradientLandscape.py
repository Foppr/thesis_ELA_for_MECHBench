import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic gradient component with modified harmonic content and dynamic coupling
        for i in range(self.dim):
            # Multi-frequency chaotic terms with altered amplitudes, phases, and dynamic modulation
            chaos_term = (np.exp(-0.1 * x[i]**2) * 
                         (np.sin(35 * x[i]) + 
                          0.6 * np.sin(90 * x[i]) + 
                          0.35 * np.sin(220 * x[i]) + 
                          0.18 * np.sin(420 * x[i]) + 
                          0.04 * np.sin(820 * x[i]) +
                          0.015 * np.sin(1620 * x[i])))
            result += chaos_term**2
        
        # Enhanced cross-dimensional interference with modified coupling and dynamic strength
        for i in range(self.dim - 1):
            # Non-linear coupling strength based on variable interactions with altered modulation
            coupling_strength = 1.0 / (1.0 + np.exp(-0.6 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(14 * (x[i] + x[i+1])) * np.cos(10 * (x[i] - x[i+1]))
            result += 1.3 * interference
        
        # Enhanced ridge structure with modified curvature and multi-scale modulation
        for i in range(self.dim):
            # Enhanced quadratic ridges with altered peak shapes, valleys, and multi-scale harmonics
            ridge = (np.sin(45 * x[i]) + 
                    0.6 * np.sin(75 * x[i]) + 
                    0.35 * np.sin(140 * x[i]) + 
                    0.18 * np.sin(260 * x[i]) + 
                    0.04 * np.sin(510 * x[i]) +
                    0.015 * np.sin(1010 * x[i]))
            result += 0.75 * ridge**2
        
        # Improved saddle point configuration with altered curvature variation and dynamic behavior
        for i in range(self.dim):
            # Enhanced saddle behavior with different directional differences and time-like modulation
            if i < self.dim - 1:
                saddle = (x[i]**6 - x[i+1]**6) * np.exp(-0.08 * (x[i]**2 + x[i+1]**2))
                result += 0.85 * saddle
        
        # Enhanced multi-scale modulation with modified frequency progression and phase coupling
        for i in range(self.dim):
            # Advanced periodic modulation with altered frequency, amplitude, and phase coupling
            modulated = np.sin(2 * np.pi * x[i] * (1 + 1.2 * np.sin(x[i]**2))) * np.exp(-0.05 * x[i]**2)
            result += 1.4 * modulated**3
        
        # Refined adaptive conditioning based on position and dimensionality with altered scaling
        conditioning_factor = 1.0 + 0.7 * np.tanh(np.sum(x**2) / self.dim)
        result *= conditioning_factor
        
        # Enhanced noise-like perturbations for increased complexity with modified phase coupling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(35 * x[i] + i * 0.35) * np.cos(18 * x[i] + i * 0.45)
        result += 0.65 * noise
        
        # Add dimensionality-dependent scaling with modified logarithmic growth
        result *= (1.0 + 0.42 * np.log(self.dim + 1))
        
        # Normalize by dimension and add final regularization with altered quartic term
        result /= self.dim
        result += 0.045 * np.sum(x**4) / self.dim
        
        return result