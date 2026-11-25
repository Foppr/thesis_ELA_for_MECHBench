import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Layer 1: Sinusoidal base with varying frequencies and amplitudes
        layer1 = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.2 * np.sin(0.5 * i))
            amp = 1.0 / (1.0 + 0.1 * i)
            layer1 += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Layer 2: Non-separable cross-terms with exponential weighting
        layer2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                layer2 += weight * np.sin(4 * x_scaled[i] * x_scaled[j]) * np.cos(2 * x_scaled[i] * x_scaled[j])
        
        # Layer 3: Polynomial with adaptive conditioning
        layer3 = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.sin(0.3 * i)
            layer3 += cond_factor * (x_scaled[i]**4 + x_scaled[i]**2)
        
        # Layer 4: Hybrid interaction with trigonometric and polynomial components
        layer4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = np.sin(3 * x_scaled[i]) * np.cos(3 * x_scaled[j]) + (x_scaled[i]**2 + x_scaled[j]**2)
                layer4 += term * np.exp(-0.3 * (x_scaled[i] - x_scaled[j])**2)
        
        # Combine layers with dynamic weights
        return 3.0 * layer1 + 2.5 * layer2 + 2.0 * layer3 + 1.5 * layer4