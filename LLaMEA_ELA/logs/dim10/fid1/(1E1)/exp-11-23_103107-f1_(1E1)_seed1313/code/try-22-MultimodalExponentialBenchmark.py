import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic sine wave components with varying frequencies and amplitudes
        chaotic_waves = 0
        for i in range(self.dim):
            freq = 2 * (i + 1) * np.pi
            amp = 1.5 + 0.5 * np.sin(i)
            chaotic_waves += amp * np.sin(freq * x[i] + np.sin(freq * x[i])) * \
                           np.cos(freq * x[i] + np.cos(freq * x[i]))
            
        # Radial basis functions with adaptive scaling and multiple peaks
        radial_basis = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i] if self.dim > 1 else 0
            sigma = 0.5 + 0.3 * np.sin(i)
            radial_basis += np.exp(-0.5 * ((x - center) / sigma)**2) * \
                          np.sin(3 * (x - center))**2
        
        # Cross-dimensional coupling with hyperbolic tangent interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for complexity
                cross_coupling += np.tanh(x[i] * x[j]) * \
                                np.sin(2 * (x[i]**2 + x[j]**2)) * \
                                np.cos(x[i] - x[j])
                
        # Spherical penalty with multiple concentric regions and varying penalties
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += (5 + 3 * np.sin(dist_from_origin)) * \
                      (1 - np.exp(-0.2 * (dist_from_origin - 3)**2)) * \
                      np.sin(3 * dist_from_origin)**2
        
        # Add a global scaling factor and combine all components
        return 1.2 * (chaotic_waves + radial_basis + cross_coupling + penalty)