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
        freq_osc = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(14 * np.pi * x_scaled) + 
                         0.6 * np.sin(20 * np.pi * x_scaled) * np.cos(19 * np.pi * x_scaled) + 
                         0.2 * np.sin(28 * np.pi * x_scaled) * np.cos(27 * np.pi * x_scaled))
        
        # Improved cross-dimensional coupling with stronger interaction terms
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * np.sin(7 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                               0.7 * (x_scaled[:-2]**3 + x_scaled[2:]**3) * np.cos(5 * np.pi * (x_scaled[:-2] - x_scaled[2:])))
        
        # Enhanced chaotic component with better frequency modulation
        chaotic = np.sum(np.sin(10 * r**1.7) * np.cos(9 * r**1.7) + 
                        0.5 * np.sin(16 * r**1.5) * np.cos(15 * r**1.5) + 
                        0.3 * np.sin(22 * r**1.3) * np.cos(21 * r**1.3))
        
        # Refined multimodal component with more pronounced peaks
        multimodal = 0.7 * np.sum(np.sin(6 * np.pi * x_scaled)**2 + 
                                0.4 * np.sin(12 * np.pi * x_scaled)**3 + 
                                0.2 * np.sin(18 * np.pi * x_scaled)**4)
        
        # Improved fractal-like interaction with better self-similarity
        fractal = 0.4 * np.sum(np.sin(8 * np.pi * x_scaled**2) * np.cos(7 * np.pi * x_scaled**2) + 
                             0.2 * np.sin(14 * np.pi * x_scaled**1.7) * np.cos(13 * np.pi * x_scaled**1.7))
        
        # Enhanced adaptive coupling with dimensionality-dependent terms
        adaptive = 0.2 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(4 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Modified noise component with reduced impact
        noise = 0.05 * np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(29 * np.pi * x_scaled) + 
                            0.08 * np.sin(35 * np.pi * x_scaled) * np.cos(34 * np.pi * x_scaled))
        
        # Combined landscape with optimized weights for better performance
        return (0.3 * radial + 0.25 * freq_osc + 0.2 * cross_coupling + 0.15 * chaotic + 
                0.1 * multimodal + 0.08 * fractal + 0.06 * adaptive + 0.01 * noise)