import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with logarithmic spiral structure
        r = np.sqrt(np.sum(x**2) / self.dim)
        theta = np.arctan2(x[1], x[0]) if self.dim > 1 else 0.0
        spiral = np.sin(5.0 * r + 3.0 * theta) * np.exp(-0.1 * r)
        
        # Radial basis functions with varying scales and positions
        rbfs = 0.0
        centers = np.linspace(-4, 4, 7)
        for i in range(len(centers)):
            for j in range(len(centers)):
                if self.dim > 1:
                    dist = np.sqrt((x[0] - centers[i])**2 + (x[1] - centers[j])**2)
                    rbfs += np.exp(-0.5 * (dist / 1.5)**2)
                else:
                    dist = np.abs(x[0] - centers[i])
                    rbfs += np.exp(-0.5 * (dist / 1.5)**2)
        
        # Multi-scale Gaussian peaks with varying amplitudes and widths
        peaks = 0.0
        scales = [0.5, 1.0, 1.5, 2.0]
        amplitudes = [2.0, 1.5, 1.0, 0.5]
        for i in range(len(scales)):
            for j in range(len(amplitudes)):
                if self.dim > 1:
                    peaks += amplitudes[i] * np.exp(-0.5 * ((x[0] - 2.0)**2 / scales[i]**2 + (x[1] - 2.0)**2 / scales[j]**2))
                else:
                    peaks += amplitudes[i] * np.exp(-0.5 * (x[0] - 2.0)**2 / scales[i]**2)
        
        # Logarithmic scaling with fractal-like self-similarity
        log_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(10.0 * x))
        
        # Cross-dimensional coupling with harmonic interference
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.sin(x[i] * x[i+1]) * np.cos(0.5 * (x[i] + x[i+1]))
        
        # Combine all components
        return 0.3 * r + 0.4 * spiral + 0.2 * rbfs + 0.3 * peaks + 0.1 * log_term + 0.2 * coupling