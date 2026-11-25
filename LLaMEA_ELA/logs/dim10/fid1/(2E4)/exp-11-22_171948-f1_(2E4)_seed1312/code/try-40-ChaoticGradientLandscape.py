import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Ultra-high frequency chaotic component with exponential modulation
        for i in range(self.dim):
            chaos_term = (np.exp(-0.05 * x[i]**2) * 
                         (np.sin(30 * x[i]) + 
                          0.7 * np.sin(90 * x[i]) + 
                          0.4 * np.sin(270 * x[i]) + 
                          0.2 * np.sin(810 * x[i]) + 
                          0.05 * np.sin(2430 * x[i])))
            result += chaos_term**3
        
        # Fractal-like ridge structure with self-similar patterns
        for i in range(self.dim):
            ridge = (np.sin(50 * x[i]) + 
                    0.5 * np.sin(100 * x[i]) + 
                    0.2 * np.sin(200 * x[i]) + 
                    0.1 * np.sin(400 * x[i]) + 
                    0.05 * np.sin(800 * x[i]))
            result += 0.6 * ridge**3
        
        # Dynamic coupling with time-like progression
        for i in range(self.dim - 1):
            coupling_strength = 1.0 / (1.0 + np.exp(-0.5 * (x[i] - x[i+1])**2))
            interference = coupling_strength * np.sin(13 * (x[i] + x[i+1])) * np.cos(9 * (x[i] - x[i+1]))
            result += 0.8 * interference
        
        # Saddle point with hyperbolic tangent curvature variation
        for i in range(self.dim):
            if i < self.dim - 2:
                saddle = (x[i]**4 - x[i+1]**4) * np.tanh(0.05 * (x[i]**2 + x[i+1]**2))
                result += 0.7 * saddle
        
        # Multi-scale fractal modulation with recursive frequency progression
        for i in range(self.dim):
            modulated = np.sin(2 * np.pi * x[i] * (1 + 0.9 * np.sin(x[i]**3))) * np.exp(-0.02 * x[i]**2)
            result += 0.9 * modulated**4
        
        # Adaptive conditioning with exponential scaling
        conditioning_factor = 1.0 + 0.6 * np.tanh(np.sum(x**3) / self.dim)
        result *= conditioning_factor
        
        # Ultra-complex noise-like perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(23 * x[i] + i * 0.2) * np.cos(13 * x[i] + i * 0.3) * np.sin(7 * x[i] + i * 0.1)
        result += 0.5 * noise
        
        # Add dimensionality-dependent scaling with fractal exponent
        result *= (1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.log(self.dim + 1)**2)
        
        # Normalize by dimension and add final regularization with cubic terms
        result /= self.dim
        result += 0.02 * np.sum(x**6) / self.dim
        
        return result