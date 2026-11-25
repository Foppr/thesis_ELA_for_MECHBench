import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic fractal pattern with enhanced exponential coupling
        chaotic_fractal = 0.0
        for i in range(self.dim):
            chaotic_fractal += np.sin(np.exp(x[i] * 1.2)) * np.cos(np.exp(x[i] * 0.3)) * np.sin(x[i] ** 3.5)
        
        # Dynamic radial corridors with multi-scale sinusoidal modulation
        radial_corridors = 0.0
        for i in range(self.dim):
            radial_corridors += (x[i] ** 2) * np.sin(12 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
        
        # Mixed higher-order polynomial-trigonometric interactions with adaptive penalties
        poly_trig_interaction = 0.0
        for i in range(self.dim):
            poly_trig_interaction += (x[i] ** 4.2) * np.sin(x[i] * 1.1) * np.cos(x[i] ** 2.1) + (x[i] ** 3.1) * np.tan(x[i] * 0.6)
        
        # Adaptive penalty landscapes with modified exponential coupling terms
        adaptive_penalty = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                adaptive_penalty += np.exp(2.5 * (np.abs(x[i]) - 4.2)) * np.sin(3.5 * x[i])
            else:
                adaptive_penalty += 0.6 * (x[i] ** 2) * np.cos(2.1 * x[i]) + 0.12 * (x[i] ** 4)
        
        # Nested complex sinusoidal structures with varying frequencies
        nested_sine = 0.0
        for i in range(self.dim):
            freq_factor = 2.5 ** (i % 5)
            nested_sine += np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[i] * 0.8) * np.exp(-0.6 * x[i] ** 2)
        
        # Multi-scale Gaussian peaks with varying heights and widths
        gaussian_peaks = 0.0
        centers = np.linspace(-4.9, 4.9, 15)
        for center in centers:
            gaussian_peaks += np.exp(-0.5 * np.sum((x - center) ** 2) / (0.35 + 0.12 * np.abs(center))) * np.sin(3.2 * np.pi * np.sum((x - center) ** 2))
        
        # Cross-term exponential attraction basins with modified fractal scaling
        cross_attraction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j]) ** 2 + 1e-8)
                cross_attraction += np.exp(-dist * 1.2) * np.sin(5.5 * np.pi * dist) * (1.0 + 0.25 * np.sin(dist * 1.3))
        
        # Combined fitness with adjusted weights
        return 0.27 * chaotic_fractal + 0.22 * radial_corridors + 0.21 * poly_trig_interaction + 0.16 * adaptive_penalty + 0.11 * nested_sine + 0.12 * gaussian_peaks + cross_attraction