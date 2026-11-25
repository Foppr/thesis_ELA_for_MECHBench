import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Nested sinusoidal waves with varying amplitudes and frequencies
        nested_waves = 0.0
        for i in range(1, min(6, self.dim + 1)):
            freq = i * (1.0 + 0.2 * np.sin(i * 0.5))
            amp = 1.0 / (i * (1.0 + 0.1 * np.cos(i * 0.3)))
            nested_waves += amp * np.sin(freq * x_scaled[i-1]) * np.cos(freq * x_scaled[i-1])
        
        # Polynomial chaos component with increasing degree
        poly_chaos = 0.0
        for i in range(1, min(5, self.dim + 1)):
            poly_chaos += (i * 0.2) * (x_scaled[i-1] ** (2 * i))
        
        # Cross-dimensional interactions with exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                cross_interaction += np.exp(-dist) * np.sin(3 * (x_scaled[i] + x_scaled[j]))
        
        # Fractal-like scaling with recursive sinusoidal modulation
        fractal_component = 0.0
        for i in range(min(4, self.dim)):
            scale_factor = 2 ** (i + 1)
            fractal_component += np.sin(scale_factor * x_scaled[i]) * np.cos(scale_factor * x_scaled[i])
        
        # Asymmetric ridge structure with Gaussian modulation
        ridge = 0.0
        for i in range(self.dim):
            ridge += (x_scaled[i] ** 2) * np.exp(-0.5 * (x_scaled[i] ** 2))
        
        # Add a small random noise component to increase ruggedness
        noise = 0.001 * np.sum(np.sin(50 * x_scaled) * np.cos(48 * x_scaled))
        
        # Combine all components with carefully tuned weights
        return nested_waves + 0.3 * poly_chaos + 0.2 * cross_interaction + 0.1 * fractal_component + 0.05 * ridge + noise + 0.001 * np.sum(x_scaled**6)