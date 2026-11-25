import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial polynomial component with modified exponents and coefficients
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.7 * r + 0.4 * r**2 + 0.2 * r**3 + 0.1 * r**4 + 0.05 * r**5) * np.exp(-0.5 * r**2)
        
        # Modified high-frequency sinusoidal oscillations with altered frequencies and amplitudes
        freq_osc = np.sum(1.2 * np.sin(18 * np.pi * x_scaled) * np.cos(17 * np.pi * x_scaled) + 
                         0.9 * np.sin(22 * np.pi * x_scaled) * np.cos(21 * np.pi * x_scaled) + 
                         0.6 * np.sin(27 * np.pi * x_scaled) * np.cos(26 * np.pi * x_scaled) + 
                         0.3 * np.sin(32 * np.pi * x_scaled) * np.cos(31 * np.pi * x_scaled))
        
        # Improved cross-dimensional coupling with different interaction terms and weights
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * np.sin(8 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                               0.9 * (x_scaled[:-2]**3 + x_scaled[2:]**3) * np.cos(6 * np.pi * (x_scaled[:-2] - x_scaled[2:])) + 
                               0.6 * (x_scaled[:-3]**2 + x_scaled[3:]**2) * np.sin(7 * np.pi * (x_scaled[:-3] - x_scaled[3:])))
        
        # Enhanced chaotic component with modified frequency modulation and additional harmonics
        chaotic = np.sum(np.sin(12 * r**1.8) * np.cos(11 * r**1.8) + 
                        0.7 * np.sin(18 * r**1.6) * np.cos(17 * r**1.6) + 
                        0.5 * np.sin(24 * r**1.4) * np.cos(23 * r**1.4) + 
                        0.3 * np.sin(30 * r**1.2) * np.cos(29 * r**1.2))
        
        # Refined multimodal component with more pronounced peaks and altered exponents
        multimodal = 0.8 * np.sum(np.sin(7 * np.pi * x_scaled)**2 + 
                                0.6 * np.sin(13 * np.pi * x_scaled)**3 + 
                                0.4 * np.sin(19 * np.pi * x_scaled)**4 + 
                                0.2 * np.sin(25 * np.pi * x_scaled)**5)
        
        # Improved fractal-like interaction with different scaling and interaction terms
        fractal = 0.5 * np.sum(np.sin(9 * np.pi * x_scaled**1.8) * np.cos(8 * np.pi * x_scaled**1.8) + 
                             0.4 * np.sin(15 * np.pi * x_scaled**1.6) * np.cos(14 * np.pi * x_scaled**1.6) + 
                             0.3 * np.sin(21 * np.pi * x_scaled**1.4) * np.cos(20 * np.pi * x_scaled**1.4))
        
        # Enhanced adaptive coupling with modified dimensionality-dependent terms
        adaptive = 0.3 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(5 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)) + 
                              0.2 * np.abs(x_scaled[:-2] - x_scaled[2:]) * np.cos(4 * np.pi * (x_scaled[:-2]**3 + x_scaled[2:]**3)))
        
        # Modified noise component with increased complexity and altered frequencies
        noise = 0.08 * np.sum(np.sin(35 * np.pi * x_scaled) * np.cos(34 * np.pi * x_scaled) + 
                            0.15 * np.sin(40 * np.pi * x_scaled) * np.cos(39 * np.pi * x_scaled) + 
                            0.12 * np.sin(45 * np.pi * x_scaled) * np.cos(44 * np.pi * x_scaled))
        
        # Combined landscape with optimized weights for better performance and increased difficulty
        return (0.25 * radial + 0.3 * freq_osc + 0.25 * cross_coupling + 0.18 * chaotic + 
                0.12 * multimodal + 0.1 * fractal + 0.07 * adaptive + 0.05 * noise)