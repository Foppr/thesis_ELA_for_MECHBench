import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for stability
        self.a = 3.9
        self.b = 0.1
        self.c = 0.05
        
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Chaotic map component for dynamic landscape modulation
        chaotic = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic += self.a * x_scaled[i] * (1 - x_scaled[i])
            else:
                chaotic += self.a * x_scaled[i] * (1 - x_scaled[i]) + self.b * np.sin(2 * np.pi * x_scaled[i-1])
        
        # Exponential repulsion wells centered at regular grid points
        repulsion = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / self.dim) * 0.5
            width = 0.1 + 0.05 * np.cos(i)
            repulsion += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2) * (1 + 0.2 * np.sin(3 * x_scaled[i]))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        modulation = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4)
            amp = 0.5 + 0.3 * np.cos(i)
            modulation += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Gradient-based curvature with asymmetric hessian
        gradient_curvature = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x_scaled[i] - x_scaled[j]
                gradient_curvature += (dx**2) * np.exp(-0.5 * (dx**2)) * (i + j)
        
        # Combined chaotic and repulsion landscape with boundary penalty
        total = chaotic + repulsion + modulation + gradient_curvature
        
        # Add boundary avoidance with exponential penalty
        boundary_penalty = np.sum(np.exp(2 * np.abs(x_scaled)) - 1)
        
        return total + boundary_penalty