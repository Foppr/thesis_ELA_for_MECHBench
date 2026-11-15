import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested harmonic oscillators with frequency modulation
        harmonic = np.sum(np.sin(2 * np.pi * x_norm * (1 + 0.5 * np.sin(3 * x_norm))) + 
                         0.5 * np.sin(4 * np.pi * x_norm * (1 + 0.3 * np.cos(2 * x_norm))))
        
        # Polynomial chaos with mixed exponents and cross-terms
        poly_chaos = np.sum(x_norm**4 + 0.8 * x_norm**3 + 0.6 * x_norm**2 + 0.4 * x_norm + 
                           0.2 * x_norm[:-1]**2 * x_norm[1:] + 0.1 * x_norm[:-1] * x_norm[1:]**2)
        
        # Adaptive radial basis functions with dimension-dependent widths
        rbf_adaptive = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            center = 0.3 * np.cos(i * np.pi / self.dim)
            rbf_adaptive += np.exp(-width * (x_norm[i] - center)**2)
        
        # Coupled sine-wave components with dynamic phase shifts
        coupled_sine = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                phase_shift = 0.1 * np.sin(x_norm[i] + x_norm[i+1])
                coupled_sine += np.sin(10 * x_norm[i] + phase_shift) * np.cos(15 * x_norm[i+1] + phase_shift)
        
        # Fractional polynomial interactions with varying degrees
        frac_poly = np.sum(np.abs(x_norm[:-1])**1.5 * np.abs(x_norm[1:])**2.5 + 
                          np.abs(x_norm[:-1])**2.5 * np.abs(x_norm[1:])**1.5)
        
        # Multi-scale exponential decay with adaptive rates
        exp_decay = np.sum(np.exp(-2.0 * np.abs(x_norm)) + 0.5 * np.exp(-5.0 * np.abs(x_norm)) + 
                          0.2 * np.exp(-10.0 * np.abs(x_norm)))
        
        # Asymmetric power-law component with dynamic exponent
        asym_power = 0.0
        for i in range(self.dim):
            exponent = 1.5 + 0.5 * np.sin(i * np.pi / self.dim)
            asym_power += np.abs(x_norm[i])**exponent * np.sign(x_norm[i])
        
        # Dynamic noise component that varies with dimensionality
        noise = 0.001 * np.random.random() * (1.0 + 0.1 * self.dim)
        
        # Combine all components with adaptive weights
        return (0.2 * harmonic + 
                0.15 * poly_chaos + 
                0.15 * rbf_adaptive + 
                0.1 * coupled_sine + 
                0.1 * frac_poly + 
                0.1 * exp_decay + 
                0.08 * asym_power + 
                noise)