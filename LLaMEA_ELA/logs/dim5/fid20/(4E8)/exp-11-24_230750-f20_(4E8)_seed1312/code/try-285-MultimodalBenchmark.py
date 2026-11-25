import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quantum harmonic oscillator with chaotic frequency modulation
        quantum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.4 * np.sin(0.5 * x[i]) + 0.3 * np.cos(0.7 * x[i]) + 0.2 * np.sin(0.3 * x[i]**2)
            quantum += 0.5 * freq * x[i]**2 + 0.4 * np.sin(freq * x[i])
        
        # Adaptive fractal landscape with dynamic scaling and rotation
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.6 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i])
            fractal += scale * np.sin(2.5 * x[i]) * np.cos(1.8 * x[i])
        
        # Multi-scale Gaussian peaks with time-varying parameters and cross-dimensional interaction
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(4):
                center = -4.0 + 2.0 * j
                variance = 0.9 + 0.3 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
                amplitude = 1.2 + 0.4 * np.cos(0.5 * x[i]) + 0.3 * np.sin(0.8 * x[i]**2)
                gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional coupling with enhanced nonlinear interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling range
                coupling += (x[i]**4 + x[j]**4) * np.sin(0.3 * (x[i] - x[j])) * np.cos(0.2 * (x[i] + x[j]))
        
        # Dynamic saddle-point structure with enhanced chaotic modulation and dimensionally adaptive components
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.6 + 0.4 * np.sin(0.8 * x[i]) * np.cos(0.5 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Additional chaotic modulation component for increased complexity
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.3 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.sin(0.5 * x[i]**3)
        
        # Combined function with improved dimensionally adaptive weights and scaling
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        return (0.2 * quantum + 0.25 * fractal + 0.25 * gaussian_peaks + 
                0.15 * coupling + 0.1 * saddle + 0.05 * chaos) * dim_factor