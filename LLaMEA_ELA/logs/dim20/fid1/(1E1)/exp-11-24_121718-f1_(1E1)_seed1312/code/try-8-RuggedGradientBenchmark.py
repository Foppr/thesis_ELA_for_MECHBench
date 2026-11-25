import numpy as np

class RuggedGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with varying weights
        quadratic = np.sum(x**2) / self.dim
        
        # Sinusoidal modulation with exponentially decaying amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            amplitude = np.exp(-0.1 * i)
            sinusoidal += amplitude * np.sin(5 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Exponentially decaying gradient landscape with saddle points
        gradient = 0.0
        for i in range(self.dim):
            gradient += np.exp(-0.2 * np.abs(x[i])) * np.sin(2 * np.pi * x[i]) * np.cos(4 * np.pi * x[i])
        
        # Saddle-point structure with multiple intersecting hyperplanes
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                saddle += (x[i] - x[j])**2 * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Combine all components with different scaling factors
        return quadratic + 0.6 * sinusoidal + 0.4 * gradient + 0.3 * saddle