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
                         (np.sin(45 * x[i]) + 
                          0.6 * np.sin(110 * x[i]) + 
                          0.3 * np.sin(270 * x[i]) + 
                          0.15 * np.sin(500 * x[i]) + 
                          0.04 * np.sin(900 * x[i]) +
                          0.01 * np.sin(1800 * x[i])))
            result += chaos_term**2
        
        # Enhanced cross-dimensional interference with modified coupling and dynamic strength
        for i in range(self.dim - 1):
            # Non-linear coupling strength with altered modulation
            coupling_strength = 1.0 / (1.0 + np.exp(-0.8 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(17 * (x[i] + x[i+1])) * np.cos(13 * (x[i] - x[i+1]))
            result += 1.5 * interference
        
        # Enhanced ridge structure with modified curvature and multi-scale modulation
        for i in range(self.dim):
            # Enhanced quadratic ridges with altered peak shapes and multi-scale harmonics
            ridge = (np.sin(55 * x[i]) + 
                    0.6 * np.sin(90 * x[i]) + 
                    0.3 * np.sin(160 * x[i]) + 
                    0.15 * np.sin(300 * x[i]) + 
                    0.04 * np.sin(600 * x[i]) +
                    0.01 * np.sin(1200 * x[i]))
            result += 0.9 * ridge**2
        
        # Improved saddle point configuration with altered curvature variation and dynamic behavior
        for i in range(self.dim):
            # Enhanced saddle behavior with modified directional differences and time-like modulation
            if i < self.dim - 1:
                saddle = (x[i]**7 - x[i+1]**7) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
                result += 1.0 * saddle
        
        # Enhanced multi-scale modulation with modified frequency progression and phase coupling
        for i in range(self.dim):
            # Advanced periodic modulation with altered frequency, amplitude, and phase coupling
            modulated = np.sin(2 * np.pi * x[i] * (1 + 1.1 * np.sin(x[i]**2))) * np.exp(-0.07 * x[i]**2)
            result += 1.7 * modulated**3
        
        # Refined adaptive conditioning based on position and dimensionality with modified dynamic scaling
        conditioning_factor = 1.0 + 1.0 * np.tanh(np.sum(x**2) / self.dim)
        result *= conditioning_factor
        
        # Enhanced noise-like perturbations for increased complexity with altered phase coupling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(40 * x[i] + i * 0.45) * np.cos(20 * x[i] + i * 0.55)
        result += 0.8 * noise
        
        # Add dimensionality-dependent scaling with modified logarithmic growth
        result *= (1.0 + 0.5 * np.log(self.dim + 1))
        
        # Normalize by dimension and add final regularization with modified quartic term
        result /= self.dim
        result += 0.06 * np.sum(x**4) / self.dim
        
        return result