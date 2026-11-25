import numpy as np

class SpectralFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial chaos expansion component with Hermite polynomials
        hermite_poly = np.sum((1 + 2 * x_scaled + 2 * x_scaled**2 + (4/3) * x_scaled**3 + 0.5 * x_scaled**4) * np.exp(-0.5 * x_scaled**2))
        
        # Spectral decomposition with frequency bands and amplitude modulation
        spectral = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled) + 
                         0.8 * np.sin(15 * np.pi * x_scaled) * np.cos(14 * np.pi * x_scaled) + 
                         0.6 * np.sin(20 * np.pi * x_scaled) * np.cos(19 * np.pi * x_scaled) + 
                         0.4 * np.sin(25 * np.pi * x_scaled) * np.cos(24 * np.pi * x_scaled))
        
        # Fractal self-similarity component with recursive scaling
        fractal = 0.0
        for i in range(1, min(6, self.dim + 1)):
            scale_factor = 0.5**i
            fractal += scale_factor * np.sum(np.sin((2**i) * np.pi * x_scaled) * np.cos((2**i - 1) * np.pi * x_scaled))
        
        # Cross-dimensional coupling with recursive interaction terms
        cross_dim = 0.0
        for i in range(1, min(4, self.dim)):
            cross_dim += (x_scaled[:-i]**2 + x_scaled[i:]**2) * np.sin(np.pi * (x_scaled[:-i] - x_scaled[i:]))
        
        # Multi-scale oscillation with varying frequencies and amplitudes
        multi_scale = 0.0
        for k in range(1, 6):
            multi_scale += (1/k) * np.sum(np.sin(k**2 * np.pi * x_scaled) * np.cos(k**1.5 * np.pi * x_scaled))
        
        # Chaotic phase modulation with logistic map behavior
        chaotic_phase = np.sum(np.sin(20 * np.pi * x_scaled + 0.5 * np.sin(10 * np.pi * x_scaled)) * 
                              np.cos(19 * np.pi * x_scaled + 0.3 * np.cos(15 * np.pi * x_scaled)))
        
        # Combined landscape with optimized weights
        return (0.3 * hermite_poly + 0.25 * spectral + 0.2 * fractal + 
                0.15 * cross_dim + 0.08 * multi_scale + 0.02 * chaotic_phase)