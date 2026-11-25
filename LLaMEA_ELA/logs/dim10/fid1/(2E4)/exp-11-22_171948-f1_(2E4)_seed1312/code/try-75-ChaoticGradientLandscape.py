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
                          0.5 * np.sin(90 * x[i]) + 
                          0.25 * np.sin(220 * x[i]) + 
                          0.12 * np.sin(420 * x[i]) + 
                          0.03 * np.sin(780 * x[i]) +
                          0.008 * np.sin(1550 * x[i])))
            result += chaos_term**2
        
        # Enhanced cross-dimensional interference with modified coupling and dynamic strength
        for i in range(self.dim - 1):
            # Non-linear coupling strength with altered modulation
            coupling_strength = 1.0 / (1.0 + np.exp(-0.4 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(13 * (x[i] + x[i+1])) * np.cos(9 * (x[i] - x[i+1]))
            result += 1.3 * interference
        
        # Enhanced ridge structure with modified curvature and multi-scale modulation
        for i in range(self.dim):
            # Enhanced quadratic ridges with altered peak shapes and multi-scale harmonics
            ridge = (np.sin(45 * x[i]) + 
                    0.5 * np.sin(75 * x[i]) + 
                    0.25 * np.sin(135 * x[i]) + 
                    0.12 * np.sin(260 * x[i]) + 
                    0.03 * np.sin(510 * x[i]) +
                    0.008 * np.sin(1010 * x[i]))
            result += 0.75 * ridge**2
        
        # Improved saddle point configuration with altered curvature variation and dynamic behavior
        for i in range(self.dim):
            # Enhanced saddle behavior with modified directional differences and time-like modulation
            if i < self.dim - 1:
                saddle = (x[i]**5 - x[i+1]**5) * np.exp(-0.06 * (x[i]**2 + x[i+1]**2))
                result += 0.85 * saddle
        
        # Enhanced multi-scale modulation with modified frequency progression and phase coupling
        for i in range(self.dim):
            # Advanced periodic modulation with altered frequency, amplitude, and phase coupling
            modulated = np.sin(2 * np.pi * x[i] * (1 + 0.7 * np.sin(x[i]**2))) * np.exp(-0.035 * x[i]**2)
            result += 1.35 * modulated**3
        
        # Refined adaptive conditioning based on position and dimensionality with modified dynamic scaling
        conditioning_factor = 1.0 + 0.75 * np.tanh(np.sum(x**2) / self.dim)
        result *= conditioning_factor
        
        # Enhanced noise-like perturbations for increased complexity with altered phase coupling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(32 * x[i] + i * 0.32) * np.cos(16 * x[i] + i * 0.42)
        result += 0.65 * noise
        
        # Add dimensionality-dependent scaling with modified logarithmic growth
        result *= (1.0 + 0.42 * np.log(self.dim + 1))
        
        # Normalize by dimension and add final regularization with modified quartic term
        result /= self.dim
        result += 0.035 * np.sum(x**4) / self.dim
        
        return result