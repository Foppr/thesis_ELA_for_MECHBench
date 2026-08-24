import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic gradient modulation with sinusoidal perturbations
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale harmonic modulation with varying frequencies
        harmonic = 0
        for i in range(self.dim):
            freq1 = 2 + 3 * np.sin(0.5 * x[i])
            freq2 = 5 + 2 * np.cos(0.3 * x[i])
            harmonic += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Saddle-point structure with cross-terms
        saddle = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            saddle += (x[i]**3 - 3 * x[i]) * (x[j]**3 - 3 * x[j])
        
        # Periodic attractor component with dynamic centers
        attractor = 0
        for i in range(self.dim):
            center = 2 * np.sin(0.4 * i)
            attractor += np.exp(-0.5 * (x[i] - center)**2) * np.sin(3 * (x[i] - center))
        
        # Multi-scale fractal-like structure
        fractal = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(2 * x[i])
            fractal += scale * np.sin(15 * x[i]) * np.cos(10 * x[i])
        
        # Combined weighted function
        return 0.25 * quadratic + 0.3 * chaotic + 0.2 * harmonic + 0.15 * saddle + 0.1 * attractor + 0.05 * fractal