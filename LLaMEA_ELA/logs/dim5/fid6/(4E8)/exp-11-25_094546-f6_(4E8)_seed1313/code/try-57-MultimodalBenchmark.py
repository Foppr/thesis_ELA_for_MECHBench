import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component with nested sine-cosine interactions and time-varying frequencies
        chaotic = 0.0
        for i in range(self.dim):
            freq = 3 + 2 * np.sin(0.5 * i)
            chaotic += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 1.5)
        
        # Nested spiral attractor terms with time-varying angular frequencies and radial dependence
        spiral = 0.0
        for i in range(self.dim):
            r = np.sqrt(x_norm[i]**2 + x_norm[(i+1) % self.dim]**2)
            angle = np.arctan2(x_norm[i], x_norm[(i+1) % self.dim])
            freq = 5 + 3 * np.cos(0.3 * i)
            spiral += r * np.sin(freq * angle + 0.5 * np.sin(2 * angle))
        
        # Dynamic curvature modulation with exponential and polynomial components
        curvature = 0.0
        for i in range(self.dim):
            exp_term = np.exp(-x_norm[i]**2) * np.cos(x_norm[i]**3)
            poly_term = x_norm[i]**7 + 0.3 * x_norm[i]**4 + 0.1 * x_norm[i]
            curvature += (poly_term + exp_term) / (1.0 + np.abs(x_norm[i]))
        
        # Adaptive noise sensitivity with multi-scale perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += (np.sin(7 * x_norm[i]) + 0.5 * np.sin(14 * x_norm[i])) * np.random.uniform(0.7, 1.3)
        
        # High-order cross-dimensional coupling with non-linear interaction strengths
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_norm[i] * x_norm[j]) + 0.5 * np.cos(x_norm[i]**2 + x_norm[j]**2)
                cross += (x_norm[i]**3 + x_norm[j]**3) * coupling
        
        # Add a global scaling factor that varies with dimensionality
        scale_factor = 1.0 + 0.1 * np.sin(self.dim * 0.2)
        
        # Combine all components with adaptive weights and global scaling
        return scale_factor * (0.25 * chaotic + 0.3 * spiral + 0.2 * curvature + 0.15 * noise + 0.1 * cross)