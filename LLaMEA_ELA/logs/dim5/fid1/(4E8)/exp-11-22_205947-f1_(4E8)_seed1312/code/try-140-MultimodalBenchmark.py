import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic potential wells with varying depths and widths
        well_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple periodic components with different frequencies and amplitudes
            well_term += (1 + 0.3 * np.sin(7 * np.pi * xi)) * \
                        np.exp(-0.5 * (xi - np.sin(3 * np.pi * xi))**2 / 0.1) + \
                        0.5 * np.cos(11 * np.pi * xi) * np.exp(-0.5 * xi**2 / 0.05)
        
        # Adaptive conditioning with dimension-dependent scaling
        cond_term = 0.0
        for i in range(self.dim):
            # Dynamic scaling factor based on position and dimension
            scale_factor = 1 + 0.4 * np.sin(5 * np.pi * x_norm[i]) * (i + 1) / self.dim
            cond_term += scale_factor * (x_norm[i]**3 + 0.5 * x_norm[i]**2)
        
        # Cross-dimensional coupling with varying interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction strength varies with dimension indices and positions
                strength = (1 + 0.3 * np.sin(2 * np.pi * (i + j))) * \
                          np.cos(4 * np.pi * (x_norm[i] - x_norm[j]))
                coupling_term += strength * (x_norm[i]**2 + x_norm[j]**2)
        
        # Multi-scale harmonic components with dynamic modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple harmonic terms with different frequencies and amplitudes
            harmonic_term += (1 + 0.2 * np.cos(9 * np.pi * xi)) * \
                           np.sin(6 * np.pi * xi) * \
                           np.exp(-0.5 * xi**2)
        
        # Nonlinear transformation with piecewise polynomial behavior
        poly_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Piecewise polynomial with smooth transitions
            if xi < -0.5:
                poly_term += 0.8 * xi**3 + 0.2 * xi**2
            elif xi > 0.5:
                poly_term += 0.6 * xi**3 - 0.3 * xi**2
            else:
                poly_term += 0.4 * xi**3 + 0.1 * xi**2
        
        # Combined result with global scaling factors
        result = 1.2 * well_term + 0.9 * cond_term + 0.7 * coupling_term + \
                 0.8 * harmonic_term + 0.6 * poly_term
        
        # Add noise-like modulation to increase algorithmic pressure
        noise = 0.05 * np.sin(13 * np.pi * np.sum(x_norm**3)) * np.cos(17 * np.pi * np.prod(x_norm))
        result += noise
        
        return result