import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal modulation with varying frequencies
        chaotic = 0
        for i in range(self.dim):
            freq = 2 * (i + 1) / self.dim
            chaotic += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) + np.sin(freq * x[i] * 3)
        
        # Polynomial coupling with exponential barriers
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                coupling += (x[i]**3 + x[j]**3) * np.exp(-dist) * np.sin(2 * x[i] * x[j])
        
        # Modulated cubic polynomial with sinusoidal perturbations
        polynomial = 0
        for i in range(self.dim):
            polynomial += (x[i]**3 - 3 * x[i]) * np.cos(0.5 * x[i]) + 0.5 * np.sin(4 * x[i])
        
        # Exponential barrier terms to create rugged landscape
        barriers = 0
        for i in range(self.dim):
            barriers += np.exp(-0.5 * (x[i] - 2)**2) + np.exp(-0.5 * (x[i] + 2)**2) + np.exp(-0.3 * x[i]**2)
        
        # Multi-scale sinusoidal interference
        interference = 0
        for i in range(self.dim):
            interference += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
        
        # Combine all components with adaptive weights
        return (quadratic + 0.8 * chaotic + 0.6 * coupling + 0.4 * polynomial + 
                0.3 * barriers + 0.5 * interference + 10 * np.sum(np.sin(x)**2))