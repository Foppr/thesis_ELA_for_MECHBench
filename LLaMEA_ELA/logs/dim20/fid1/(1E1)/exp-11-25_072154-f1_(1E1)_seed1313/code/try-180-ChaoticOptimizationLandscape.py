import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial polynomial with higher-order terms and sharper transitions
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.6 * r + 0.3 * r**2 + 0.15 * r**3 + 0.07 * r**4 + 0.02 * r**5) * np.exp(-0.4 * r**2)
        
        # High-frequency sinusoidal oscillations with increased complexity and irregularity
        freq_osc = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(14 * np.pi * x_scaled) + 
                         0.7 * np.sin(22 * np.pi * x_scaled) * np.cos(21 * np.pi * x_scaled) + 
                         0.4 * np.sin(30 * np.pi * x_scaled) * np.cos(29 * np.pi * x_scaled) + 
                         0.2 * np.sin(35 * np.pi * x_scaled) * np.cos(34 * np.pi * x_scaled))
        
        # Stronger cross-dimensional coupling with non-linear interaction terms
        cross_coupling = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * np.sin(7 * np.pi * (x_scaled[:-1] - x_scaled[1:])) + 
                               0.8 * (x_scaled[:-2]**4 + x_scaled[2:]**4) * np.cos(5 * np.pi * (x_scaled[:-2] - x_scaled[2:])))
        
        # Enhanced chaotic component with multi-scale fractal-like behavior
        chaotic = np.sum(np.sin(10 * r**1.7) * np.cos(9 * r**1.7) + 
                        0.6 * np.sin(18 * r**1.5) * np.cos(17 * r**1.5) + 
                        0.4 * np.sin(25 * r**1.3) * np.cos(24 * r**1.3) + 
                        0.2 * np.sin(32 * r**1.1) * np.cos(31 * r**1.1))
        
        # More pronounced multimodal component with sharper peaks and valleys
        multimodal = 0.7 * np.sum(np.sin(6 * np.pi * x_scaled)**2 + 
                                0.5 * np.sin(12 * np.pi * x_scaled)**3 + 
                                0.3 * np.sin(18 * np.pi * x_scaled)**4 + 
                                0.1 * np.sin(25 * np.pi * x_scaled)**5)
        
        # Fractal-like interaction with stronger self-similarity and recursive patterns
        fractal = 0.4 * np.sum(np.sin(9 * np.pi * x_scaled**1.8) * np.cos(8 * np.pi * x_scaled**1.8) + 
                             0.3 * np.sin(15 * np.pi * x_scaled**1.5) * np.cos(14 * np.pi * x_scaled**1.5) + 
                             0.2 * np.sin(20 * np.pi * x_scaled**1.3) * np.cos(19 * np.pi * x_scaled**1.3))
        
        # Adaptive coupling with dynamic weights based on dimensionality
        adaptive = 0.2 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(4 * np.pi * (x_scaled[:-1]**2 + x_scaled[1:]**2)) + 
                              0.1 * np.abs(x_scaled[:-2] - x_scaled[2:]) * np.cos(3 * np.pi * (x_scaled[:-2]**3 + x_scaled[2:]**3)))
        
        # Increased noise component with broader frequency spectrum and more irregular structure
        noise = 0.05 * np.sum(np.sin(35 * np.pi * x_scaled) * np.cos(34 * np.pi * x_scaled) + 
                            0.08 * np.sin(42 * np.pi * x_scaled) * np.cos(41 * np.pi * x_scaled) + 
                            0.06 * np.sin(50 * np.pi * x_scaled) * np.cos(49 * np.pi * x_scaled))
        
        # Combined landscape with updated weights for higher complexity and challenge
        return (0.22 * radial + 0.18 * freq_osc + 0.20 * cross_coupling + 0.16 * chaotic + 
                0.10 * multimodal + 0.08 * fractal + 0.06 * adaptive + 0.02 * noise)