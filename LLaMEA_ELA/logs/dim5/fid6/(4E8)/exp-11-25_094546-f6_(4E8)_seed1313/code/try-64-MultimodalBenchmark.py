import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spiral attractor component with chaotic dynamics
        spiral = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Create spiral pattern with varying radius and angle
            r = np.sqrt(xi**2 + (0.1 * xi)**2)
            theta = np.arctan2(0.1 * xi, xi)
            spiral += r * np.sin(5.0 * theta + i * 0.5) * np.cos(3.0 * theta - i * 0.3)
        
        # Chaotic sine wave component with adaptive frequency
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10.0 * x_norm[i] + np.sin(7.0 * x_norm[i])) * np.exp(-0.5 * x_norm[i]**2)
        
        # Dynamic curvature modulation with noise sensitivity
        curvature = 0.0
        for i in range(self.dim):
            # Add dynamic scaling based on neighboring dimensions
            if i > 0:
                curvature += (x_norm[i] - x_norm[i-1])**2 * np.cos(2.0 * x_norm[i])
            else:
                curvature += x_norm[i]**2 * np.cos(2.0 * x_norm[i])
        
        # Embedded noise sensitivity with adaptive threshold
        noise = 0.0
        for i in range(self.dim):
            # Add controlled noise that increases near boundaries
            noise += np.sin(15.0 * x_norm[i]) * (1.0 + 0.1 * np.abs(x_norm[i]))
        
        # Cross-dimensional coupling with exponential decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross += np.exp(-dist**2) * np.sin(8.0 * dist)
        
        # Combine all components with adaptive weights based on dimensionality
        weight_spiral = 0.3 + 0.1 * np.sin(self.dim * 0.1)
        weight_chaotic = 0.25 + 0.05 * np.cos(self.dim * 0.05)
        weight_curvature = 0.2 + 0.1 * np.tanh(self.dim * 0.02)
        weight_noise = 0.15 + 0.05 * np.sin(self.dim * 0.08)
        weight_cross = 0.1
        
        return (weight_spiral * spiral + 
                weight_chaotic * chaotic + 
                weight_curvature * curvature + 
                weight_noise * noise + 
                weight_cross * cross)