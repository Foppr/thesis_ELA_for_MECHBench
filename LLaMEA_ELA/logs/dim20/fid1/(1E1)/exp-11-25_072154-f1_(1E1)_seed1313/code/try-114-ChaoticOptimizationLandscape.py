import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with modified exponential and polynomial terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) + 0.6 * np.exp(-0.3 * r**2) * np.sin(5 * r) + 
                 0.25 * np.exp(-0.1 * r**3) * np.cos(4 * r)) * (1 + 0.35 * np.sin(8 * r))
        
        # Multi-frequency trigonometric complexity with stronger cross-dimensional coupling
        trig = np.sum(np.cos(7 * np.pi * x_scaled) * np.sin(8 * np.pi * x_scaled) + 
                     0.7 * np.sin(5 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) + 
                     0.35 * np.cos(9 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled))
        
        # Multi-scale exponential interaction terms with enhanced long-range coupling
        exp_interaction = np.sum(np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                               0.9 * np.exp(-0.2 * (x_scaled[:-2] - x_scaled[2:])**2) + 
                               0.45 * np.exp(-0.05 * (x_scaled[:-3] - x_scaled[3:])**2))
        
        # Nested chaotic component with modified fractional power radial dependence
        chaotic = np.sum(np.sin(10 * r**2.5) * np.cos(7 * r**2.5) + 
                        0.45 * np.sin(15 * r**1.8) * np.cos(12 * r**1.8) + 
                        0.25 * np.sin(20 * r**1.2))
        
        # Highly multi-modal component with enhanced frequency modulation
        multimodal = 0.65 * np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled)) + \
                    0.35 * np.sum(np.sin(12 * np.pi * x_scaled)**2 + 
                                0.55 * np.sin(8 * np.pi * x_scaled)**3) + \
                    0.15 * np.sum(np.sin(25 * np.pi * x_scaled) * np.cos(20 * np.pi * x_scaled))
        
        # Enhanced cross-dimensional coupling term with increased complexity
        cross_coupling = 0.25 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(2 * np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Fractal noise component with modified fractional Brownian motion characteristics
        fractal_noise = 0.18 * np.sum(np.sin(13 * np.pi * x_scaled**1.7) * np.cos(11 * np.pi * x_scaled**1.3)) + \
                       0.12 * np.sum(np.sin(22 * np.pi * x_scaled**0.9) * np.cos(18 * np.pi * x_scaled**1.1))
        
        # High-frequency oscillatory terms with increased multimodality
        high_freq = 0.09 * np.sum(np.sin(50 * np.pi * x_scaled) * np.cos(45 * np.pi * x_scaled)) + \
                   0.07 * np.sum(np.sin(70 * np.pi * x_scaled**2) * np.cos(65 * np.pi * x_scaled**2))
        
        # Novel hyper-chaotic component with modified quaternion-like interactions
        hyper_chaotic = 0.045 * np.sum(np.sin(25 * r**3) * np.cos(20 * r**3) + 
                                    0.35 * np.sin(30 * r**2.7) * np.cos(25 * r**2.7) + 
                                    0.12 * np.sin(35 * r**2.3))
        
        # Multi-scale self-similar component with modified power-law scaling
        self_similar = 0.06 * np.sum(np.sin(10 * np.pi * x_scaled**1.5) * np.cos(8 * np.pi * x_scaled**1.5) + 
                                   0.22 * np.sin(15 * np.pi * x_scaled**0.7) * np.cos(12 * np.pi * x_scaled**0.7))
        
        # Quaternion-like chaotic interaction term with modified parameters
        quat_interaction = 0.035 * np.sum(np.sin(18 * r**2.8) * np.cos(14 * r**2.8) + 
                                       0.22 * np.sin(22 * r**2.1) * np.cos(19 * r**2.1) + 
                                       0.17 * np.sin(26 * r**1.9))
        
        # Increased fractal dimensionality with enhanced complexity
        fractal_dim = 0.09 * np.sum(np.sin(30 * np.pi * x_scaled**1.9) * np.cos(25 * np.pi * x_scaled**1.6) + 
                                  0.28 * np.sin(40 * np.pi * x_scaled**1.3) * np.cos(35 * np.pi * x_scaled**1.1))
        
        # Enhanced cross-dimensional coupling with adaptive weights
        enhanced_cross = 0.17 * np.sum((x_scaled[:-1] * x_scaled[1:]) * np.sin(3 * np.pi * (x_scaled[:-1]**2 - x_scaled[1:]**2)))
        
        # Multi-scale oscillatory component for greater multimodality
        multi_scale_osc = 0.07 * np.sum(np.sin(60 * np.pi * x_scaled**0.8) * np.cos(55 * np.pi * x_scaled**0.9) + 
                                       0.14 * np.sin(75 * np.pi * x_scaled**0.6) * np.cos(70 * np.pi * x_scaled**0.5))
        
        # Improved algorithm discrimination component
        adaptive_component = 0.035 * np.sum(np.sin(40 * np.pi * x_scaled**1.2) * np.cos(35 * np.pi * x_scaled**1.4) + 
                                          0.20 * np.sin(50 * np.pi * x_scaled**0.9) * np.cos(45 * np.pi * x_scaled**1.1))
        
        # Enhanced cross-dimensional term with varying coupling strength
        varying_coupling = 0.14 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(4 * np.pi * (x_scaled[:-1] + x_scaled[1:])))
        
        # Combine all components with optimized weights for better algorithm discrimination
        return 0.27 * radial + 0.22 * trig + 0.20 * exp_interaction + 0.17 * chaotic + 0.09 * multimodal + 0.07 * cross_coupling + 0.06 * fractal_noise + 0.04 * high_freq + 0.05 * hyper_chaotic + 0.06 * self_similar + 0.03 * quat_interaction + 0.09 * fractal_dim + 0.07 * enhanced_cross + 0.05 * multi_scale_osc + 0.04 * adaptive_component + 0.06 * varying_coupling