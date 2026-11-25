import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map chaotic component with varying r parameters
        logistic = np.sum(4.0 * x_scaled * (1.0 - x_scaled))
        
        # Spherical harmonics with mixed degrees and azimuthal frequencies
        sph_harmonics = np.sum(
            np.sin(3.0 * np.sqrt(np.sum(x_scaled**2, axis=0))) * 
            np.cos(2.0 * np.arctan2(x_scaled[1], x_scaled[0])) +
            0.5 * np.cos(4.0 * np.sqrt(np.sum(x_scaled**2, axis=0))) * 
            np.sin(3.0 * np.arctan2(x_scaled[1], x_scaled[0]))
        )
        
        # Asymmetric polynomial potentials with mixed exponents
        poly_potential = np.sum(
            0.8 * x_scaled**5 + 1.2 * x_scaled**3 - 0.5 * x_scaled**2 + 
            0.3 * np.abs(x_scaled) + 0.7 * x_scaled**4
        )
        
        # Cross-dimensional coupling with trigonometric interaction
        cross_coupling = np.sum(
            np.sin(2.0 * (x_scaled[:-1] + x_scaled[1:])) * 
            np.cos(1.5 * (x_scaled[:-1] - x_scaled[1:])) +
            0.6 * np.tan(0.5 * (x_scaled[:-2] + x_scaled[2:]))
        )
        
        # Multi-scale exponential decay with sinusoidal modulation
        exp_decay = np.sum(
            np.exp(-2.0 * np.abs(x_scaled)) * 
            (1.0 + 0.3 * np.sin(5.0 * x_scaled) + 0.2 * np.cos(7.0 * x_scaled))
        )
        
        # Asymmetric noise injection with chaotic modulation
        noise = np.sum(
            0.4 * np.sin(8.0 * x_scaled) * np.exp(-0.5 * x_scaled**2) +
            0.3 * np.cos(6.0 * x_scaled) * np.exp(-0.3 * np.abs(x_scaled))
        )
        
        # Combine all components with adaptive weights
        return (0.4 * logistic + 
                0.3 * sph_harmonics + 
                0.2 * poly_potential + 
                0.1 * cross_coupling + 
                0.08 * exp_decay + 
                0.05 * noise + 
                2.1)