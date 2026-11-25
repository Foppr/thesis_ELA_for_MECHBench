import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced trigonometric component with interference patterns
        trig = np.sum(np.sin(5.0 * np.pi * x_norm) * np.cos(3.0 * np.pi * x_norm))
        
        # Adaptive exponential decay terms with varying rates
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += np.exp(-5.0 * np.abs(x_norm[i]) ** 1.5) * np.sin(2.0 * np.pi * x_norm[i])
        
        # Gaussian peaks with adaptive widths and positions
        gaussian = 0.0
        centers = np.linspace(-0.7, 0.7, min(7, self.dim))
        widths = np.linspace(0.1, 0.5, min(7, self.dim))
        for i in range(min(7, self.dim)):
            if i < len(centers):
                gaussian += np.exp(-0.5 * ((x_norm[i] - centers[i]) / widths[i]) ** 2)
        
        # Novel cross-dimensional interaction terms with radial symmetry
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross += (np.sin(10.0 * dist) + 1.0) / (1.0 + dist ** 2)
        
        # Polynomial terms with mixed degrees and adaptive weights
        poly = 0.0
        degrees = [2, 3, 4, 5]
        for i in range(min(len(degrees), self.dim)):
            poly += (x_norm[i] ** degrees[i]) / (1.0 + np.abs(x_norm[i]))
        
        # Combine all components with optimized weights
        return 0.3 * trig + 0.25 * exp_decay + 0.2 * gaussian + 0.15 * cross + 0.1 * poly