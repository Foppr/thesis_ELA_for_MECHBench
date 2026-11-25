import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic gradient component with increased harmonic complexity and dynamic modulation
        for i in range(self.dim):
            # Multi-frequency chaotic terms with amplified amplitudes, phase shifts, and time-varying coupling
            chaos_term = (np.exp(-0.15 * x[i]**2) * 
                         (np.sin(40 * x[i]) + 
                          0.6 * np.sin(100 * x[i]) + 
                          0.3 * np.sin(250 * x[i]) + 
                          0.15 * np.sin(500 * x[i]) + 
                          0.04 * np.sin(900 * x[i]) +
                          0.01 * np.sin(1800 * x[i]) +
                          0.005 * np.sin(3200 * x[i])))
            result += chaos_term**2
        
        # Enhanced cross-dimensional interference with stronger coupling and dynamic strength
        for i in range(self.dim - 1):
            # Non-linear coupling strength with more aggressive modulation and phase shifts
            coupling_strength = 1.0 / (1.0 + np.exp(-0.5 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(15 * (x[i] + x[i+1])) * np.cos(11 * (x[i] - x[i+1]))
            result += 1.5 * interference
        
        # Enhanced ridge structure with more complex curvature and multi-scale modulation
        for i in range(self.dim):
            # Enhanced quadratic ridges with sharper peaks, altered phase relationships, and multi-scale harmonics
            ridge = (np.sin(50 * x[i]) + 
                    0.6 * np.sin(85 * x[i]) + 
                    0.3 * np.sin(150 * x[i]) + 
                    0.15 * np.sin(300 * x[i]) + 
                    0.04 * np.sin(600 * x[i]) +
                    0.01 * np.sin(1200 * x[i]) +
                    0.005 * np.sin(2400 * x[i]))
            result += 0.85 * ridge**2
        
        # Enhanced saddle point configuration with increased curvature variation and dynamic behavior
        for i in range(self.dim):
            # Enhanced saddle behavior with stronger directional differences and non-linear modulation
            if i < self.dim - 1:
                saddle = (x[i]**7 - x[i+1]**7) * np.exp(-0.08 * (x[i]**2 + x[i+1]**2))
                result += 1.0 * saddle
        
        # Enhanced multi-scale modulation with more aggressive frequency progression and phase coupling
        for i in range(self.dim):
            # Advanced periodic modulation with amplified frequency, amplitude, and phase coupling
            modulated = np.sin(2 * np.pi * x[i] * (1 + 0.9 * np.sin(x[i]**2))) * np.exp(-0.05 * x[i]**2)
            result += 1.6 * modulated**3
        
        # Refined adaptive conditioning based on position and dimensionality with enhanced dynamic scaling
        conditioning_factor = 1.0 + 1.0 * np.tanh(np.sum(x**2) / self.dim)
        result *= conditioning_factor
        
        # Enhanced noise-like perturbations for increased complexity with more aggressive phase coupling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(40 * x[i] + i * 0.4) * np.cos(20 * x[i] + i * 0.5)
        result += 0.8 * noise
        
        # Add dimensionality-dependent scaling with more aggressive logarithmic growth
        result *= (1.0 + 0.6 * np.log(self.dim + 1))
        
        # Normalize by dimension and add final regularization with amplified quartic term
        result /= self.dim
        result += 0.05 * np.sum(x**4) / self.dim
        
        return result