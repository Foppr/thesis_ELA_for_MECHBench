import numpy as np

class MultiModalAttractorLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial base with mixed degrees
        poly_base = np.sum(x_scaled**4 + 0.5 * x_scaled**3 - 0.3 * x_scaled**2 + 0.1 * x_scaled)
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        sin_wave = np.sum(np.sin(10 * x_scaled) * np.cos(7 * x_scaled) + 
                         0.5 * np.sin(15 * x_scaled) * np.cos(12 * x_scaled) + 
                         0.3 * np.sin(20 * x_scaled) * np.cos(18 * x_scaled))
        
        # Gradient-based attraction terms with different control parameters
        attraction = np.sum((x_scaled[:-1] - x_scaled[1:])**2 * np.exp(-0.5 * (x_scaled[:-1] + x_scaled[1:])**2))
        
        # Multi-scale oscillatory pattern with coupling between dimensions
        coupled_osc = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) + 
                            0.7 * np.sin(8 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) + 
                            0.4 * np.sin(12 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled))
        
        # Radial multi-modal component with exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial_multi = np.sum(0.5 * np.exp(-r**2) * (np.sin(10 * r) + 0.3 * np.cos(15 * r)) + 
                            0.2 * np.exp(-0.5 * r**2) * (np.sin(20 * r) + 0.1 * np.cos(25 * r)))
        
        # Cross-dimensional interaction with polynomial coupling
        cross_poly = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * np.sin(2 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                           0.5 * (x_scaled[:-2]**2 + x_scaled[2:]**2) * np.cos(3 * np.pi * (x_scaled[:-2] - x_scaled[2:])))
        
        # Modified chaotic component with cubic interactions
        chaotic = np.sum(np.sin(8 * x_scaled**3) * np.cos(6 * x_scaled**3) + 
                        0.4 * np.sin(12 * x_scaled**3) * np.cos(9 * x_scaled**3))
        
        # Multi-scale fractal-like structure with self-similarity
        fractal = np.sum(np.sin(4 * np.pi * x_scaled**1.5) * np.cos(3 * np.pi * x_scaled**1.5) + 
                        0.6 * np.sin(6 * np.pi * x_scaled**1.2) * np.cos(5 * np.pi * x_scaled**1.2))
        
        # Adaptive coupling with dimensionality-dependent weights
        adaptive = np.sum(np.sin(9 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * 
                         (1 + 0.3 * np.sin(4 * np.pi * x_scaled)))
        
        # Combined landscape function
        return (0.25 * poly_base + 0.2 * sin_wave + 0.15 * attraction + 0.12 * coupled_osc + 
                0.1 * radial_multi + 0.08 * cross_poly + 0.06 * chaotic + 0.05 * fractal + 
                0.04 * adaptive)