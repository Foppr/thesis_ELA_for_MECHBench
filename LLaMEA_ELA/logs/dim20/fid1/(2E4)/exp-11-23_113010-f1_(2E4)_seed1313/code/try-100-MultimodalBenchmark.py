import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial potential with chaotic coefficients
        poly_potential = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm) + 0.05 * np.cos(15 * x_norm))**3)
        
        # Sinusoidal waves with varying frequencies and amplitudes
        sin_waves = np.sum(np.sin(2**(np.arange(self.dim) + 1) * np.pi * x_norm) * 
                          np.cos(3**(np.arange(self.dim) + 1) * np.pi * x_norm))
        
        # Cross-dimensional interactions with chaotic coupling coefficients
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin((i + 1) * (j + 1)) * np.cos((i + 1) * (j + 1))
                cross_terms += coupling * (x_norm[i]**3 + x_norm[j]**3) * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Fractal-like irregularities using iterative chaotic maps
        fractal_irregularity = 0.0
        for i in range(self.dim):
            val = x_norm[i]
            for _ in range(5):
                val = np.sin(10 * val) + 0.1 * np.cos(20 * val)
            fractal_irregularity += val**2
        
        # Adaptive noise with dynamic amplitude and frequency
        noise_amp = 0.02 * (1 + np.sin(np.sum(x_norm**2))) * np.log(self.dim + 1)
        noise_freq = 2**(self.dim // 2 + 1) * (1 + np.cos(np.sum(x_norm)))
        noise = noise_amp * np.random.random() * np.sin(noise_freq * np.pi * np.sum(x_norm**2))
        
        # Scaling factor based on dimensionality and chaotic behavior
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1) * (1 + np.sin(np.sum(x_norm)))
        
        return scale_factor * (poly_potential + 0.5 * sin_waves + 0.3 * cross_terms + 0.4 * fractal_irregularity + noise)