import numpy as np

class FractalChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Fractal-like self-similar structure using sine and cosine with varying frequencies
        fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Self-similar interaction with fractal scaling
                scale = 1.0 / (1.0 + np.abs(x_norm[i] - x_norm[j]))
                fractal += scale * np.sin(10 * (x_norm[i] + x_norm[j])) * np.cos(5 * (x_norm[i] - x_norm[j]))
        
        # Chaotic ridge structure with adaptive conditioning based on distance from origin
        distance = np.sqrt(np.sum(x_norm**2))
        ridge = 0.0
        for i in range(self.dim):
            # Adaptive frequency based on distance
            adaptive_freq = 15.0 * (1.0 + 0.5 * np.sin(distance))
            ridge += np.sin(adaptive_freq * x_norm[i]) * np.cos(adaptive_freq * x_norm[i])
        
        # Multimodal component with chaotic perturbations and varying amplitude
        multimodal = 0.0
        for i in range(self.dim):
            # Perturbed sinusoidal with chaotic modulation
            chaos_mod = 1.0 + 0.3 * np.sin(25 * x_norm[i])
            multimodal += chaos_mod * np.sin(8 * x_norm[i])**2 + np.cos(12 * x_norm[i])**2
        
        # Cross-term with chaotic interaction and distance-dependent scaling
        cross = 0.0
        for i in range(self.dim - 1):
            # Distance-dependent scaling factor
            scale = 1.0 + 0.2 * np.sin(5 * distance)
            cross += scale * np.sin(x_norm[i] + x_norm[i+1]) * np.cos(x_norm[i] - x_norm[i+1])
        
        # Global optimum at shifted position with chaotic perturbation
        shift = 0.05 * np.sum((x_norm - 0.2)**2)
        
        # Combine all components with different weights
        return 0.5 * quadratic + 1.2 * fractal + 1.8 * ridge + 1.5 * multimodal + 0.9 * cross + 0.4 * shift