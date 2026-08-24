import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.hurst = 0.3  # Controls fractal roughness
        self.fractal_scale = 10.0
        self.modulation_freq = 2.0 * np.pi
        self.base_amplitude = 5.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize input to [-1, 1] for fractal generation
        x_norm = x / 5.0
        
        # Generate fractal component using fractional Brownian motion-like approach
        fractal_component = 0.0
        for i in range(self.dim):
            # Create self-similar pattern using multiple frequencies
            freqs = [1.0, 2.0, 4.0, 8.0]
            for freq in freqs:
                fractal_component += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.5) * np.exp(-0.1 * freq)
        
        # Add multi-scale sinusoidal modulation
        modulation = 0.0
        for i in range(self.dim):
            modulation += np.sin(self.modulation_freq * x_norm[i]) * np.cos(self.modulation_freq * x_norm[i] * 0.3) + \
                         np.sin(self.modulation_freq * x_norm[i] * 0.7) * np.cos(self.modulation_freq * x_norm[i] * 0.5)
        
        # Radial fractal component with polynomial decay
        r = np.sqrt(np.sum(x_norm**2))
        radial_fractal = np.sin(self.fractal_scale * r) * np.cos(self.fractal_scale * r * 0.5) * np.exp(-0.5 * r**2)
        
        # Cross-dimensional interaction terms with fractal scaling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-inspired interaction
                interaction = np.sin(self.fractal_scale * x_norm[i] * x_norm[j]) * \
                              np.cos(self.fractal_scale * x_norm[i] * x_norm[j] * 0.3)
                cross_interaction += interaction * (1.0 / (1.0 + np.abs(i - j)))
        
        # Add polynomial terms for increased curvature
        poly_terms = 0.0
        for i in range(self.dim):
            poly_terms += 0.1 * x_norm[i]**4 + 0.05 * x_norm[i]**6
        
        # Combine all components with varying weights
        return (1.5 * fractal_component + 
                2.0 * modulation + 
                0.8 * radial_fractal + 
                0.5 * cross_interaction + 
                0.3 * poly_terms)