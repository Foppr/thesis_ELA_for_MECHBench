import numpy as np

class ChaoticSaddleFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        scaled_x = x / 5.0
        
        # Base chaotic saddle-point term with fractal-like scaling
        result = 0.0
        for i in range(self.dim):
            # Dynamic polynomial exponents based on dimension index
            exp = 2 + 3 * np.sin(i * np.pi / max(1, self.dim - 1))
            result += np.abs(scaled_x[i])**exp
            
        # Add embedded fractal structures with multi-scale oscillations
        fractal_penalty = 0.0
        for i in range(self.dim):
            # Multi-scale oscillatory components
            scale1 = np.sin(10 * scaled_x[i]) * np.cos(5 * scaled_x[i])
            scale2 = np.sin(3 * scaled_x[i]) * np.cos(7 * scaled_x[i])
            scale3 = np.sin(15 * scaled_x[i]) * np.cos(2 * scaled_x[i])
            
            # Fractal-like interaction terms
            fractal_term = 0.5 * (scale1**2 + scale2**2 + scale3**2)
            fractal_penalty += fractal_term
            
        result += fractal_penalty
        
        # Introduce dynamic coupling with varying strength
        coupling_penalty = 0.0
        for i in range(self.dim):
            # Coupling with previous dimension (with dynamic strength)
            if i > 0:
                coupling_strength = 0.2 + 0.8 * np.sin(i * np.pi / max(1, self.dim - 1))
                coupling_term = coupling_strength * (scaled_x[i] - scaled_x[i-1])**4
                coupling_penalty += coupling_term
                
            # Coupling with next dimension (with dynamic strength)
            if i < self.dim - 1:
                coupling_strength = 0.2 + 0.8 * np.cos(i * np.pi / max(1, self.dim - 1))
                coupling_term = coupling_strength * (scaled_x[i] - scaled_x[i+1])**4
                coupling_penalty += coupling_term
                
        result += coupling_penalty
        
        # Add chaotic saddle-point components with varying parameters
        saddle_penalty = 0.0
        for i in range(self.dim):
            # Chaotic parameter variation based on dimension
            a = 1.5 + 0.5 * np.sin(i * np.pi / max(1, self.dim - 1))
            b = 0.8 + 0.4 * np.cos(i * np.pi / max(1, self.dim - 1))
            
            # Saddle-point contribution
            saddle_term = a * scaled_x[i]**2 - b * scaled_x[i]**4
            saddle_penalty += saddle_term
            
        result += saddle_penalty
        
        # Add multi-scale noise to increase non-smoothness
        noise = 0.05 * np.sum(np.sin(20 * scaled_x)**3 + np.cos(12 * scaled_x)**3)
        result += noise
        
        # Global scaling factor
        result *= (1.0 + 0.2 * self.dim)
        
        return result