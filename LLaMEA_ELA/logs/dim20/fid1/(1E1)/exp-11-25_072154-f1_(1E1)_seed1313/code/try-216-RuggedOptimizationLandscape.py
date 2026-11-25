import numpy as np

class RuggedOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Exponential decay component with varying rates and directional influence
        exp_decay = np.sum(np.exp(-5 * np.abs(x_scaled)) * np.cos(3 * np.pi * x_scaled) + 
                          0.7 * np.exp(-3 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled) + 
                          0.5 * np.exp(-2 * np.abs(x_scaled)) * np.cos(5 * np.pi * x_scaled))
        
        # Trigonometric wave interference with multiple frequencies and phase shifts
        wave_interference = np.sum(np.sin(15 * x_scaled) * np.cos(14 * x_scaled) + 
                                 0.8 * np.sin(20 * x_scaled) * np.cos(19 * x_scaled) + 
                                 0.6 * np.sin(25 * x_scaled) * np.cos(24 * x_scaled) + 
                                 0.4 * np.sin(30 * x_scaled) * np.cos(29 * x_scaled))
        
        # Polynomial coupling between dimensions with mixed powers and interaction terms
        poly_coupling = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * np.sin(7 * (x_scaled[:-1] - x_scaled[1:])) + 
                              0.9 * (x_scaled[:-2]**2 + x_scaled[2:]**2) * np.cos(6 * (x_scaled[:-2] - x_scaled[2:])) + 
                              0.7 * (x_scaled[:-3]**4 + x_scaled[3:]**4) * np.sin(5 * (x_scaled[:-3] - x_scaled[3:])) + 
                              0.5 * (x_scaled[:-4]**2 + x_scaled[4:]**2) * np.cos(4 * (x_scaled[:-4] - x_scaled[4:])))
        
        # Multi-scale oscillation with self-similar patterns and varying amplitude
        multi_scale = np.sum(np.sin(10 * x_scaled**1.5) * np.cos(9 * x_scaled**1.5) + 
                            0.8 * np.sin(15 * x_scaled**1.3) * np.cos(14 * x_scaled**1.3) + 
                            0.6 * np.sin(20 * x_scaled**1.1) * np.cos(19 * x_scaled**1.1) + 
                            0.4 * np.sin(25 * x_scaled**0.9) * np.cos(24 * x_scaled**0.9))
        
        # Ruggedness component with sharp valleys and steep gradients
        ruggedness = np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.exp(-2 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) + 
                           0.8 * np.abs(x_scaled[:-2] - x_scaled[2:]) * np.exp(-1.5 * (x_scaled[:-2]**2 + x_scaled[2:]**2)) + 
                           0.6 * np.abs(x_scaled[:-3] - x_scaled[3:]) * np.exp(-1.0 * (x_scaled[:-3]**2 + x_scaled[3:]**2)))
        
        # Asymmetric harmonic component with directional bias and irregular spacing
        asymmetric = np.sum(np.sin(8 * x_scaled)**2 * np.cos(7 * x_scaled) + 
                           0.9 * np.sin(12 * x_scaled)**3 * np.sin(11 * x_scaled) + 
                           0.7 * np.sin(16 * x_scaled)**4 * np.cos(15 * x_scaled) + 
                           0.5 * np.sin(20 * x_scaled)**5 * np.sin(19 * x_scaled))
        
        # Combined landscape with balanced weights for ruggedness and multimodality
        return (0.3 * exp_decay + 0.25 * wave_interference + 0.2 * poly_coupling + 
                0.15 * multi_scale + 0.1 * ruggedness + 0.05 * asymmetric)