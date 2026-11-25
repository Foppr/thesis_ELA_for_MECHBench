import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic fractal pattern with exponential coupling
        chaotic_fractal = 0.0
        for i in range(self.dim):
            chaotic_fractal += np.sin(np.exp(x[i])) * np.cos(np.exp(x[i] * 0.5)) * np.sin(x[i] ** 3)
        
        # Dynamic radial corridors with multi-scale sinusoidal modulation
        radial_corridors = 0.0
        for i in range(self.dim):
            radial_corridors += (x[i] ** 2) * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Mixed higher-order polynomial-trigonometric interactions with adaptive penalties
        poly_trig_interaction = 0.0
        for i in range(self.dim):
            poly_trig_interaction += (x[i] ** 4) * np.sin(x[i]) * np.cos(x[i] ** 2) + (x[i] ** 3) * np.tan(x[i] * 0.5)
        
        # Adaptive penalty landscapes with exponential coupling terms
        adaptive_penalty = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                adaptive_penalty += np.exp(2.0 * (np.abs(x[i]) - 4.0)) * np.sin(3 * x[i])
            else:
                adaptive_penalty += 0.5 * (x[i] ** 2) * np.cos(2 * x[i]) + 0.1 * (x[i] ** 4)
        
        # Nested complex sinusoidal structures with varying frequencies
        nested_sine = 0.0
        for i in range(self.dim):
            freq_factor = 2 ** (i % 4)
            nested_sine += np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[i] * 0.7) * np.exp(-0.5 * x[i] ** 2)
        
        # Multi-scale Gaussian peaks with varying heights and widths
        gaussian_peaks = 0.0
        centers = np.linspace(-4.8, 4.8, 13)
        for center in centers:
            gaussian_peaks += np.exp(-0.5 * np.sum((x - center) ** 2) / (0.3 + 0.1 * np.abs(center))) * np.sin(3 * np.pi * np.sum((x - center) ** 2))
        
        # Cross-term exponential attraction basins with fractal scaling
        cross_attraction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j]) ** 2 + 1e-8)
                cross_attraction += np.exp(-dist) * np.sin(5 * np.pi * dist) * (1.0 + 0.2 * np.sin(dist))
        
        # Combined fitness with adjusted weights
        return 0.25 * chaotic_fractal + 0.2 * radial_corridors + 0.2 * poly_trig_interaction + 0.15 * adaptive_penalty + 0.1 * nested_sine + 0.1 * gaussian_peaks + cross_attraction