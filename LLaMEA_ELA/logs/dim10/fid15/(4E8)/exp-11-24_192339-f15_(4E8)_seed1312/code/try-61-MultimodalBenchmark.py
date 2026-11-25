import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Chaotic multimodal component with exponential decay and trigonometric interference
        chaotic = 0
        for i in range(self.dim):
            freq = 4 * (i + 1) / self.dim
            chaotic += np.exp(-0.5 * (x[i] / 2.0)**2) * np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i] / 2.0)
        
        # Wave interference component with varying amplitudes and frequencies
        wave = 0
        for i in range(self.dim):
            amp = 0.8 + 0.2 * np.sin(0.5 * i)
            freq = 2 * (i + 1) / self.dim
            wave += amp * np.sin(freq * np.pi * x[i] + 0.3 * np.cos(freq * np.pi * x[i]))
        
        # Adaptive radial basis function with dynamic centers and widths
        rbf = 0
        for i in range(min(7, self.dim)):
            center = -5.0 + (10.0 / (min(7, self.dim) - 1)) * i if min(7, self.dim) > 1 else 0.0
            width = 0.5 + 0.3 * np.sin(0.2 * i)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional coupling with polynomial interactions
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.02 * (x[i]**4) * (x[j]**3) + 0.015 * (x[i]**3) * (x[j]**4)
        
        # Dynamic scaling factor based on problem dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1) + 0.03 * np.cos(self.dim * 0.3)
        
        # Global shift with chaotic component
        shift = 0.2 * np.sum(np.abs(x)) + 0.1 * np.sum(np.sin(x)**2) + 0.05 * np.sum(np.exp(-x**2))
        
        # Combined function
        return sphere + scale_factor * (0.3 * chaotic + 0.1 * wave + 0.05 * rbf + 0.02 * cross) + shift