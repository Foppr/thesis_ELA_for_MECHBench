import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with adaptive scaling
        poly_base = np.sum(x**4) + 0.5 * np.sum(x**3) + 0.1 * np.sum(x**2)
        
        # Trigonometric components with varying frequencies and amplitudes
        trig_components = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi / 2.0
            trig_components += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.1 * np.abs(x[i]))
        
        # Radial basis function component with adaptive centers
        rbf = 0.0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                rbf += np.exp(-0.5 * np.sum((x - centers[i])**2)) * np.sin(2.0 * centers[i])
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * np.sin(x[i] * x[i+1])
        
        # Adaptive noise component with dimension-dependent scaling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 2)) * (1.0 / (i + 1))
        
        # Combine all components with dimension-adaptive weights
        result = poly_base + 0.5 * trig_components + 0.3 * rbf + 0.2 * coupling + 0.1 * noise
        
        return result