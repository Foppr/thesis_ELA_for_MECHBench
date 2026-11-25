import numpy as np

class QuaternionRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with varying widths and centers
        rbf = 0
        centers = np.linspace(-1, 1, min(5, self.dim))
        widths = np.logspace(-1, 1, min(5, self.dim))
        heights = np.logspace(0, 2, min(5, self.dim))
        
        for i in range(min(5, self.dim)):
            center = centers[i] if i < len(centers) else 0
            width = widths[i] if i < len(widths) else 1.0
            height = heights[i] if i < len(heights) else 1.0
            
            # Radial distance with quaternion-inspired rotation
            dist = np.sum((x_norm - center)**2)
            rbf += height * np.exp(-dist / (2 * width**2))
        
        # Quaternion-inspired rotational symmetry component
        rot_sym = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                # Create rotation-like interaction between pairs of dimensions
                xi = x_norm[i]
                yi = x_norm[i+1]
                rot_sym += (xi**2 + yi**2) * np.cos(3.14159 * (xi - yi)) * np.sin(2.718 * (xi + yi))
        
        # Directional bias with harmonic modulation
        dir_bias = 0
        for i in range(self.dim):
            # Create directional preference with sinusoidal modulation
            dir_bias += (x_norm[i]**3) * np.cos(2.5 * x_norm[i]) * np.sin(1.8 * x_norm[i])
        
        # Multi-scale harmonic oscillation with exponential decay
        harmonics = 0
        scales = [0.5, 1.5, 3.0]
        for scale in scales:
            harmonics += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm) * 
                              np.exp(-0.2 * x_norm**2))
        
        # Cross-term coupling with asymmetric interaction
        coupling = 0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**2.5 + x_norm[i+1]**2.5) * \
                       np.sin(2.1 * (x_norm[i] - x_norm[i+1])) * \
                       np.exp(-0.3 * (x_norm[i] + x_norm[i+1])**2)
        
        # Combine all components
        result = rbf + rot_sym + dir_bias + harmonics + coupling
        
        # Add small random noise for robustness
        noise = 0.01 * np.random.rand()
        
        return result + noise