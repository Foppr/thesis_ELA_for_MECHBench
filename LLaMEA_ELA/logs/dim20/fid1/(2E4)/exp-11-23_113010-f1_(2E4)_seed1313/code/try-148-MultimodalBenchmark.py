import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        # Fractal structure with recursive scaling
        for i in range(self.dim):
            # Modified power-law scaling with enhanced nonlinearity
            scale_factor = np.power(np.abs(x_norm[i]) + 1e-8, 0.42)
            
            # Enhanced sinusoidal components with varying frequencies
            freq1 = 3 * np.pi * (i + 1) * (1 + 0.6 * np.sin(x_norm[i] * np.pi / 2))
            freq2 = 5 * np.pi * (i + 1) * (1 + 0.4 * np.cos(x_norm[i] * np.pi / 3))
            
            # Altered recursive dimension coupling with stronger interactions
            coupling = 1.0
            for j in range(i):
                coupling *= (1 + 0.15 * np.sin(x_norm[j] * (j + 2) * np.pi / (i + 1)) * np.cos(x_norm[j] * (j + 1) * np.pi / (i + 2)))
            
            # Modified multi-scale sinusoidal modulation with additional nonlinear terms
            term1 = np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i])
            term2 = np.sin(freq1 * x_norm[i]**1.5) * np.cos(freq2 * x_norm[i]**2.5)
            
            # Combine with modified scaling and coupling
            result += scale_factor * coupling * (term1 + 0.6 * term2)
        
        # Enhanced fractal component with different amplitude decay
        fractal_component = 0.0
        for i in range(self.dim):
            # Modified recursive pattern with exponential amplitude decay
            amp = 0.15 / np.exp(i * 0.3)
            freq = 3**(i % 5 + 1) * (1 + 0.25 * np.sin(i * np.pi / self.dim))
            fractal_component += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**1.8)
        
        # Modified dynamic weighting scheme
        weight_main = 0.55 + 0.45 * np.sin(self.dim * 0.25)
        weight_fractal = 0.45 + 0.55 * np.cos(self.dim * 0.2)
        
        return weight_main * result + weight_fractal * fractal_component