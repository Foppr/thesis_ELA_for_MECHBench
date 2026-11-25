import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic sine-wave interactions with varying amplitudes and phases
        chaotic_waves = 0
        for i in range(self.dim):
            chaotic_waves += np.sin(10 * np.sin(5 * x[i])) * np.cos(7 * np.cos(3 * x[i])) + \
                           np.cos(8 * np.sin(4 * x[i])) * np.sin(6 * np.cos(2 * x[i]))
            
        # Radial exponential barriers with multiple local minima
        radial_barrier = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            radial_barrier += np.exp(-0.5 * (dist_from_origin - 1)**2) * \
                            np.sin(3 * dist_from_origin)**4 + \
                            np.exp(-0.3 * (dist_from_origin - 3)**2) * \
                            np.cos(5 * dist_from_origin)**3
            
        # Cross-dimensional polynomial couplings with high-order interactions
        poly_couplings = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_couplings += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * \
                                (x[i]**2 + x[j]**2) * np.cos(x[i] + x[j])
                
        # Spherical penalty regions with irregular local minima
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 15 * (1 - np.exp(-0.2 * (dist_from_origin - 2.5)**2)) * \
                      np.sin(4 * dist_from_origin)**3 + \
                      5 * (1 - np.exp(-0.1 * (dist_from_origin - 4)**2)) * \
                      np.cos(6 * dist_from_origin)**2
        
        # Add a global scaling factor and combine all components
        return 1.2 * (chaotic_waves + radial_barrier + poly_couplings + penalty)