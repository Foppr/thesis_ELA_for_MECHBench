import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial polynomial component with smoother transitions and higher-order terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.6 * r + 0.3 * r**2 + 0.15 * r**3 + 0.08 * r**4 + 0.03 * r**5) * np.exp(-0.4 * r**2)
        
        # Modified high-frequency sinusoidal oscillations with better distribution and increased complexity
        freq_osc = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(14 * np.pi * x_scaled) + 
                         0.7 * np.sin(20 * np.pi * x_scaled) * np.cos(19 * np.pi * x_scaled) + 
                         0.4 * np.sin(25 * np.pi * x_scaled) * np.cos(24 * np.pi * x_scaled) + 
                         0.2 * np.sin(30 * np.pi * x_scaled) * np.cos(29 * np.pi * x_scaled))
        
        # Improved cross-dimensional coupling with stronger interaction terms and additional dimension pairs
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * np.sin(7 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                               0.8 * (x_scaled[:-2]**3 + x_scaled[2:]**3) * np.cos(5 * np.pi * (x_scaled[:-2] - x_scaled[2:])) + 
                               0.5 * (x_scaled[:-3]**2 + x_scaled[3:]**2) * np.sin(6 * np.pi * (x_scaled[:-3] - x_scaled[3:])))
        
        # Enhanced chaotic component with better frequency modulation and additional harmonics
        chaotic = np.sum(np.sin(10 * r**1.7) * np.cos(9 * r**1.7) + 
                        0.6 * np.sin(16 * r**1.5) * np.cos(15 * r**1.5) + 
                        0.4 * np.sin(22 * r**1.3) * np.cos(21 * r**1.3) + 
                        0.2 * np.sin(28 * r**1.1) * np.cos(27 * r**1.1))
        
        # Refined multimodal component with more pronounced peaks and increased complexity
        multimodal = 0.7 * np.sum(np.sin(6 * np.pi * x_scaled)**2 + 
                                0.5 * np.sin(12 * np.pi * x_scaled)**3 + 
                                0.3 * np.sin(18 * np.pi * x_scaled)**4 + 
                                0.1 * np.sin(24 * np.pi * x_scaled)**5)
        
        # Improved fractal-like interaction with better self-similarity and multi-scale components
        fractal = 0.4 * np.sum(np.sin(8 * np.pi * x_scaled**1.9) * np.cos(7 * np.pi * x_scaled**1.9) + 
                             0.3 * np.sin(14 * np.pi * x_scaled**1.7) * np.cos(13 * np.pi * x_scaled**1.7) + 
                             0.2 * np.sin(20 * np.pi * x_scaled**1.5) * np.cos(19 * np.pi * x_scaled**1.5))
        
        # Enhanced adaptive coupling with dimensionality-dependent terms and additional interaction
        adaptive = 0.2 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(4 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)) + 
                              0.15 * np.abs(x_scaled[:-2] - x_scaled[2:]) * np.cos(3 * np.pi * (x_scaled[:-2]**3 + x_scaled[2:]**3)))
        
        # Modified noise component with increased impact and complexity
        noise = 0.05 * np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(29 * np.pi * x_scaled) + 
                            0.1 * np.sin(35 * np.pi * x_scaled) * np.cos(34 * np.pi * x_scaled) + 
                            0.08 * np.sin(40 * np.pi * x_scaled) * np.cos(39 * np.pi * x_scaled))
        
        # Combined landscape with optimized weights for better performance and increased difficulty
        return (0.2 * radial + 0.25 * freq_osc + 0.2 * cross_coupling + 0.15 * chaotic + 
                0.1 * multimodal + 0.08 * fractal + 0.06 * adaptive + 0.03 * noise)