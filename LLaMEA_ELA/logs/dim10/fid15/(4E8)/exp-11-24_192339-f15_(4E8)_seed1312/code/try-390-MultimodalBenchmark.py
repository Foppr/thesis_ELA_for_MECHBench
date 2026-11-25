import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with sine-wave modulation
        chaotic_grad = 0
        for i in range(self.dim):
            chaotic_grad += np.sin(x[i] * np.pi * (1 + 0.5 * np.sin(3 * x[i]))) * np.cos(2 * x[i])
        
        # Dynamic curvature modulation based on dimension and position
        curvature = 0
        for i in range(self.dim):
            # Multi-scale harmonic interference
            scale_factor = 1.0 + 0.3 * np.sin(0.5 * x[i] + self.dim * 0.2)
            curvature += (x[i]**2) * scale_factor * np.exp(-0.1 * x[i]**2)
        
        # Saddle point structure with cross-dimensional coupling
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                saddle += (x[i] * x[j]) * np.sin(0.3 * (x[i]**2 + x[j]**2))
        
        # Multi-scale harmonic interference with dynamic phase
        harmonic = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.7 * x[i] + self.dim * 0.3)
            harmonic += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Combined landscape with dynamic weights
        weight1 = 0.4 + 0.2 * np.sin(self.dim * 0.1)
        weight2 = 0.3 + 0.2 * np.cos(self.dim * 0.15)
        weight3 = 0.3 + 0.2 * np.sin(self.dim * 0.2)
        
        return weight1 * chaotic_grad + weight2 * curvature + weight3 * saddle + 0.1 * harmonic