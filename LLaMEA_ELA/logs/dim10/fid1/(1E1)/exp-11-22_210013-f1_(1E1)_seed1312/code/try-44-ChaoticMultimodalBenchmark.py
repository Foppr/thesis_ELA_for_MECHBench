import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal base with varying frequencies
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i]) * np.cos(7 * x[i])
            chaotic += 0.5 * np.sin(15 * x[i]) * np.cos(12 * x[i])
        
        # Polynomial cross-dimensional interactions with exponential scaling
        polynomial = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            polynomial += 0.3 * x[i]**3 * np.exp(-0.1 * x[j]**2)
            polynomial += 0.2 * x[i]**2 * x[k] * np.exp(-0.05 * (x[j] - x[k])**2)
        
        # Exponential decay with multi-modal oscillations
        exponential = 0.0
        for i in range(self.dim):
            exponential += 0.4 * np.exp(-0.5 * (x[i] - 1)**2) * np.sin(8 * x[i])
            exponential += 0.3 * np.exp(-0.3 * (x[i] + 2)**2) * np.cos(6 * x[i])
        
        # Non-separable high-dimensional structure with chaotic phase shifts
        nonsep = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 3) % self.dim
            nonsep += 0.25 * np.sin(5 * x[i] + 2 * x[j]) * np.cos(4 * x[k])
            nonsep += 0.15 * np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(9 * x[k])
        
        # High-frequency noise with chaotic amplitude modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(50 * x[i]) * np.cos(45 * x[(i + 1) % self.dim])
            noise += 0.05 * np.sin(30 * x[i]) * np.exp(-0.1 * x[(i + 2) % self.dim]**2)
        
        # Combine all components with adaptive weights
        return 1.2 * chaotic + 1.0 * polynomial + 0.8 * exponential + 1.1 * nonsep + 0.5 * noise