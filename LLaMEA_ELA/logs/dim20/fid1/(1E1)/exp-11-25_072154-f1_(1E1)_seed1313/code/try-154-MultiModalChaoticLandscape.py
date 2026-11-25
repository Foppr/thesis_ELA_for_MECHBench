import numpy as np

class MultiModalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial Gaussian component with multiple peaks
        r = np.sqrt(np.sum(x_scaled**2))
        gaussian_radial = np.exp(-r**2) + 0.5 * np.exp(-0.5 * (r - 1.5)**2) + 0.3 * np.exp(-0.3 * (r - 2.5)**2)
        
        # Multi-dimensional sinusoidal periodicity with varying frequencies
        sinusoidal = np.sum(np.sin(8 * np.pi * x_scaled) + 0.7 * np.sin(12 * np.pi * x_scaled) + 
                           0.4 * np.sin(16 * np.pi * x_scaled) + 0.2 * np.sin(20 * np.pi * x_scaled))
        
        # Cross-dimensional coupling with interaction terms
        coupling = np.sum((x_scaled[:-1] * x_scaled[1:]) * np.sin(5 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Multi-scale chaotic oscillations with fractal-like behavior
        chaotic_osc = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) + 
                            0.5 * np.sin(7 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) + 
                            0.2 * np.sin(11 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled))
        
        # Multi-modal component with multiple local minima
        multimodal = 0.5 * np.sum(np.sin(6 * np.pi * x_scaled)**2 + 
                                0.3 * np.sin(9 * np.pi * x_scaled)**3 + 
                                0.1 * np.sin(13 * np.pi * x_scaled)**4)
        
        # Modified radial sinusoidal interaction
        radial_sin = np.sum(np.sin(5 * r) * np.cos(3 * r) + 0.6 * np.sin(8 * r) * np.cos(6 * r))
        
        # High-frequency oscillatory component
        high_freq = 0.1 * np.sum(np.sin(50 * np.pi * x_scaled) + 
                               0.05 * np.sin(70 * np.pi * x_scaled) + 
                               0.02 * np.sin(90 * np.pi * x_scaled))
        
        # Modified cross-dimensional interaction with exponential decay
        exp_coupling = np.sum(np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) * 
                            np.sin(3 * np.pi * (x_scaled[:-1] + x_scaled[1:])))
        
        # Fractal-like self-similar component
        fractal = 0.2 * np.sum(np.sin(4 * np.pi * x_scaled**1.5) + 
                             0.15 * np.sin(6 * np.pi * x_scaled**1.3) + 
                             0.1 * np.sin(8 * np.pi * x_scaled**1.1))
        
        # Combined landscape
        return (0.3 * gaussian_radial + 0.25 * sinusoidal + 0.15 * coupling + 
                0.12 * chaotic_osc + 0.08 * multimodal + 0.06 * radial_sin + 
                0.04 * high_freq + 0.03 * exp_coupling + 0.02 * fractal)