import numpy as np

class HarmonicChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-0.5 * r**2) * (1 + 0.3 * np.sin(10 * r) + 0.2 * np.cos(15 * r))
        
        # Multi-frequency sinusoidal terms with varying amplitudes
        sinusoidal = np.sum(np.sin(2 * np.pi * x_scaled) + 
                           0.7 * np.sin(4 * np.pi * x_scaled) + 
                           0.4 * np.sin(6 * np.pi * x_scaled) + 
                           0.2 * np.sin(8 * np.pi * x_scaled))
        
        # Phase-shifted harmonic components for increased complexity
        phase_shifted = np.sum(np.sin(3 * np.pi * x_scaled + np.pi/4) * 
                              np.cos(2 * np.pi * x_scaled + np.pi/6) + 
                              0.5 * np.sin(5 * np.pi * x_scaled + np.pi/3) * 
                              np.cos(3 * np.pi * x_scaled + np.pi/5))
        
        # Cross-dimensional coupling with exponential weighting
        cross_dim = 0.5 * np.sum(np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) * 
                               np.sin(2 * np.pi * (x_scaled[:-1] + x_scaled[1:])))
        
        # Multi-modal structure with periodic peaks
        multimodal = 0.3 * np.sum(np.sin(12 * np.pi * x_scaled)**2 + 
                                0.4 * np.sin(8 * np.pi * x_scaled)**3 + 
                                0.2 * np.sin(6 * np.pi * x_scaled)**4)
        
        # Fractal-like self-similarity through nested sinusoidal components
        fractal_like = 0.2 * np.sum(np.sin(15 * np.pi * x_scaled**0.7) + 
                                  0.3 * np.sin(10 * np.pi * x_scaled**1.3) + 
                                  0.1 * np.sin(5 * np.pi * x_scaled**2))
        
        # Adaptive frequency modulation based on radial distance
        adaptive_freq = 0.1 * np.sum(np.sin((5 + 2 * r) * np.pi * x_scaled) * 
                                   np.cos((3 + 1.5 * r) * np.pi * x_scaled))
        
        # Add a unique spiral-like structure in high dimensions
        spiral = 0.15 * np.sum(np.sin(2 * np.pi * (x_scaled[:-1] * x_scaled[1:] + r)) * 
                             np.cos(2 * np.pi * (x_scaled[:-1] * x_scaled[1:] - r)))
        
        # Combine all components with optimized weights
        return 0.3 * radial + 0.25 * sinusoidal + 0.15 * phase_shifted + 0.1 * cross_dim + \
               0.1 * multimodal + 0.08 * fractal_like + 0.07 * adaptive_freq + 0.05 * spiral