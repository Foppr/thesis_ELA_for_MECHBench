import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal component with recursive structure
        fractal = 0.0
        for i in range(1, 6):
            scale = 2 ** i
            fractal += np.sum(np.sin(scale * np.pi * x_norm) * np.exp(-0.5 * scale * np.abs(x_norm)))
        
        # Exponential barrier regions to create rugged terrain
        barriers = np.sum(np.exp(5 * np.abs(x_norm)) * np.sin(3 * np.pi * x_norm)**2)
        
        # Gradient-dependent conditioning with varying curvature
        conditioning = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                conditioning += (x_norm[i]**2 + x_norm[i+1]**2) * np.exp(-0.1 * (x_norm[i] - x_norm[i+1])**2)
        
        # Multi-scale sinusoidal peaks with varying amplitudes and frequencies
        peaks = 0.0
        for i in range(1, 11):
            freq = i * 3
            amp = 1.0 / i
            peaks += amp * np.sum(np.sin(freq * np.pi * x_norm) * np.cos(freq * np.pi * x_norm**2))
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x_norm[i] * x_norm[j])**3
        
        # Asymmetric exponential decay to create directional bias
        asymmetry = np.sum(np.exp(-2 * np.abs(x_norm)) * np.sin(2 * np.pi * x_norm)**3)
        
        # Combine all components
        result = 0.2 * fractal + 0.3 * barriers + 0.15 * conditioning + 0.25 * peaks + 0.05 * coupling + 0.05 * asymmetry
        
        # Add noise with amplitude dependent on function value
        noise = 0.01 * (1 + np.abs(result)) * np.random.uniform(-1, 1)
        
        return result + noise