import numpy as np

class MultiModalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Quadratic radial basins with periodic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_basin = 0.5 * r**2 + 0.3 * np.sin(10 * r) + 0.2 * np.cos(8 * r)
        
        # Multi-modal sinusoidal components with varying frequencies
        modal_components = np.sum(np.sin(15 * x_scaled) * np.cos(12 * x_scaled) + 
                                0.7 * np.sin(20 * x_scaled) * np.cos(18 * x_scaled) + 
                                0.4 * np.sin(25 * x_scaled) * np.cos(22 * x_scaled))
        
        # Cross-dimensional coupling with interaction weights
        cross_dim = np.sum((x_scaled[:-1] * x_scaled[1:]) * np.sin(5 * (x_scaled[:-1] + x_scaled[1:])))
        
        # Periodic boundary effect with enhanced complexity
        periodic_effect = np.sum(np.sin(30 * x_scaled) * np.cos(28 * x_scaled) + 
                               0.6 * np.sin(35 * x_scaled) * np.cos(32 * x_scaled))
        
        # Fractional power radial interaction terms
        fractional_interaction = np.sum((np.abs(x_scaled)**1.7) * np.sin(4 * np.abs(x_scaled)) + 
                                      0.5 * (np.abs(x_scaled)**1.3) * np.cos(3 * np.abs(x_scaled)))
        
        # Multi-scale oscillatory landscape with self-similarity
        multiscale = 0.8 * np.sum(np.sin(50 * x_scaled**0.9) * np.cos(45 * x_scaled**0.8) + 
                                0.3 * np.sin(60 * x_scaled**0.7) * np.cos(55 * x_scaled**0.6))
        
        # Add a novel hyper-chaotic component with complex frequency modulation
        hyperchaos = 0.2 * np.sum(np.sin(40 * r**1.5) * np.cos(35 * r**1.5) + 
                                0.15 * np.sin(45 * r**1.3) * np.cos(40 * r**1.3))
        
        # Combine all components with optimized weights
        return 0.3 * radial_basin + 0.25 * modal_components + 0.15 * cross_dim + 0.1 * periodic_effect + 0.1 * fractional_interaction + 0.08 * multiscale + 0.02 * hyperchaos