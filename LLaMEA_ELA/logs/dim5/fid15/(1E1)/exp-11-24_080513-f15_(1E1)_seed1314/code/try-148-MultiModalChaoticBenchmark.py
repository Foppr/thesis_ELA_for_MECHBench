import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(self.dim):
            min_dist = float('inf')
            for center in centers:
                dist = abs(x_normalized[i] - center)
                if dist < min_dist:
                    min_dist = dist
            rbf += np.exp(-5 * min_dist**2)
        
        # Sine-cosine chaotic modulation with varying frequency
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * 0.5)
            chaotic += np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i])
        
        # Adaptive conditioning based on dimension index
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 2.0 * np.sin(i * 0.3) + 0.5 * np.cos(i * 0.7)
            conditioning += cond_factor * x_normalized[i]**4
        
        # Multi-modal interaction with exponential decay
        modal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 2.0)
                modal += weight * np.sin(5 * (x_normalized[i] + x_normalized[j]))**2
        
        # Asymmetric penalty for boundary regions
        boundary = 0.0
        for i in range(self.dim):
            if abs(x_normalized[i]) > 0.9:
                boundary += 10 * (abs(x_normalized[i]) - 0.9)**2
        
        # Combined fitness with dynamic weighting
        return 0.4 * rbf + 0.3 * chaotic + 0.2 * conditioning + 0.08 * modal + 0.02 * boundary