import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced nested sinusoidal waves with chaotic modulation
        nested_waves = 0.0
        for i in range(1, min(8, self.dim + 1)):
            freq = i * (1.0 + 0.3 * np.sin(i * 0.7))
            amp = 1.0 / (i * (1.0 + 0.2 * np.cos(i * 0.4)))
            nested_waves += amp * np.sin(freq * x_scaled[i-1]) * np.cos(freq * x_scaled[i-1])
        
        # Chaotic polynomial chaos with non-uniform exponents
        poly_chaos = 0.0
        for i in range(1, min(6, self.dim + 1)):
            exp = 2 * i + np.sin(i * 0.5)
            poly_chaos += (i * 0.3) * (x_scaled[i-1] ** exp)
        
        # Long-range cross-dimensional interactions with inverse distance weighting
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Limited range to increase complexity
                dist = np.abs(x_scaled[i] - x_scaled[j])
                weight = 1.0 / (1.0 + dist**2)
                cross_interaction += weight * np.sin(5 * (x_scaled[i] + x_scaled[j]))
        
        # Fractal-like scaling with recursive sinusoidal modulation and phase shifts
        fractal_component = 0.0
        for i in range(min(5, self.dim)):
            scale_factor = 3 ** (i + 1)
            phase_shift = np.sin(i * 0.6)
            fractal_component += np.sin(scale_factor * x_scaled[i] + phase_shift) * np.cos(scale_factor * x_scaled[i] + phase_shift)
        
        # Complex ridge structure with multi-scale Gaussian modulation
        ridge = 0.0
        for i in range(self.dim):
            ridge += (x_scaled[i] ** 2) * np.exp(-0.3 * (x_scaled[i] ** 2)) * np.sin(2 * x_scaled[i])
        
        # Add a significant random noise component with multi-frequency modulation
        noise = 0.005 * np.sum(np.sin(100 * x_scaled) * np.cos(98 * x_scaled) + np.sin(75 * x_scaled))
        
        # Non-linear scaling and higher-order polynomial terms for increased ruggedness
        high_order = 0.002 * np.sum(x_scaled**8)
        
        # Combine all components with carefully tuned weights
        return nested_waves + 0.4 * poly_chaos + 0.3 * cross_interaction + 0.15 * fractal_component + 0.08 * ridge + noise + high_order + 0.001 * np.sum(np.abs(x_scaled)**7)