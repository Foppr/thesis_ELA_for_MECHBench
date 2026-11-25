import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic component with higher frequency interactions
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(7 * x_norm[i]) * np.cos(5 * x_norm[i]) + np.sin(3 * x_norm[i]) * np.cos(9 * x_norm[i])
        
        # Spiral attractor terms with dynamic radius and angle modulation
        spiral = 0.0
        for i in range(self.dim):
            r = np.sqrt(x_norm[i]**2 + x_norm[(i+1) % self.dim]**2)
            angle = np.arctan2(x_norm[i], x_norm[(i+1) % self.dim])
            spiral += r * np.sin(15 * angle + 0.5 * np.cos(3 * r))
        
        # Elevated polynomial and exponential components with radial dependence
        curvature = 0.0
        for i in range(self.dim):
            curvature += (x_norm[i]**8 + 0.3 * np.exp(-x_norm[i]**3) + 0.7 * np.sin(x_norm[i]**2)) / (1.0 + np.abs(x_norm[i])**1.5)
        
        # Controlled noise sensitivity with adaptive perturbations
        noise = 0.0
        for i in range(self.dim):
            perturbation = np.random.uniform(0.7, 1.3)
            noise += np.sin(9 * x_norm[i]) * perturbation + np.cos(4 * x_norm[i]) * (1.0 - 0.2 * np.sin(x_norm[i]))
        
        # Increased cross-dimensional coupling with non-linear interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i]**2 + x_norm[j]**2)
                cross += (x_norm[i]**3 + x_norm[j]**3) * interaction
        
        # Novel radial exponential components with varying decay rates
        radial_exp = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x_norm**2))
            radial_exp += np.exp(-r**2) * np.sin(2 * r) + 0.5 * np.exp(-0.5 * r**3)
        
        # Combine all components with adaptive weights and additional nonlinear modulation
        return (0.25 * chaotic + 
                0.2 * spiral + 
                0.15 * curvature + 
                0.15 * noise + 
                0.1 * cross + 
                0.15 * radial_exp)