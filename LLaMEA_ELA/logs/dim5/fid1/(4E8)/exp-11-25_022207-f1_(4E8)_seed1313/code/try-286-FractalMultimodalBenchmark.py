import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different scales
        self.scales = np.logspace(0, 2, min(5, dim))
        self.frequencies = np.logspace(1, 3.5, min(5, dim))
        self.amplitudes = np.logspace(0.5, 3.0, min(5, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal component with multiple scales
        for i in range(min(len(self.scales), self.dim)):
            scale = self.scales[i]
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            
            # Multi-scale sinusoidal contribution
            fractal_term = amp * np.sin(freq * np.pi * x_norm[i] * scale) * \
                          np.cos(freq * np.pi * x_norm[i] / scale)
            
            # Add hierarchical structure through nested scaling with enhanced coupling
            if i > 0:
                fractal_term *= (1.0 + 0.7 * np.sin(np.pi * x_norm[i-1]) * np.cos(np.pi * x_norm[i-1]))
                
            result += fractal_term
            
        # Add self-similar peaks using recursive structure with modified peak shapes
        peak_component = 0.0
        for i in range(self.dim):
            # Create nested peaks with varying heights and widths
            peak_height = 2.5 + 2.0 * np.sin(4.0 * np.pi * x_norm[i])
            peak_width = 0.3 + 0.4 * np.cos(3.0 * np.pi * x_norm[i])
            
            # Gaussian-like peaks with fractal scaling and sharper profiles
            peak_value = peak_height * np.exp(-0.5 * (x_norm[i] / peak_width)**3)
            peak_component += peak_value
            
        # Add interaction terms between dimensions with enhanced fractal coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Enhanced fractal coupling with non-linear interaction
                coupling_scale = (i + j) / (self.dim + 2)
                interaction = np.sin(np.pi * (x_norm[i] - x_norm[j]) * coupling_scale**1.5) * \
                             np.cos(np.pi * (x_norm[i] + x_norm[j]) / (coupling_scale + 0.5))
                interaction_term += interaction
                
        # Add chaotic modulation with enhanced fractal frequency components
        chaotic_component = 0.0
        for i in range(self.dim):
            # Multiple chaotic frequencies that create complex landscape
            freqs = [8.0, 15.0, 22.0, 27.0]
            for f in freqs:
                chaotic_component += np.sin(f * x_norm[i]) * np.cos(f * x_norm[i] / (i + 1.5))
                
        # Combine all components
        result = result + peak_component + interaction_term + 0.6 * chaotic_component
        
        # Add noise with fractal characteristics
        noise = 0.015 * np.random.randn() * (1.0 + 0.15 * np.abs(np.mean(x_norm)))
        
        return result + noise