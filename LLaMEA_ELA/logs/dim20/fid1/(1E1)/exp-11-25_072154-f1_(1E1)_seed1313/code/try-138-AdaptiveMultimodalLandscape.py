import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial base component with varying degrees
        poly_base = np.sum(0.5 * x_scaled**2 + 0.3 * x_scaled**4 + 0.1 * x_scaled**6)
        
        # Sinusoidal wave component with adaptive frequencies
        wave_freq = 2 + np.abs(x_scaled)
        sin_wave = np.sum(np.sin(wave_freq * np.pi * x_scaled) * np.cos(wave_freq * np.pi * x_scaled))
        
        # Multi-scale interaction terms with exponential decay
        scale_factors = [0.1, 0.3, 0.7]
        interaction = 0
        for i, scale in enumerate(scale_factors):
            if i < len(x_scaled) - 1:
                interaction += scale * np.exp(-0.5 * (x_scaled[i] - x_scaled[i+1])**2) * np.sin(3 * np.pi * (x_scaled[i] + x_scaled[i+1]))
        
        # Adaptive coupling with distance-dependent modulation
        dist_coupling = 0
        for i in range(len(x_scaled)):
            for j in range(i+1, len(x_scaled)):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                dist_coupling += np.exp(-dist**2) * np.sin(5 * np.pi * (x_scaled[i] + x_scaled[j]))
        
        # High-frequency oscillatory component
        high_freq = np.sum(np.sin(10 * np.pi * x_scaled**3) * np.cos(8 * np.pi * x_scaled**2))
        
        # Fractal-like self-similarity with recursive scaling
        fractal_component = 0
        for i in range(len(x_scaled)):
            fractal_component += np.sin(4 * np.pi * x_scaled[i]**1.5) * np.cos(3 * np.pi * x_scaled[i]**1.2)
        
        # Asymmetric multimodal peaks
        asym_peaks = np.sum((x_scaled**2 + 0.5 * x_scaled**4) * np.sin(6 * np.pi * x_scaled))
        
        # Combined fitness function with adaptive weights
        return (0.3 * poly_base + 0.25 * sin_wave + 0.2 * interaction + 
                0.1 * dist_coupling + 0.08 * high_freq + 0.07 * fractal_component + 
                0.05 * asym_peaks)