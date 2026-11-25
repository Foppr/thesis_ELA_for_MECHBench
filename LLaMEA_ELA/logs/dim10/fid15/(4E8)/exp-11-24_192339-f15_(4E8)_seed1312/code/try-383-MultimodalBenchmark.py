import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with dynamic degree
        chaos = 0
        for i in range(self.dim):
            degree = 2 + int(np.abs(x[i]) * 0.5) % 4
            poly_term = np.sum([np.power(x[i], k) for k in range(1, degree + 1)])
            chaos += poly_term * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function modulation with adaptive width
        rbf = 0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(self.dim):
            width = 0.5 + 0.3 * np.sin(0.3 * x[i])
            for center in centers:
                rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Dynamic hyperbolic tangent coupling
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                coupling += np.tanh(x[i]) * np.tanh(x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Multi-scale oscillatory components with frequency modulation
        oscillation = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.4 * x[i])
            scale = 1.0 + 0.2 * np.cos(0.6 * x[i])
            oscillation += scale * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Adaptive basin structure with sigmoidal transitions
        basin = 0
        for i in range(self.dim):
            transition = 1.0 / (1.0 + np.exp(-2.0 * (x[i] - 1.5)))
            basin += transition * (x[i]**4 - 2*x[i]**2 + 1)
        
        # Combine all components with optimized weights
        return 0.25 * chaos + 0.25 * rbf + 0.20 * coupling + 0.20 * oscillation + 0.10 * basin