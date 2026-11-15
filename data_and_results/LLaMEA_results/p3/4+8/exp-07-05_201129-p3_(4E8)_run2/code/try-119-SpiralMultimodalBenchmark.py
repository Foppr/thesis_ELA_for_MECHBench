import numpy as np

class SpiralMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial base with varying degrees
        poly = np.sum(x_normalized**4) + 0.5 * np.sum(x_normalized**6)
        
        # Trigonometric components creating spiral-like patterns
        trig = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_normalized[i], x_normalized[(i+1) % self.dim])
            radius = np.sqrt(x_normalized[i]**2 + x_normalized[(i+1) % self.dim]**2)
            trig += np.sin(5 * radius + 3 * angle) * np.cos(4 * radius - 2 * angle)
        
        # Exponential interaction term creating rugged landscape
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-0.5 * (x_normalized[i] - 0.3)**2) * np.sin(10 * x_normalized[i])
        
        # Spiral-shaped local minima with varying radii
        spiral = 0.0
        for i in range(1, min(6, self.dim + 1)):
            radius = 0.5 + 0.3 * np.sin(i * 0.5)
            angle = i * 0.8
            x_spiral = radius * np.cos(angle)
            y_spiral = radius * np.sin(angle)
            spiral += (x_normalized[i-1] - x_spiral)**2 + (x_normalized[(i+1) % self.dim] - y_spiral)**2
        
        # Global optimum at origin with additional noise
        return poly + 0.3 * trig + 0.2 * exp_term + 0.1 * spiral + 0.5