import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Ring-like structure with periodic components and polynomial curvature
        ring_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Periodic modulation with varying frequencies and amplitudes
            periodic = np.sin(7 * np.pi * xi) + 0.5 * np.cos(13 * np.pi * xi)
            # Polynomial curvature with adaptive scaling
            poly_curvature = xi**4 + 0.8 * xi**2 + 0.3 * xi
            ring_term += periodic * poly_curvature
            
        # Add radial symmetry with multi-scale harmonic components
        radial = 0.0
        for i in range(self.dim):
            radial += x_norm[i]**2
        radial = np.sqrt(radial)
        
        # Multi-harmonic radial component with varying amplitudes
        harmonic_radial = 0.0
        for k in range(1, 6):
            amplitude = 1.0 / (k + 1)
            frequency = k * 5
            harmonic_radial += amplitude * np.sin(frequency * np.pi * radial)
            
        # Cross-dimensional interaction with ring-based coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Ring-based interaction with phase coupling
                phase = np.arctan2(x_norm[j], x_norm[i])
                interaction = (x_norm[i]**2 + x_norm[j]**2) * np.cos(3 * phase)
                cross_term += interaction
                
        # Adaptive conditioning with dimension-dependent scaling
        adaptive = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(11 * np.pi * x_norm[i])
            adaptive += scale_factor * (x_norm[i]**3 + 0.7 * x_norm[i])
            
        # Combine all terms with appropriate weights
        result = 1.2 * ring_term + 0.8 * harmonic_radial + 0.6 * cross_term + 0.4 * adaptive
        
        # Add noise-like modulation to increase algorithmic pressure
        noise = 0.05 * np.sin(31 * np.pi * np.sum(x_norm**3)) * np.cos(23 * np.pi * radial)
        result += noise
        
        return result