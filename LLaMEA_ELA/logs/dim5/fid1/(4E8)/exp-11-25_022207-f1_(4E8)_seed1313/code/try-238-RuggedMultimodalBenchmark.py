import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay potential wells with varying depths and widths
        potentials = np.sum(0.5 * np.exp(-0.5 * (x_norm**2)) * (1.0 + 0.3 * np.sin(3.0 * x_norm)))
        
        # Trigonometric wave interference creating complex landscape patterns
        waves = np.sum(np.sin(2.0 * np.pi * x_norm) * np.cos(1.5 * np.pi * x_norm) * 
                      np.exp(-0.2 * np.abs(x_norm)) * (1.0 + 0.2 * np.cos(4.0 * x_norm)))
        
        # Adaptive dimensional coupling with varying interaction strengths
        coupling = 0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**2.5 + x_norm[i+1]**2.5) * np.exp(-0.3 * (x_norm[i] - x_norm[i+1])**2) * \
                       np.sin(2.0 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Multi-scale Gaussian ridges with dynamic amplitude modulation
        ridges = 0
        for i in range(3):
            scale = 0.3 + 0.4 * i
            amp = 1.5 + 0.5 * np.sin(i * 1.2)
            ridges += amp * np.exp(-0.5 * ((x_norm - 0.5 * i) / scale)**2)
        
        # Saddle-point perturbation with dynamic frequency and amplitude
        saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2) * 
                       np.exp(-0.4 * (x_norm[:-1] + x_norm[1:])**2) * 
                       np.cos(3.0 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Fractal-like dimension scaling with recursive pattern
        fractal = 0
        for i in range(1, min(4, self.dim)):
            fractal += np.sum(np.sin(i * 2.0 * np.pi * x_norm) * 
                            np.cos(i * 1.5 * np.pi * x_norm) * 
                            np.exp(-0.1 * np.abs(x_norm)))
        
        # Combined function with asymmetric gradient characteristics
        result = potentials + waves + coupling + ridges + saddle + fractal
        
        # Add controlled noise for robustness and challenge
        noise = 0.02 * np.random.randn() * (1.0 + 0.1 * np.std(x_norm))
        
        return result + noise