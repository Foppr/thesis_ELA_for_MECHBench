import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component with dimensionally dependent frequencies
        quantum = 0.0
        for i in range(self.dim):
            freq = 1.2 + 0.4 * np.sin(0.5 * x[i]) + 0.3 * np.cos(0.7 * x[i])
            quantum += 0.5 * freq * x[i]**2 + 0.4 * np.sin(freq * x[i])
        
        # Adaptive fractal landscape with self-similar structures
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.6 * np.sin(0.4 * x[i])
            fractal += scale * np.sin(2.5 * x[i]) * np.cos(2.0 * x[i])
        
        # Multi-scale Gaussian peaks with dynamic positioning
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -4.0 + 2.5 * j  # Slightly shifted centers
                variance = 0.9 + 0.3 * np.sin(0.6 * x[i])
                amplitude = 1.2 + 0.6 * np.cos(0.5 * x[i])
                gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional coupling with nonlinear interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i]**3 + x[j]**3) * np.sin(0.3 * (x[i] - x[j]))
        
        # Dynamic saddle-point structure with chaotic modulation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.6 + 0.4 * np.sin(0.8 * x[i])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Combined function with dimensionally adaptive weights
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        return (0.3 * quantum + 0.35 * fractal + 0.25 * gaussian_peaks + 
                0.1 * coupling + 0.05 * saddle) * dim_factor