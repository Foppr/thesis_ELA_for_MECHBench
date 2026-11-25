import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial polynomial component with multiple powers
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.5 * r + 0.3 * r**2 + 0.1 * r**3 + 0.05 * r**4) * np.exp(-0.5 * r**2)
        
        # High-frequency sinusoidal oscillations in each dimension
        freq_osc = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled) + 
                         0.7 * np.sin(15 * np.pi * x_scaled) * np.cos(14 * np.pi * x_scaled) + 
                         0.3 * np.sin(20 * np.pi * x_scaled) * np.cos(19 * np.pi * x_scaled))
        
        # Cross-dimensional coupling with polynomial interaction
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * np.sin(5 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                               0.5 * (x_scaled[:-2]**3 + x_scaled[2:]**3) * np.cos(3 * np.pi * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale chaotic component with varying frequency modulation
        chaotic = np.sum(np.sin(7 * r**1.5) * np.cos(6 * r**1.5) + 
                        0.4 * np.sin(13 * r**1.3) * np.cos(12 * r**1.3) + 
                        0.2 * np.sin(19 * r**1.1) * np.cos(18 * r**1.1))
        
        # Multimodal component with multiple peaks and valleys
        multimodal = 0.5 * np.sum(np.sin(4 * np.pi * x_scaled)**2 + 
                                0.3 * np.sin(8 * np.pi * x_scaled)**3 + 
                                0.1 * np.sin(12 * np.pi * x_scaled)**4)
        
        # Fractal-like interaction with self-similar structure
        fractal = 0.2 * np.sum(np.sin(6 * np.pi * x_scaled**1.8) * np.cos(5 * np.pi * x_scaled**1.8) + 
                             0.15 * np.sin(11 * np.pi * x_scaled**1.5) * np.cos(10 * np.pi * x_scaled**1.5))
        
        # Adaptive coupling with dimensionality-dependent terms
        adaptive = 0.1 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(2 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # High-dimensional noise component
        noise = 0.05 * np.sum(np.sin(25 * np.pi * x_scaled) * np.cos(24 * np.pi * x_scaled) + 
                            0.08 * np.sin(30 * np.pi * x_scaled) * np.cos(29 * np.pi * x_scaled))
        
        # Combined landscape with weighted components
        return (0.3 * radial + 0.25 * freq_osc + 0.15 * cross_coupling + 0.12 * chaotic + 
                0.08 * multimodal + 0.06 * fractal + 0.04 * adaptive + 0.05 * noise)