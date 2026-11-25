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
                 0.15 * np.exp(-0.1 * r**3) * np.cos(4 * r)) * (1 + 0.25 * np.sin(8 * r))
        
        # Multi-frequency trigonometric complexity with altered coupling
        trig = np.sum(np.cos(6 * np.pi * x_scaled) * np.sin(7 * np.pi * x_scaled) + 
                     0.5 * np.sin(4 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) + 
                     0.25 * np.cos(8 * np.pi * x_scaled) * np.sin(2 * np.pi * x_scaled))
        
        # Multi-scale exponential interaction terms with modified coupling
        exp_interaction = np.sum(np.exp(-0.4 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                               0.7 * np.exp(-0.15 * (x_scaled[:-2] - x_scaled[2:])**2) + 
                               0.3 * np.exp(-0.03 * (x_scaled[:-3] - x_scaled[3:])**2))
        
        # Modified chaotic component with different power radial dependence
        chaotic = np.sum(np.sin(9 * r**2.3) * np.cos(6 * r**2.3) + 
                        0.35 * np.sin(14 * r**1.7) * np.cos(11 * r**1.7) + 
                        0.18 * np.sin(19 * r**1.1))
        
        # Modified multi-modal component with altered frequency modulation
        multimodal = 0.5 * np.sum(np.sin(2.5 * np.pi * x_scaled) * np.cos(2.5 * np.pi * x_scaled)) + \
                    0.25 * np.sum(np.sin(11 * np.pi * x_scaled)**2 + 
                                0.4 * np.sin(7 * np.pi * x_scaled)**3) + \
                    0.08 * np.sum(np.sin(24 * np.pi * x_scaled) * np.cos(19 * np.pi * x_scaled))
        
        # Altered cross-dimensional coupling term with enhanced nonlinearity
        cross_coupling = 0.15 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(1.5 * np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Modified fractal noise component with increased complexity
        fractal_noise = 0.12 * np.sum(np.sin(12 * np.pi * x_scaled**1.6) * np.cos(10 * np.pi * x_scaled**1.2)) + \
                       0.09 * np.sum(np.sin(21 * np.pi * x_scaled**0.8) * np.cos(17 * np.pi * x_scaled**1.0))
        
        # Modified high-frequency oscillatory terms with altered amplitudes
        high_freq = 0.07 * np.sum(np.sin(45 * np.pi * x_scaled) * np.cos(40 * np.pi * x_scaled)) + \
                   0.05 * np.sum(np.sin(65 * np.pi * x_scaled**2) * np.cos(60 * np.pi * x_scaled**2))
        
        # Modified hyper-chaotic component with additional frequency terms
        hyper_chaotic = 0.03 * np.sum(np.sin(24 * r**3) * np.cos(19 * r**3) + 
                                    0.25 * np.sin(29 * r**2.6) * np.cos(24 * r**2.6) + 
                                    0.08 * np.sin(34 * r**2.2))
        
        # Modified self-similar component with enhanced dimensionality
        self_similar = 0.04 * np.sum(np.sin(9 * np.pi * x_scaled**1.4) * np.cos(7 * np.pi * x_scaled**1.4) + 
                                   0.18 * np.sin(14 * np.pi * x_scaled**0.6) * np.cos(11 * np.pi * x_scaled**0.6))
        
        # Modified quaternion-like chaotic interaction term with increased coupling
        quat_interaction = 0.025 * np.sum(np.sin(17 * r**2.7) * np.cos(13 * r**2.7) + 
                                       0.18 * np.sin(21 * r**2.0) * np.cos(18 * r**2.0) + 
                                       0.12 * np.sin(25 * r**1.8))
        
        # Modified fractal dimensionality component with increased complexity
        fractal_dim = 0.07 * np.sum(np.sin(29 * np.pi * x_scaled**1.8) * np.cos(24 * np.pi * x_scaled**1.5) + 
                                  0.22 * np.sin(39 * np.pi * x_scaled**1.2) * np.cos(34 * np.pi * x_scaled**1.0))
        
        # Enhanced cross-dimensional coupling with adaptive scaling
        enhanced_cross = 0.13 * np.sum((x_scaled[:-1] * x_scaled[1:]) * np.sin(2.5 * np.pi * (x_scaled[:-1]**2 - x_scaled[1:]**2)))
        
        # Modified multi-scale oscillatory component with increased frequency diversity
        multi_scale_osc = 0.05 * np.sum(np.sin(55 * np.pi * x_scaled**0.7) * np.cos(50 * np.pi * x_scaled**0.8) + 
                                       0.1 * np.sin(70 * np.pi * x_scaled**0.5) * np.cos(65 * np.pi * x_scaled**0.4))
        
        # Modified adaptive component with enhanced nonlinearity
        adaptive_component = 0.025 * np.sum(np.sin(39 * np.pi * x_scaled**1.1) * np.cos(34 * np.pi * x_scaled**1.3) + 
                                          0.16 * np.sin(49 * np.pi * x_scaled**0.8) * np.cos(44 * np.pi * x_scaled**1.0))
        
        # Modified varying coupling term with increased sensitivity
        varying_coupling = 0.1 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * np.sin(3.5 * np.pi * (x_scaled[:-1] + x_scaled[1:])))
        
        # Additional high-dimensional fractal component with modified interaction
        fractal_high_dim = 0.08 * np.sum(np.sin(42 * np.pi * x_scaled**1.9) * np.cos(37 * np.pi * x_scaled**1.3) + 
                                       0.25 * np.sin(51 * np.pi * x_scaled**1.1) * np.cos(46 * np.pi * x_scaled**1.4))
        
        # Modified multi-scale chaotic interaction with enhanced coupling
        multi_scale_chaotic = 0.03 * np.sum(np.sin(33 * r**2.9) * np.cos(28 * r**2.9) + 
                                          0.22 * np.sin(38 * r**2.4) * np.cos(33 * r**2.4) + 
                                          0.15 * np.sin(43 * r**2.1))
        
        # Enhanced hyper-chaotic coupling with higher dimensional interactions
        hyper_chaotic_coupled = 0.05 * np.sum(np.sin(37 * r**3.2) * np.cos(32 * r**3.2) + 
                                            0.18 * np.sin(41 * r**2.8) * np.cos(36 * r**2.8) + 
                                            0.1 * np.sin(45 * r**2.5))
        
        # Modified additional chaotic component with enhanced complexity
        additional_chaotic = 0.02 * np.sum(np.sin(50 * r**2.5) * np.cos(45 * r**2.5) + 
                                         0.15 * np.sin(55 * r**2.0) * np.cos(50 * r**2.0))
        
        # Modified multi-modal component with enhanced diversity
        multimodal_enhanced = 0.3 * np.sum(np.sin(3.0 * np.pi * x_scaled)**2 + 
                                         0.2 * np.sin(9.0 * np.pi * x_scaled)**3 + 
                                         0.1 * np.sin(15.0 * np.pi * x_scaled)**4)
        
        # Combined with new interaction terms for increased complexity and improved discrimination
        return (0.24 * radial + 0.19 * trig + 0.17 * exp_interaction + 0.14 * chaotic + 
                0.07 * multimodal + 0.05 * cross_coupling + 0.04 * fractal_noise + 
                0.025 * high_freq + 0.035 * hyper_chaotic + 0.045 * self_similar + 
                0.018 * quat_interaction + 0.07 * fractal_dim + 0.055 * enhanced_cross + 
                0.035 * multi_scale_osc + 0.025 * adaptive_component + 0.045 * varying_coupling + 
                0.06 * fractal_high_dim + 0.04 * multi_scale_chaotic + 0.05 * hyper_chaotic_coupled +
                0.03 * additional_chaotic + 0.08 * multimodal_enhanced)