import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimensions and spectral parameters
        self.fractal_dim = 1.5 + 0.5 * np.random.rand()
        self.spectral_freqs = 2.0 + 3.0 * np.random.rand(dim)
        self.gauss_components = min(5, max(2, dim // 4))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity component with power-law scaling
        fractal = 0.0
        for i in range(self.dim):
            # Power-law interaction with previous dimensions
            scale_factor = 1.0 / (1.0 + np.abs(x[i]))
            fractal += scale_factor * np.sin(self.spectral_freqs[i] * x[i])**2
        
        # Spectral decomposition using discrete cosine transform-like interactions
        spectral = 0.0
        for i in range(self.dim):
            freq_term = 0.0
            for k in range(1, min(6, self.dim)):
                freq_term += np.cos(k * np.pi * x[i] / 5.0) * np.sin(k * x[i])
            spectral += freq_term**2
            
        # Gaussian mixture components with varying covariances
        gaussian = 0.0
        for i in range(self.gauss_components):
            mean = (i + 1) * 2.0 / self.gauss_components - 5.0
            variance = 0.5 + 0.5 * np.random.rand()
            gaussian += np.exp(-0.5 * ((x[0] - mean) / variance)**2)
            
        # Multi-scale coupling with exponentially decaying weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = np.exp(-0.1 * (j - i))
                coupling += weight * (x[i]**2 + x[j]**2) * np.cos(5.0 * (x[i] - x[j]))
                
        # Nonlinear transformation with chaotic-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(x[i])**3 + np.cos(x[i])**3 + 0.1 * np.sin(10.0 * x[i])
            
        # Adaptive scaling based on problem dimensionality
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return scale_factor * (0.25 * fractal + 0.2 * spectral + 0.15 * gaussian + 
                              0.3 * coupling + 0.1 * chaotic)