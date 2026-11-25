import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.sin(3 * r) * np.exp(-0.5 * r**2)
        
        # Multi-modal sinusoidal terms with varying frequencies
        modal_terms = []
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            modal_terms.append(np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i]))
        
        modal = np.sum(modal_terms)
        
        # Cross-dimensional coupling with adaptive scaling
        coupling = 0.0
        for i in range(self.dim - 1):
            scale_factor = 1.0 / (1.0 + 0.1 * np.abs(x_scaled[i]) + 0.2 * np.abs(x_scaled[i+1]))
            coupling += scale_factor * np.sin(5 * (x_scaled[i] - x_scaled[i+1])) * np.cos(3 * (x_scaled[i] + x_scaled[i+1]))
        
        # Adaptive dimensionality scaling
        dim_scaling = 0.0
        for i in range(self.dim):
            dim_scaling += (i + 1) * np.sin(2 * x_scaled[i])**2
        
        # Fractal-like self-similarity component
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(7 * x_scaled[i] * (1 + 0.1 * i)) * np.cos(4 * x_scaled[i] * (1 + 0.05 * i))
        
        # Combined function with weighted components
        return 0.3 * radial + 0.4 * modal + 0.2 * coupling + 0.1 * dim_scaling + 0.05 * fractal