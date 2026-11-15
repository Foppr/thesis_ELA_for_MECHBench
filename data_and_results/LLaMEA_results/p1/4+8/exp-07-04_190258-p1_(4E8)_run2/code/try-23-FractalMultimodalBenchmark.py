import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Fractal-like exponential interactions
        fractal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                fractal += np.exp(-distance) * np.sin(2 * np.pi * distance)
        
        # Trigonometric basin structure with varying frequencies
        basin = 0
        for i in range(self.dim):
            basin += np.sin(0.5 * x[i])**2 * np.cos(0.3 * x[i])**2
        
        # Multi-scale harmonic perturbations
        harmonic = 0
        for i in range(self.dim):
            harmonic += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Cross-term coupling with varying weights
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.05 * x[i] * x[j] * np.cos(0.2 * (x[i]**2 + x[j]**2))
        
        return quadratic + fractal + basin + harmonic + cross