import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logarithmic spiral gradient component with adaptive frequencies
        spiral = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[i], x[(i+1) % self.dim])
            radius = np.sqrt(x[i]**2 + x[(i+1) % self.dim]**2)
            freq = 2.0 + 0.8 * np.sin(0.3 * x[i])
            spiral += radius * np.sin(freq * angle + 0.5 * radius)
        
        # Quantum harmonic oscillator potential with position-dependent frequency
        quantum = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.3 * np.cos(0.2 * x[i])
            quantum += 0.5 * freq * (x[i]**2) + 0.3 * (np.sin(x[i])**2)
        
        # Multi-scale Gaussian peaks with asymmetric shapes and varying heights
        gaussian_peaks = 0.0
        scales = [0.1, 0.3, 1.0, 3.0]
        for scale in scales:
            for i in range(self.dim):
                center = 2.0 * np.sin(scale * x[i]) + 0.5 * np.cos(2 * scale * x[i])
                width = 0.15 + 0.7 * np.exp(-scale)
                # Asymmetric Gaussian peak
                asymmetry = 0.3 * np.sin(1.5 * x[i])
                gaussian_peaks += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(scale * x[i]) * (1 + asymmetry)
        
        # Logarithmic barrier penalties with boundary sensitivity
        log_barrier = 0.0
        for i in range(self.dim):
            dist_from_boundary = min(5.0 - np.abs(x[i]), 0.1)
            log_barrier += -np.log(dist_from_boundary + 1e-8) * (1.0 + 0.2 * np.sin(0.5 * x[i]))
        
        # Fractal self-similarity through recursive dimension coupling with nonlinear interaction
        fractal = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                interaction = np.sin(x[i] * x[i+1]) * np.exp(-0.15 * (x[i] - x[i+1])**2)
                fractal += interaction * (1.0 + 0.1 * np.sin(2 * x[i]))
        
        # Combined fitness function with dynamic weighting
        return 0.35 * spiral + 0.3 * quantum + 0.25 * gaussian_peaks + 0.07 * log_barrier + 0.03 * fractal