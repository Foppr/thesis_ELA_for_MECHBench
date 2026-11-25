import numpy as np

class FractalMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial base with varying degrees
        polynomial = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 4)
            polynomial += (x_normalized[i] ** degree) * (1.0 + 0.5 * np.sin(i))
        
        # Trigonometric component with fractal-like frequency modulation
        trigonometric = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 3) * (1.0 + 0.3 * np.cos(i))
            trigonometric += np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.5)
        
        # Logarithmic barrier component for boundary sensitivity
        logarithmic = 0.0
        for i in range(self.dim):
            if abs(x_normalized[i]) < 0.1:
                logarithmic += 10.0 * (0.1 - abs(x_normalized[i])) ** 2
            else:
                logarithmic += np.log(1.0 + abs(x_normalized[i]))
        
        # Multi-scale interaction terms with fractal coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                coupling = 1.0 / (1.0 + dist ** 2)
                interaction += coupling * np.sin(5 * (x_normalized[i] + x_normalized[j])) * np.cos(3 * (x_normalized[i] - x_normalized[j]))
        
        # Saddle point structure with hyperbolic functions
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.tanh(x_normalized[i]) * (x_normalized[i] ** 2) * np.sin(x_normalized[i])
        
        # Multi-modal component with Gaussian peaks
        multimodal = 0.0
        peak_centers = np.linspace(-1, 1, 5)
        for i in range(self.dim):
            min_dist = float('inf')
            for center in peak_centers:
                dist = abs(x_normalized[i] - center)
                if dist < min_dist:
                    min_dist = dist
            multimodal += np.exp(-5.0 * min_dist ** 2)
        
        # Combined fitness function with dynamic weighting
        return (0.3 * polynomial + 0.25 * trigonometric + 0.15 * logarithmic + 
                0.15 * interaction + 0.1 * saddle + 0.05 * multimodal)