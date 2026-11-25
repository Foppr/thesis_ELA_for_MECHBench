import numpy as np

class FractalChaoticRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal Brownian motion component with varying Hurst parameters
        fbm_sum = 0.0
        for i in range(self.dim):
            hurst = 0.3 + 0.4 * np.sin(i * np.pi / (self.dim + 1))
            # Simple fractal sum approximation
            freq = 2**(i % 4 + 1)
            fbm_sum += np.sin(freq * x_norm[i]) * (np.abs(x_norm[i])**hurst)
        
        # Chaotic phase modulation with logistic map
        phase_mod = 0.0
        for i in range(self.dim):
            r = 3.8 + 0.2 * np.sin(i * np.pi / (self.dim + 2))
            logistic = 0.5
            for _ in range(5):
                logistic = r * logistic * (1 - logistic)
            phase_mod += np.cos(logistic * x_norm[i] * np.pi) * np.sin(x_norm[i]**2)
        
        # Adaptive ridge structure with dynamic curvature
        ridge_sum = 0.0
        for i in range(self.dim):
            # Dynamic ridge height and width
            height = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 3))
            width = 0.2 + 0.3 * np.cos(i * np.pi / (self.dim + 4))
            ridge_sum += height * np.exp(-0.5 * (x_norm[i] / width)**2) * np.sin(x_norm[i])
        
        # Multi-scale harmonic interference patterns
        harmonic_sum = 0.0
        for i in range(self.dim):
            for j in range(1, min(6, self.dim - i + 1)):
                freq = 1.0 + 2.0 * np.sin(j * np.pi / (self.dim + 5))
                amp = 0.5 + 0.5 * np.cos(j * np.pi / (self.dim + 6))
                harmonic_sum += amp * np.sin(freq * x_norm[i] + j) * np.cos(x_norm[i]**2)
        
        # Cross-dimensional coupling with fractal scaling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                scale = 0.5 + 0.5 * np.sin((i+j) * np.pi / (self.dim + 7))
                coupling_sum += scale * np.exp(-0.5 * ((x_norm[i] - x_norm[j])**2)) * np.sin(x_norm[i] * x_norm[j])
        
        # Dynamic conditioning factor based on dimensionality
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all components with adaptive weights
        result = (0.3 * fbm_sum + 
                 0.25 * phase_mod + 
                 0.2 * ridge_sum + 
                 0.15 * harmonic_sum + 
                 0.1 * coupling_sum) * condition_factor
        
        # Add a global scaling term
        result += 0.05 * np.sum(np.abs(x_norm)**3)
        
        return result