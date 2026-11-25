import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with modified exponential and polynomial terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) + 0.6 * np.exp(-0.2 * r**2) * np.sin(4 * r) + 
                 0.3 * np.exp(-0.15 * r**3) * np.cos(3 * r)) * (1 + 0.4 * np.sin(7 * r))
        
        # Multi-frequency trigonometric complexity with restructured cross-dimensional coupling
        trig = np.sum(np.cos(6 * np.pi * x_scaled) * np.sin(7 * np.pi * x_scaled) + 
                     0.5 * np.sin(4 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) + 
                     0.4 * np.cos(8 * np.pi * x_scaled) * np.sin(2 * np.pi * x_scaled))
        
        # Multi-scale exponential interaction terms with enhanced long-range coupling
        exp_interaction = np.sum(np.exp(-0.4 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                               0.7 * np.exp(-0.15 * (x_scaled[:-2] - x_scaled[2:])**2) + 
                               0.3 * np.exp(-0.03 * (x_scaled[:-3] - x_scaled[3:])**2))
        
        # Modified chaotic component with different power radial dependence
        chaotic = np.sum(np.sin(8 * r**2.3) * np.cos(6 * r**2.3) + 
                        0.5 * np.sin(12 * r**1.7) * np.cos(10 * r**1.7) + 
                        0.3 * np.sin(18 * r**1.4))
        
        # Improved multi-modal component with adaptive frequency modulation
        multimodal = 0.5 * np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled)) + \
                    0.4 * np.sum(np.sin(10 * np.pi * x_scaled)**2 + 
                                0.6 * np.sin(6 * np.pi * x_scaled)**3) + \
                    0.2 * np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled))
        
        # Enhanced cross-dimensional coupling term with different weighting
        cross_coupling = 0.25 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(3 * np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Fractal noise component with adjusted fractional Brownian motion characteristics
        fractal_noise = 0.2 * np.sum(np.sin(12 * np.pi * x_scaled**1.6) * np.cos(10 * np.pi * x_scaled**1.4)) + \
                       0.15 * np.sum(np.sin(20 * np.pi * x_scaled**0.8) * np.cos(16 * np.pi * x_scaled**1.2))
        
        # High-frequency oscillatory terms with modified amplitudes
        high_freq = 0.1 * np.sum(np.sin(45 * np.pi * x_scaled) * np.cos(40 * np.pi * x_scaled)) + \
                   0.08 * np.sum(np.sin(65 * np.pi * x_scaled**2) * np.cos(60 * np.pi * x_scaled**2))
        
        # Modified hyper-chaotic component with different scaling
        hyper_chaotic = 0.05 * np.sum(np.sin(20 * r**3.2) * np.cos(18 * r**3.2) + 
                                    0.4 * np.sin(25 * r**2.9) * np.cos(22 * r**2.9) + 
                                    0.2 * np.sin(30 * r**2.5))
        
        # Self-similar component with different power-law scaling
        self_similar = 0.06 * np.sum(np.sin(9 * np.pi * x_scaled**1.4) * np.cos(7 * np.pi * x_scaled**1.4) + 
                                   0.25 * np.sin(14 * np.pi * x_scaled**0.6) * np.cos(11 * np.pi * x_scaled**0.6))
        
        # Quaternion-like chaotic interaction term with adjusted parameters
        quat_interaction = 0.04 * np.sum(np.sin(15 * r**2.9) * np.cos(13 * r**2.9) + 
                                       0.25 * np.sin(20 * r**2.2) * np.cos(17 * r**2.2) + 
                                       0.2 * np.sin(25 * r**2.0))
        
        # Increased fractal dimensionality with modified complexity
        fractal_dim = 0.1 * np.sum(np.sin(28 * np.pi * x_scaled**1.8) * np.cos(24 * np.pi * x_scaled**1.5) + 
                                  0.3 * np.sin(35 * np.pi * x_scaled**1.2) * np.cos(32 * np.pi * x_scaled**1.0))
        
        # Enhanced cross-dimensional coupling with adaptive weights
        enhanced_cross = 0.2 * np.sum((x_scaled[:-1] * x_scaled[1:]) * np.sin(2.5 * np.pi * (x_scaled[:-1]**2 - x_scaled[1:]**2)))
        
        # Additional multi-scale oscillatory component for greater multimodality
        multi_scale_osc = 0.08 * np.sum(np.sin(55 * np.pi * x_scaled**0.7) * np.cos(50 * np.pi * x_scaled**0.8) + 
                                       0.15 * np.sin(70 * np.pi * x_scaled**0.5) * np.cos(65 * np.pi * x_scaled**0.4))
        
        # Combine all components with optimized weights for better fitness
        return 0.3 * radial + 0.25 * trig + 0.2 * exp_interaction + 0.18 * chaotic + 0.1 * multimodal + 0.08 * cross_coupling + 0.06 * fractal_noise + 0.04 * high_freq + 0.05 * hyper_chaotic + 0.06 * self_similar + 0.03 * quat_interaction + 0.1 * fractal_dim + 0.07 * enhanced_cross + 0.05 * multi_scale_osc