import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic spiral gradient component
        spiral = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[i], x[(i+1) % self.dim])
            radius = np.sqrt(x[i]**2 + x[(i+1) % self.dim]**2)
            spiral += radius * np.sin(3 * angle + 0.5 * radius)
        
        # Quantum harmonic oscillator potential
        quantum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.1 * x[i])
            quantum += 0.5 * freq * (x[i]**2) + 0.25 * (np.cos(x[i])**2)
        
        # Multi-scale Gaussian peaks with varying widths and heights
        gaussian_peaks = 0.0
        scales = [0.1, 0.3, 1.0, 3.0]
        for scale in scales:
            for i in range(self.dim):
                center = 2.5 * np.sin(scale * x[i])
                width = 0.2 + 0.8 * np.exp(-scale)
                gaussian_peaks += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(scale * x[i])
        
        # Logarithmic barrier penalties
        log_barrier = 0.0
        for i in range(self.dim):
            dist_from_boundary = min(5.0 - np.abs(x[i]), 0.1)
            log_barrier += -np.log(dist_from_boundary + 1e-8)
        
        # Fractal self-similarity through recursive dimension coupling
        fractal = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                fractal += np.sin(x[i] * x[i+1]) * np.exp(-0.1 * (x[i] - x[i+1])**2)
        
        # Combined fitness function with dynamic weighting
        return 0.4 * spiral + 0.3 * quantum + 0.2 * gaussian_peaks + 0.08 * log_barrier + 0.02 * fractal