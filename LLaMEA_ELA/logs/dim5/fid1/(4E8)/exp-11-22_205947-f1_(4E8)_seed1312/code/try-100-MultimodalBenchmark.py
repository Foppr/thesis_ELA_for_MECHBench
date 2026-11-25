import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial conditioning with varying exponents
        poly_term = np.sum((x ** 2) + 0.1 * (x ** 3) + 0.01 * (x ** 4))
        
        # Radial sinusoidal component with multiple frequencies and centers
        radial_sine = 0.0
        for i in range(self.dim):
            radial_sine += np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + \
                          np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) + \
                          np.sin(11.0 * x[i]) * np.cos(13.0 * x[i])
        
        # Multi-scale radial basis with varying widths and offsets
        rbfs = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.5 * np.sin(i * 0.5)
            offset = 2.0 * np.cos(i * 0.3)
            rbfs += np.exp(-0.5 * ((x[i] - offset) / width) ** 2)
        
        # Cross-dimensional coupling with trigonometric interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                cross_coupling += np.sin(x[i] + x[j]) * np.cos(2.0 * (x[i] - x[j]))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.5)
        
        # Final combination with scaling and modulation
        return condition_factor * (poly_term + 0.3 * radial_sine + 0.2 * rbfs + 0.15 * cross_coupling)