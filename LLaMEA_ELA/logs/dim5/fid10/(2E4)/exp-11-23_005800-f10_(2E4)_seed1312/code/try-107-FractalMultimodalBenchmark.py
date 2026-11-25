import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 2.5
        self.amplitude = 3.0
        self.frequency = 4.0
        self.barrier_strength = 10.0
        self.roughness = 0.8
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal component using fractional Brownian motion-like approach
        fractal = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-scale sine waves with decreasing amplitude
            scale = 1.0
            for _ in range(5):
                fractal += scale * np.sin(self.frequency * xi) * np.cos(self.frequency * xi)
                scale *= self.roughness
                self.frequency *= 1.5
                
        # Chaotic modulation using logistic map
        chaotic_mod = 1.0
        log_map = 0.5
        for _ in range(10):
            log_map = 3.8 * log_map * (1 - log_map)
            chaotic_mod *= (1 + 0.1 * np.sin(log_map))
            
        # Exponential barrier terms to create rugged landscape
        barriers = 0.0
        for i in range(self.dim):
            barriers += self.barrier_strength * (np.exp(-((x[i] - 2.0)**2 / 2.0)) + 
                                                np.exp(-((x[i] + 2.0)**2 / 2.0)))
            
        # Polynomial coupling terms for increased conditioning
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                
        # Combine all components with scaling factor
        result = chaotic_mod * (self.amplitude * fractal + barriers + coupling)
        
        # Add noise and return
        return result + 0.01 * np.sum(x**4) + np.random.normal(0, 0.001)