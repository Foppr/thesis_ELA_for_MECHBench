import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Enhanced chaotic component with higher frequency oscillations
        chaotic_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Higher frequency chaotic pattern with exponential growth
            for k in range(1, 8):  # Increased recursion depth
                chaotic_term += (0.9 ** k) * np.sin(2 ** k * np.pi * xi) * np.cos(4 ** k * xi)
        
        # Spherical harmonic coupling with increased complexity
        spherical_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-frequency spherical harmonic components
            spherical_term += (xi**2 + 0.3 * np.sin(3 * xi) + 0.2 * np.cos(5 * xi) + 
                              0.1 * np.sin(7 * xi)) * (1 + 0.3 * np.sin(2 * xi) * np.cos(4 * xi))
        
        # Enhanced gradient field with stronger asymmetry
        grad_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Stronger asymmetric gradient with dimension-dependent scaling
            mod_factor = 1.0 + 0.7 * np.sin(i * np.pi / self.dim)  # Increased modulation
            grad_term += (xi**5 + 0.9 * xi**4 - 0.7 * xi**3 + 0.5 * xi**2) * mod_factor
            
        # Cross-dimensional coupling with chaotic scaling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic distance metric with exponential decay
                dist = np.abs(x_norm[i] - x_norm[j])
                chaotic_dist = dist * (1 + 0.5 * np.sin(8 * dist) * np.cos(6 * dist))  # Increased complexity
                coupling = np.exp(-chaotic_dist**3) * (1 + 0.5 * np.cos(9 * chaotic_dist))  # Cubic decay
                cross_term += coupling * (x_norm[i]**2 + x_norm[j]**2)
        
        # High-frequency periodic modulation with complex amplitude variations
        periodic_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple high-frequency components with varying amplitudes and phases
            periodic_term += (0.6 * np.sin(3 * xi) + 0.4 * np.sin(7 * xi) + 
                             0.3 * np.sin(11 * xi) + 0.2 * np.sin(15 * xi)) * \
                            (1 + 0.2 * np.cos(4 * xi) * np.sin(5 * xi))
        
        # Additional high-frequency oscillatory components
        high_freq_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Ultra-high frequency components
            high_freq_term += (0.1 * np.sin(20 * xi) + 0.05 * np.cos(25 * xi) + 
                              0.03 * np.sin(30 * xi)) * (1 + 0.1 * np.sin(8 * xi))
        
        # Combine all components with adjusted weights for better balance
        result = 2.0 * chaotic_term + 1.5 * spherical_term + 1.3 * grad_term + \
                1.0 * cross_term + 1.2 * periodic_term + 0.8 * high_freq_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise