import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.hurst = 0.3 + 0.4 * np.random.rand()
        self.fractal_dim = 1.5 + 0.5 * np.random.rand()
        self.noise_level = 0.1 + 0.2 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal component with self-similar structure
        fractal = 0.0
        for i in range(self.dim):
            # Multi-scale sine waves with varying frequencies and amplitudes
            scale = 1.0 + 2.0 * np.sin(i * 0.5)
            freq = 2.0**((i % 4) + 1)
            amplitude = 1.0 + 0.5 * np.cos(i * 0.3)
            fractal += amplitude * np.sin(freq * x[i] / scale) * np.cos(freq * x[i] / (scale * 2))
        
        # Scale-dependent ruggedness with power-law behavior
        ruggedness = 0.0
        for i in range(self.dim):
            # Use a power-law scaling for different dimensions
            power = 1.0 + 0.5 * np.sin(i * 0.4)
            ruggedness += (x[i]**2) ** power
            
        # Multi-scale correlation structure
        correlation = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Correlation decreases with distance and dimension index
                dist = np.abs(x[i] - x[j])
                corr_factor = 1.0 / (1.0 + dist * (i + j + 1))
                correlation += corr_factor * np.sin(3.0 * (x[i] + x[j]))
                
        # Add noise with fractal characteristics
        noise = 0.0
        for i in range(self.dim):
            # Fractional Brownian motion-like noise
            noise += self.noise_level * np.sin(i * 1.7) * np.cos(i * 2.3) * np.sin(x[i] * 0.5)
            
        # Combine components with dimension-dependent weights
        weight_fractal = 0.4 + 0.1 * np.sin(self.dim * 0.3)
        weight_ruggedness = 0.3 + 0.1 * np.cos(self.dim * 0.2)
        weight_correlation = 0.2 + 0.05 * np.sin(self.dim * 0.4)
        weight_noise = 0.1
        
        # Add global minimum at origin with basin of attraction
        basin = np.sum(x**2) * 0.01
        
        return weight_fractal * fractal + weight_ruggedness * ruggedness + \
               weight_correlation * correlation + weight_noise * noise + basin