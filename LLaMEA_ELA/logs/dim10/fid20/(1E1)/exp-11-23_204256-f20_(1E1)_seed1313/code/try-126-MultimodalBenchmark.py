import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential radial component with multiple fractal-like modulations
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(3 * r) * np.sin(7 * np.pi * r) + 0.3 * np.exp(5 * r) * np.cos(11 * np.pi * r)
        
        # Chaotic angular component using nested trigonometric functions
        if self.dim == 1:
            angular_term = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = np.sin(13 * angles) * np.cos(17 * angles) + 0.4 * np.sin(23 * angles) * np.cos(29 * angles)
            
        # Dynamic cross-dimensional interactions with exponential coupling strengths
        cross_terms = 0
        for i in range(self.dim - 1):
            coupling = np.exp(2 * abs(x_norm[i]) + 1.5 * abs(x_norm[i+1]))
            cross_terms += coupling * (x_norm[i]**3 + x_norm[i+1]**3) * np.sin(5 * np.pi * x_norm[i] * x_norm[i+1])
            
        # Fractal-like noise component with multiple frequency bands
        noise = 0
        for freq in [10, 15, 20, 25]:
            noise += np.sin(freq * np.pi * r) ** 5 + 0.6 * np.cos(freq * np.pi * r) ** 3
            
        # Adaptive conditioning factor with exponential scaling
        cond_factor = 2.0 + 1.2 * np.log(self.dim + 1) + 0.3 * np.sin(np.pi * self.dim / 4)
        
        # Additional chaotic perturbation term
        perturbation = np.sum(np.sin(30 * x_norm) ** 6 + 0.8 * np.cos(35 * x_norm) ** 4)
        
        # Combine all components with appropriate scaling
        return cond_factor * (radial_term + angular_term + cross_terms + noise + perturbation)