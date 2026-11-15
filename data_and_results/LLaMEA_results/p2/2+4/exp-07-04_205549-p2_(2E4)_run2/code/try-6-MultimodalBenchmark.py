import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic basin term - global minimum at origin
        quadratic = np.sum(x_normalized**2)
        
        # Sinusoidal perturbations with exponential decay
        sinusoidal = 0.0
        for i in range(self.dim):
            # Exponentially decaying amplitude
            amplitude = np.exp(-0.5 * np.sum(x_normalized**2))
            # Sinusoidal component with varying frequency
            sinusoidal += amplitude * np.sin(3 * np.pi * x_normalized[i]) * np.cos(2 * np.pi * x_normalized[i])
        
        # Central repulsion term to create local minima
        repulsion = 0.0
        distance_from_origin = np.sqrt(np.sum(x_normalized**2))
        if distance_from_origin > 0:
            repulsion = 2.0 * np.exp(-distance_from_origin**2 / 0.5)
        
        # Add a fourth-order polynomial term for additional complexity
        polynomial = 0.0
        for i in range(self.dim):
            polynomial += 0.2 * x_normalized[i]**4
        
        return quadratic + sinusoidal + repulsion + polynomial