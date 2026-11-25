import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial polynomial component with smoother transitions
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.4 * r + 0.2 * r**2 + 0.08 * r**3 + 0.03 * r**4) * np.exp(-0.3 * r**2)
        
        # Modified high-frequency sinusoidal oscillations with better distribution
        freq_osc = np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled) + 
                         0.6 * np.sin(18 * np.pi * x_scaled) * np.cos(17 * np.pi * x_scaled) + 
                         0.2 * np.sin(25 * np.pi * x_scaled) * np.cos(24 * np.pi * x_scaled))
        
        # Improved cross-dimensional coupling with stronger interaction terms
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * np.sin(6 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                               0.7 * (x_scaled[:-2]**3 + x_scaled[2:]**3) * np.cos(4 * np.pi * (x_scaled[:-2] - x_scaled[2:])))
        
        # Enhanced chaotic component with better frequency modulation
        chaotic = np.sum(np.sin(8 * r**1.6) * np.cos(7 * r**1.6) + 
                        0.5 * np.sin(14 * r**1.4) * np.cos(13 * r**1.4) + 
                        0.3 * np.sin(20 * r**1.2) * np.cos(19 * r**1.2))
        
        # Refined multimodal component with more pronounced peaks
        multimodal = 0.6 * np.sum(np.sin(5 * np.pi * x_scaled)**2 + 
                                0.4 * np.sin(10 * np.pi * x_scaled)**3 + 
                                0.2 * np.sin(15 * np.pi * x_scaled)**4)
        
        # Improved fractal-like interaction with better self-similarity
        fractal = 0.3 * np.sum(np.sin(7 * np.pi * x_scaled**1.9) * np.cos(6 * np.pi * x_scaled**1.9) + 
                             0.2 * np.sin(12 * np.pi * x_scaled**1.6) * np.cos(11 * np.pi * x_scaled**1.6))
        
        # Enhanced adaptive coupling with dimensionality-dependent terms
        adaptive = 0.15 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(3 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Modified noise component with reduced impact
        noise = 0.03 * np.sum(np.sin(28 * np.pi * x_scaled) * np.cos(27 * np.pi * x_scaled) + 
                            0.06 * np.sin(32 * np.pi * x_scaled) * np.cos(31 * np.pi * x_scaled))
        
        # Combined landscape with optimized weights for better performance
        return (0.25 * radial + 0.2 * freq_osc + 0.18 * cross_coupling + 0.14 * chaotic + 
                0.09 * multimodal + 0.07 * fractal + 0.05 * adaptive + 0.02 * noise)