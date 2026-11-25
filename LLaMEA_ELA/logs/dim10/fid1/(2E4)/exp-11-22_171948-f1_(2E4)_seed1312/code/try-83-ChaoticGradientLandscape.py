import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic gradient component with altered harmonic complexity and dynamic modulation
        for i in range(self.dim):
            # Multi-frequency chaotic terms with modified amplitudes, phase shifts, and time-varying coupling
            chaos_term = (np.exp(-0.12 * x[i]**2) * 
                         (np.sin(35 * x[i]) + 
                          0.5 * np.sin(90 * x[i]) + 
                          0.25 * np.sin(220 * x[i]) + 
                          0.12 * np.sin(450 * x[i]) + 
                          0.03 * np.sin(800 * x[i]) +
                          0.008 * np.sin(1600 * x[i]) +
                          0.003 * np.sin(3000 * x[i])))
            result += chaos_term**2
        
        # Enhanced cross-dimensional interference with modified coupling and dynamic strength
        for i in range(self.dim - 1):
            # Non-linear coupling strength with altered modulation and phase shifts
            coupling_strength = 1.0 / (1.0 + np.exp(-0.4 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(13 * (x[i] + x[i+1])) * np.cos(9 * (x[i] - x[i+1]))
            result += 1.3 * interference
        
        # Enhanced ridge structure with modified curvature and multi-scale modulation
        for i in range(self.dim):
            # Enhanced quadratic ridges with sharper peaks, altered phase relationships, and modified harmonics
            ridge = (np.sin(45 * x[i]) + 
                    0.5 * np.sin(80 * x[i]) + 
                    0.25 * np.sin(140 * x[i]) + 
                    0.12 * np.sin(280 * x[i]) + 
                    0.03 * np.sin(550 * x[i]) +
                    0.008 * np.sin(1100 * x[i]) +
                    0.003 * np.sin(2200 * x[i]))
            result += 0.9 * ridge**2
        
        # Enhanced saddle point configuration with modified curvature variation and dynamic behavior
        for i in range(self.dim):
            # Enhanced saddle behavior with altered directional differences and non-linear modulation
            if i < self.dim - 1:
                saddle = (x[i]**6 - x[i+1]**6) * np.exp(-0.07 * (x[i]**2 + x[i+1]**2))
                result += 0.9 * saddle
        
        # Enhanced multi-scale modulation with modified frequency progression and phase coupling
        for i in range(self.dim):
            # Advanced periodic modulation with modified frequency, amplitude, and phase coupling
            modulated = np.sin(2 * np.pi * x[i] * (1 + 0.8 * np.sin(x[i]**2))) * np.exp(-0.04 * x[i]**2)
            result += 1.4 * modulated**3
        
        # Refined adaptive conditioning based on position and dimensionality with modified dynamic scaling
        conditioning_factor = 1.0 + 0.9 * np.tanh(np.sum(x**2) / self.dim)
        result *= conditioning_factor
        
        # Enhanced noise-like perturbations for increased complexity with modified phase coupling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(35 * x[i] + i * 0.35) * np.cos(18 * x[i] + i * 0.45)
        result += 0.7 * noise
        
        # Add dimensionality-dependent scaling with modified logarithmic growth
        result *= (1.0 + 0.5 * np.log(self.dim + 1))
        
        # Normalize by dimension and add final regularization with modified quartic term
        result /= self.dim
        result += 0.04 * np.sum(x**4) / self.dim
        
        return result