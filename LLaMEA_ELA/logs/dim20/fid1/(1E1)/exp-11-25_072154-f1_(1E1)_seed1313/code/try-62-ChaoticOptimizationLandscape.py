import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with modified exponential and polynomial terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) + 0.6 * np.exp(-0.2 * r**2) * np.sin(6 * r) + 
                 0.3 * np.exp(-0.15 * r**3) * np.cos(5 * r)) * (1 + 0.4 * np.sin(9 * r))
        
        # Multi-frequency trigonometric complexity with enhanced cross-dimensional coupling
        trig = np.sum(np.cos(8 * np.pi * x_scaled) * np.sin(9 * np.pi * x_scaled) + 
                     0.7 * np.sin(6 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) + 
                     0.4 * np.cos(10 * np.pi * x_scaled) * np.sin(4 * np.pi * x_scaled))
        
        # Multi-scale exponential interaction terms with improved long-range coupling
        exp_interaction = np.sum(np.exp(-0.4 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                               0.9 * np.exp(-0.15 * (x_scaled[:-2] - x_scaled[2:])**2) + 
                               0.5 * np.exp(-0.03 * (x_scaled[:-3] - x_scaled[3:])**2))
        
        # Nested chaotic component with modified fractional power radial dependence
        chaotic = np.sum(np.sin(12 * r**2.3) * np.cos(9 * r**2.3) + 
                        0.5 * np.sin(18 * r**1.7) * np.cos(15 * r**1.7) + 
                        0.3 * np.sin(25 * r**1.4))
        
        # Highly multi-modal component with enhanced frequency modulation
        multimodal = 0.7 * np.sum(np.sin(4 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled)) + \
                    0.4 * np.sum(np.sin(15 * np.pi * x_scaled)**2 + 
                                0.6 * np.sin(10 * np.pi * x_scaled)**3) + \
                    0.2 * np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(25 * np.pi * x_scaled))
        
        # Enhanced cross-dimensional coupling term for increased complexity
        cross_coupling = 0.3 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(3 * np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Fractal noise component with modified fractional Brownian motion characteristics
        fractal_noise = 0.2 * np.sum(np.sin(15 * np.pi * x_scaled**1.6) * np.cos(13 * np.pi * x_scaled**1.4)) + \
                       0.15 * np.sum(np.sin(25 * np.pi * x_scaled**0.8) * np.cos(20 * np.pi * x_scaled**1.2))
        
        # High-frequency oscillatory terms with modified amplitudes and frequencies
        high_freq = 0.1 * np.sum(np.sin(60 * np.pi * x_scaled) * np.cos(55 * np.pi * x_scaled)) + \
                   0.08 * np.sum(np.sin(80 * np.pi * x_scaled**2) * np.cos(75 * np.pi * x_scaled**2))
        
        # Hyper-chaotic component with modified quaternion-like interactions
        hyper_chaotic = 0.05 * np.sum(np.sin(30 * r**3) * np.cos(25 * r**3) + 
                                    0.4 * np.sin(35 * r**2.8) * np.cos(30 * r**2.8) + 
                                    0.2 * np.sin(40 * r**2.2))
        
        # Multi-scale self-similar component with power-law scaling
        self_similar = 0.06 * np.sum(np.sin(12 * np.pi * x_scaled**1.4) * np.cos(10 * np.pi * x_scaled**1.4) + 
                                   0.3 * np.sin(18 * np.pi * x_scaled**0.6) * np.cos(15 * np.pi * x_scaled**0.6))
        
        # Add a novel component for enhanced complexity
        novel_component = 0.07 * np.sum(np.sin(20 * np.pi * x_scaled**1.3) * np.cos(18 * np.pi * x_scaled**1.1))
        
        # Combine all components with optimized weights
        return 0.22 * radial + 0.18 * trig + 0.2 * exp_interaction + 0.16 * chaotic + 0.09 * multimodal + 0.07 * cross_coupling + 0.06 * fractal_noise + 0.04 * high_freq + 0.05 * hyper_chaotic + 0.06 * self_similar + 0.03 * novel_component