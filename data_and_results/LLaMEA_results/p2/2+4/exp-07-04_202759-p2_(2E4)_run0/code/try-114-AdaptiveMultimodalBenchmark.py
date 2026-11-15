import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scaling factors for each dimension
        self.scaling = np.linspace(1.0, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with adaptive scaling
        poly = np.sum(self.scaling * x**6)
        
        # Sinusoidal component with dynamic frequencies and amplitudes
        sin_comp = 0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(x[i] * 0.5)
            amp = 2.0 + 1.5 * np.cos(x[i] * 0.3)
            sin_comp += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Radial basis function with adaptive centers and widths
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(15, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = 0.5 + 0.3 * np.sin(0.4 * i)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.sin(8 * (x[i] - center))
        
        # Coupling term with dynamic interaction weights
        coupling = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            weight = 1.0 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
            coupling += weight * np.sin(3 * (x[i] - x[j])) * np.cos(2 * (x[i] + x[j]))
        
        # Cross-dimensional interaction with varying strength
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for non-separability
                cross += np.sin(5 * (x[i] * x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Adaptive conditioning through dimension-specific modulation
        cond = 0
        for i in range(self.dim):
            cond += (1 + 0.2 * np.sin(2 * x[i])) * x[i]**4
        
        # Combine all components with dynamic weights
        return 0.25 * poly + 0.30 * sin_comp + 0.20 * rbf + 0.15 * coupling + 0.08 * cross + 0.02 * cond