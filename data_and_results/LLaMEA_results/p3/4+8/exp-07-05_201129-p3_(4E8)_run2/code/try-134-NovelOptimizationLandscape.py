import numpy as np

class NovelOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        poly = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Trigonometric components with multiple frequencies
        trig = 0.0
        for i in range(self.dim):
            trig += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) + \
                    np.sin(5 * x_norm[i]**2) * np.cos(3 * x_norm[i]**2)
        
        # Exponential interaction terms
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-5 * (x_norm[i] - 0.3)**2) + \
                        np.exp(-3 * (x_norm[i] + 0.4)**2)
        
        # Cross-term interactions with nonlinearity
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                cross += (x_norm[i] * x_norm[j]) * np.sin(2 * (x_norm[i] + x_norm[j]))
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = r * (1.0 + 0.3 * np.sin(12 * r))
        
        # Global optimum at origin with added noise-like perturbations
        return 0.5 * poly + 0.3 * trig + 0.2 * exp_term + 0.1 * cross + 0.15 * radial + 1.0