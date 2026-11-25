import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial polynomial component with higher-order terms and fractal scaling
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.5 * r + 0.3 * r**2 + 0.1 * r**3 + 0.05 * r**4 + 0.01 * r**5) * np.exp(-0.3 * r**2)
        
        # Multi-frequency sinusoidal oscillations with chaotic modulation
        freq_osc = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(14 * np.pi * x_scaled) + 
                         0.7 * np.sin(20 * np.pi * x_scaled) * np.cos(19 * np.pi * x_scaled) + 
                         0.3 * np.sin(25 * np.pi * x_scaled) * np.cos(24 * np.pi * x_scaled) + 
                         0.1 * np.sin(30 * np.pi * x_scaled) * np.cos(29 * np.pi * x_scaled))
        
        # Enhanced cross-dimensional coupling with higher-order polynomial interactions
        cross_coupling = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * np.sin(7 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                               0.5 * (x_scaled[:-2]**4 + x_scaled[2:]**4) * np.cos(4 * np.pi * (x_scaled[:-2] - x_scaled[2:])) + 
                               0.3 * (x_scaled[:-3]**2 + x_scaled[3:]**2) * np.sin(6 * np.pi * (x_scaled[:-3] - x_scaled[3:])))
        
        # Multi-scale chaotic component with exponential frequency modulation
        chaotic = np.sum(np.sin(10 * r**1.7) * np.cos(9 * r**1.7) + 
                        0.4 * np.sin(18 * r**1.4) * np.cos(17 * r**1.4) + 
                        0.2 * np.sin(25 * r**1.2) * np.cos(24 * r**1.2) + 
                        0.1 * np.sin(32 * r**1.1) * np.cos(31 * r**1.1))
        
        # Enhanced multimodal component with multiple peak types and varying amplitudes
        multimodal = 0.5 * np.sum(np.sin(6 * np.pi * x_scaled)**2 + 
                                0.3 * np.sin(12 * np.pi * x_scaled)**3 + 
                                0.1 * np.sin(18 * np.pi * x_scaled)**4 + 
                                0.05 * np.sin(24 * np.pi * x_scaled)**5)
        
        # Fractal-like interaction with self-similar structure at multiple scales
        fractal = 0.2 * np.sum(np.sin(8 * np.pi * x_scaled**1.9) * np.cos(7 * np.pi * x_scaled**1.9) + 
                             0.15 * np.sin(13 * np.pi * x_scaled**1.6) * np.cos(12 * np.pi * x_scaled**1.6) + 
                             0.1 * np.sin(18 * np.pi * x_scaled**1.4) * np.cos(17 * np.pi * x_scaled**1.4))
        
        # Adaptive coupling with dimensionality-dependent terms and exponential scaling
        adaptive = 0.1 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(3 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)) + 
                              0.05 * np.abs(x_scaled[:-2] - x_scaled[2:]) * np.cos(2 * np.pi * (x_scaled[:-2]**3 + x_scaled[2:]**3)))
        
        # Enhanced high-dimensional noise component with multiple frequency bands
        noise = 0.05 * np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(29 * np.pi * x_scaled) + 
                            0.08 * np.sin(35 * np.pi * x_scaled) * np.cos(34 * np.pi * x_scaled) + 
                            0.03 * np.sin(40 * np.pi * x_scaled) * np.cos(39 * np.pi * x_scaled))
        
        # Additional complex interaction terms for increased landscape complexity
        interaction = 0.03 * np.sum(np.sin(5 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                                 np.cos(4 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                                 0.02 * np.sin(8 * np.pi * (x_scaled[:-2]**3 + x_scaled[2:]**3)) * 
                                 np.cos(7 * np.pi * (x_scaled[:-2] - x_scaled[2:])))
        
        # Combined landscape with weighted components and increased complexity
        return (0.25 * radial + 0.2 * freq_osc + 0.18 * cross_coupling + 0.14 * chaotic + 
                0.09 * multimodal + 0.07 * fractal + 0.05 * adaptive + 0.06 * noise + 0.06 * interaction)