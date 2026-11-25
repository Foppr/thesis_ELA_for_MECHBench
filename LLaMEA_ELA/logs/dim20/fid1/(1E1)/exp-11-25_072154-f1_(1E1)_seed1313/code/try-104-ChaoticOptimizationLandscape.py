import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with nested exponential and polynomial terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) + 0.5 * np.exp(-0.3 * r**2) * np.sin(5 * r) + 
                 0.2 * np.exp(-0.1 * r**3) * np.cos(4 * r)) * (1 + 0.3 * np.sin(8 * r))
        
        # Multi-frequency trigonometric complexity with cross-dimensional coupling
        trig = np.sum(np.cos(7 * np.pi * x_scaled) * np.sin(8 * np.pi * x_scaled) + 
                     0.6 * np.sin(5 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) + 
                     0.3 * np.cos(9 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled))
        
        # Multi-scale exponential interaction terms with long-range coupling
        exp_interaction = np.sum(np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                               0.8 * np.exp(-0.2 * (x_scaled[:-2] - x_scaled[2:])**2) + 
                               0.4 * np.exp(-0.05 * (x_scaled[:-3] - x_scaled[3:])**2))
        
        # Nested chaotic component with fractional power radial dependence
        chaotic = np.sum(np.sin(10 * r**2.5) * np.cos(7 * r**2.5) + 
                        0.4 * np.sin(15 * r**1.8) * np.cos(12 * r**1.8) + 
                        0.2 * np.sin(20 * r**1.2))
        
        # Highly multi-modal component with adaptive frequency modulation
        multimodal = 0.6 * np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled)) + \
                    0.3 * np.sum(np.sin(12 * np.pi * x_scaled)**2 + 
                                0.5 * np.sin(8 * np.pi * x_scaled)**3) + \
                    0.1 * np.sum(np.sin(25 * np.pi * x_scaled) * np.cos(20 * np.pi * x_scaled))
        
        # Add a cross-dimensional coupling term for increased complexity
        cross_coupling = 0.2 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(2 * np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Fractal noise component using fractional Brownian motion characteristics
        fractal_noise = 0.15 * np.sum(np.sin(13 * np.pi * x_scaled**1.7) * np.cos(11 * np.pi * x_scaled**1.3)) + \
                       0.1 * np.sum(np.sin(22 * np.pi * x_scaled**0.9) * np.cos(18 * np.pi * x_scaled**1.1))
        
        # High-frequency oscillatory terms to increase multimodality and complexity
        high_freq = 0.08 * np.sum(np.sin(50 * np.pi * x_scaled) * np.cos(45 * np.pi * x_scaled)) + \
                   0.06 * np.sum(np.sin(70 * np.pi * x_scaled**2) * np.cos(65 * np.pi * x_scaled**2))
        
        # Add a novel hyper-chaotic component with quaternion-like interactions
        hyper_chaotic = 0.04 * np.sum(np.sin(25 * r**3) * np.cos(20 * r**3) + 
                                    0.3 * np.sin(30 * r**2.7) * np.cos(25 * r**2.7) + 
                                    0.1 * np.sin(35 * r**2.3))
        
        # Add a new multi-scale self-similar component with power-law scaling
        self_similar = 0.05 * np.sum(np.sin(10 * np.pi * x_scaled**1.5) * np.cos(8 * np.pi * x_scaled**1.5) + 
                                   0.2 * np.sin(15 * np.pi * x_scaled**0.7) * np.cos(12 * np.pi * x_scaled**0.7))
        
        # Add a novel quaternion-like chaotic interaction term
        quat_interaction = 0.03 * np.sum(np.sin(18 * r**2.8) * np.cos(14 * r**2.8) + 
                                       0.2 * np.sin(22 * r**2.1) * np.cos(19 * r**2.1) + 
                                       0.15 * np.sin(26 * r**1.9))
        
        # Introduce additional fractal dimensionality with increased complexity
        fractal_dim = 0.08 * np.sum(np.sin(30 * np.pi * x_scaled**1.9) * np.cos(25 * np.pi * x_scaled**1.6) + 
                                  0.25 * np.sin(40 * np.pi * x_scaled**1.3) * np.cos(35 * np.pi * x_scaled**1.1))
        
        # Enhanced cross-dimensional coupling with adaptive weights
        enhanced_cross = 0.15 * np.sum((x_scaled[:-1] * x_scaled[1:]) * np.sin(3 * np.pi * (x_scaled[:-1]**2 - x_scaled[1:]**2)))
        
        # Add a new multi-scale oscillatory component for greater multimodality
        multi_scale_osc = 0.06 * np.sum(np.sin(60 * np.pi * x_scaled**0.8) * np.cos(55 * np.pi * x_scaled**0.9) + 
                                       0.12 * np.sin(75 * np.pi * x_scaled**0.6) * np.cos(70 * np.pi * x_scaled**0.5))
        
        # Add a new component for improved algorithm discrimination
        adaptive_component = 0.03 * np.sum(np.sin(40 * np.pi * x_scaled**1.2) * np.cos(35 * np.pi * x_scaled**1.4) + 
                                          0.18 * np.sin(50 * np.pi * x_scaled**0.9) * np.cos(45 * np.pi * x_scaled**1.1))
        
        # Add a new cross-dimensional term with varying coupling strength
        varying_coupling = 0.12 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(4 * np.pi * (x_scaled[:-1] + x_scaled[1:])))
        
        # Additional chaotic component with higher frequency oscillations
        high_freq_chaos = 0.07 * np.sum(np.sin(80 * np.pi * x_scaled**1.3) * np.cos(75 * np.pi * x_scaled**1.4))
        
        # Add a new fractal-like interaction term with complex coupling
        fractal_coupling = 0.09 * np.sum(np.sin(28 * np.pi * x_scaled**1.8) * np.cos(24 * np.pi * x_scaled**1.9) + 
                                        0.22 * np.sin(35 * np.pi * x_scaled**1.6) * np.cos(32 * np.pi * x_scaled**1.7))
        
        # Introduce a new multi-scale power-law component with variable exponents
        power_law = 0.05 * np.sum(x_scaled**2.3 * np.sin(30 * np.pi * x_scaled) + 
                                0.15 * x_scaled**1.9 * np.cos(25 * np.pi * x_scaled))
        
        # Add a new hyper-chaotic term with cubic radial dependence
        cubic_chaos = 0.04 * np.sum(np.sin(35 * r**3.2) * np.cos(30 * r**3.2) + 
                                  0.25 * np.sin(40 * r**2.9) * np.cos(35 * r**2.9))
        
        # Combine all components with optimized weights
        return 0.25 * radial + 0.2 * trig + 0.18 * exp_interaction + 0.15 * chaotic + 0.08 * multimodal + 0.06 * cross_coupling + 0.05 * fractal_noise + 0.03 * high_freq + 0.04 * hyper_chaotic + 0.05 * self_similar + 0.02 * quat_interaction + 0.08 * fractal_dim + 0.06 * enhanced_cross + 0.04 * multi_scale_osc + 0.03 * adaptive_component + 0.05 * varying_coupling + 0.07 * high_freq_chaos + 0.09 * fractal_coupling + 0.05 * power_law + 0.04 * cubic_chaos