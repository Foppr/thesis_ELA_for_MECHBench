import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component with varying frequencies
        quantum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.4 * x[i])
            quantum += 0.5 * freq * x[i]**2 + 0.3 * np.cos(freq * x[i])
        
        # Adaptive fractal landscape with multi-scale Gaussian peaks
        fractal = 0.0
        scales = [0.5, 1.0, 2.0]
        for i in range(self.dim):
            for scale in scales:
                center = -3.0 + 6.0 * np.random.rand()
                variance = 0.2 + 0.4 * np.sin(0.3 * x[i])
                fractal += 0.3 * np.exp(-0.5 * ((x[i] - center) / variance)**2) * scale
        
        # Dynamic multi-scale Gaussian mixture with varying amplitudes
        gaussian_mixture = 0.0
        for i in range(self.dim):
            amp = 0.8 + 0.4 * np.cos(0.5 * x[i])
            for j in range(3):
                center = -4.0 + 8.0 * np.random.rand()
                variance = 0.3 + 0.2 * np.sin(0.2 * x[i])
                gaussian_mixture += amp * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional coupling with sine-wave interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                coupling += np.sin(0.3 * x[i]) * np.cos(0.2 * x[j]) * (x[i] + x[j])**2
        
        # Saddle-point structure with asymmetric components
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                saddle += (x[i]**3 - x[i+1]**3) * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i+1])
        
        # Boundary penalty and conditioning
        boundary = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                boundary += 10.0 * (abs(x[i]) - 4.5)**2
        
        # Combined function with dimensionally adaptive weights
        dim_factor = 1.0 + 0.05 * np.log(self.dim + 1)
        return (0.25 * quantum + 0.3 * fractal + 0.2 * gaussian_mixture + 
                0.15 * coupling + 0.05 * saddle + 0.05 * boundary) * dim_factor