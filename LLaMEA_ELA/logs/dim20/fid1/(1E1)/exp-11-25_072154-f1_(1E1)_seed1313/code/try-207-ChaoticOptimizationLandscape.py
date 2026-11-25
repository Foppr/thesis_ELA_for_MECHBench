import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial polynomial component with smoother transitions and higher-order terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.8 * r + 0.4 * r**2 + 0.2 * r**3 + 0.1 * r**4 + 0.05 * r**5) * np.exp(-0.5 * r**2)
        
        # Modified high-frequency sinusoidal oscillations with better distribution and increased complexity
        freq_osc = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(19 * np.pi * x_scaled) + 
                         0.8 * np.sin(25 * np.pi * x_scaled) * np.cos(24 * np.pi * x_scaled) + 
                         0.6 * np.sin(30 * np.pi * x_scaled) * np.cos(29 * np.pi * x_scaled) + 
                         0.4 * np.sin(35 * np.pi * x_scaled) * np.cos(34 * np.pi * x_scaled) + 
                         0.2 * np.sin(40 * np.pi * x_scaled) * np.cos(39 * np.pi * x_scaled))
        
        # Improved cross-dimensional coupling with stronger interaction terms and additional dimension pairs
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * np.sin(8 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                               0.9 * (x_scaled[:-2]**3 + x_scaled[2:]**3) * np.cos(6 * np.pi * (x_scaled[:-2] - x_scaled[2:])) + 
                               0.7 * (x_scaled[:-3]**2 + x_scaled[3:]**2) * np.sin(7 * np.pi * (x_scaled[:-3] - x_scaled[3:])) + 
                               0.5 * (x_scaled[:-4]**3 + x_scaled[4:]**3) * np.cos(5 * np.pi * (x_scaled[:-4] - x_scaled[4:])))
        
        # Enhanced chaotic component with better frequency modulation and additional harmonics
        chaotic = np.sum(np.sin(12 * r**1.8) * np.cos(11 * r**1.8) + 
                        0.7 * np.sin(18 * r**1.6) * np.cos(17 * r**1.6) + 
                        0.5 * np.sin(24 * r**1.4) * np.cos(23 * r**1.4) + 
                        0.3 * np.sin(30 * r**1.2) * np.cos(29 * r**1.2) + 
                        0.1 * np.sin(36 * r**1.0) * np.cos(35 * r**1.0))
        
        # Refined multimodal component with more pronounced peaks and increased complexity
        multimodal = 0.8 * np.sum(np.sin(8 * np.pi * x_scaled)**2 + 
                                0.6 * np.sin(16 * np.pi * x_scaled)**3 + 
                                0.4 * np.sin(24 * np.pi * x_scaled)**4 + 
                                0.2 * np.sin(32 * np.pi * x_scaled)**5 + 
                                0.1 * np.sin(40 * np.pi * x_scaled)**6)
        
        # Improved fractal-like interaction with better self-similarity and multi-scale components
        fractal = 0.5 * np.sum(np.sin(10 * np.pi * x_scaled**2.1) * np.cos(9 * np.pi * x_scaled**2.1) + 
                             0.4 * np.sin(16 * np.pi * x_scaled**1.9) * np.cos(15 * np.pi * x_scaled**1.9) + 
                             0.3 * np.sin(22 * np.pi * x_scaled**1.7) * np.cos(21 * np.pi * x_scaled**1.7) + 
                             0.2 * np.sin(28 * np.pi * x_scaled**1.5) * np.cos(27 * np.pi * x_scaled**1.5))
        
        # Enhanced adaptive coupling with dimensionality-dependent terms and additional interaction
        adaptive = 0.3 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(5 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)) + 
                              0.25 * np.abs(x_scaled[:-2] - x_scaled[2:]) * np.cos(4 * np.pi * (x_scaled[:-2]**3 + x_scaled[2:]**3)) + 
                              0.2 * np.abs(x_scaled[:-3] - x_scaled[3:]) * np.sin(3 * np.pi * (x_scaled[:-3]**2 + x_scaled[3:]**2)))
        
        # Modified noise component with increased impact and complexity
        noise = 0.1 * np.sum(np.sin(40 * np.pi * x_scaled) * np.cos(39 * np.pi * x_scaled) + 
                            0.15 * np.sin(45 * np.pi * x_scaled) * np.cos(44 * np.pi * x_scaled) + 
                            0.12 * np.sin(50 * np.pi * x_scaled) * np.cos(49 * np.pi * x_scaled) + 
                            0.08 * np.sin(55 * np.pi * x_scaled) * np.cos(54 * np.pi * x_scaled))
        
        # Combined landscape with optimized weights for better performance and increased difficulty
        return (0.25 * radial + 0.3 * freq_osc + 0.25 * cross_coupling + 0.2 * chaotic + 
                0.15 * multimodal + 0.1 * fractal + 0.08 * adaptive + 0.05 * noise)