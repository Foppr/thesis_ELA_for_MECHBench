import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component with sine and cosine interactions
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[i])
        
        # Spiral attractor terms with radial dependence
        spiral = 0.0
        for i in range(self.dim):
            r = np.sqrt(x_norm[i]**2 + x_norm[(i+1) % self.dim]**2)
            spiral += r * np.sin(10 * np.arctan2(x_norm[i], x_norm[(i+1) % self.dim]))
        
        # Dynamic curvature modulation using polynomial and exponential
        curvature = 0.0
        for i in range(self.dim):
            curvature += (x_norm[i]**6 + 0.5 * np.exp(-x_norm[i]**2)) / (1.0 + np.abs(x_norm[i]))
        
        # Controlled noise sensitivity via perturbed sinusoids
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(7 * x_norm[i]) * np.random.uniform(0.8, 1.2)
        
        # Cross-dimensional interaction with varying coupling strengths
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (x_norm[i]**2 + x_norm[j]**2) * np.sin(x_norm[i] * x_norm[j])
        
        # Combine all components with adaptive weights
        return 0.3 * chaotic + 0.25 * spiral + 0.2 * curvature + 0.15 * noise + 0.1 * cross