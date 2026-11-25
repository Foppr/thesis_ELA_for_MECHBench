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
            # Higher frequency chaotic pattern with exponential decay
            for k in range(1, 8):  # Increased recursion depth
                chaotic_term += (0.9 ** k) * np.sin(3 ** k * np.pi * xi) * np.cos(4 ** k * xi)
        
        # Extended spherical harmonic coupling with additional angular components
        harmonic_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Spherical harmonic with multiple angular frequencies
            harmonic_term += (xi**2 + 0.6 * np.sin(5 * xi) + 0.4 * np.cos(7 * xi) + 
                             0.3 * np.sin(9 * xi)) * \
                            (1 + 0.3 * np.sin(3 * xi) * np.cos(4 * xi) + 0.2 * np.sin(6 * xi))
        
        # Stronger gradient asymmetry with non-linear modulation
        grad_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Asymmetric gradient field with higher-order polynomial
            mod_factor = 1.0 + 0.7 * np.sin(i * np.pi / self.dim) + 0.3 * np.cos(i * np.pi / self.dim)
            grad_term += (xi**5 + 0.9 * xi**4 - 0.7 * xi**3 + 0.5 * xi**2) * mod_factor
            
        # Cross-dimensional coupling with spherical distance metric
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Spherical distance with chaotic scaling
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.1 * np.sin(3 * (x_norm[i] + x_norm[j])))
                spherical_dist = dist * (1 + 0.5 * np.sin(8 * dist))
                coupling = np.exp(-spherical_dist**2) * (1 + 0.6 * np.cos(9 * spherical_dist))
                cross_term += coupling * (x_norm[i]**3 + x_norm[j]**3)
        
        # Additional high-frequency oscillatory components
        high_freq_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple high-frequency components with varying amplitudes and phases
            high_freq_term += (0.8 * np.sin(10 * xi) + 0.6 * np.sin(15 * xi) + 
                              0.4 * np.sin(20 * xi) + 0.2 * np.sin(25 * xi)) * \
                             (1 + 0.2 * np.cos(5 * xi) + 0.1 * np.sin(8 * xi))
        
        # Combine all components with enhanced weights
        result = 2.0 * chaotic_term + 1.5 * harmonic_term + 1.3 * grad_term + \
                1.0 * cross_term + 1.7 * high_freq_term
        
        # Add chaotic noise for increased complexity
        noise = np.random.normal(0, 0.002) * (1 + 0.5 * np.sin(np.sum(x_norm)))
        
        return result + noise