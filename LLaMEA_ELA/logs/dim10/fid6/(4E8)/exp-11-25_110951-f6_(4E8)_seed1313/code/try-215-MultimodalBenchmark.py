import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logistic map chaotic dynamics with parameter modulation
        chaotic_term = 0.0
        r = 3.95
        for i in range(self.dim):
            xi = x_norm[i]
            # Simulate logistic map behavior in one dimension
            for _ in range(5):
                xi = r * xi * (1 - xi)
            chaotic_term += xi**2
            
        # Radial basis function with multi-scale Gaussian components
        rbfn_term = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            for c in centers:
                rbfn_term += np.exp(-5 * (x_norm[i] - c)**2) * np.sin(3 * np.pi * x_norm[i])
                
        # Quaternion-based rotation structure for cross-dimensional coupling
        quat_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            quat_term += (x_norm[i]**2 + x_norm[j]**2 - x_norm[k]**2) * \
                        np.cos(2 * np.pi * x_norm[i]) * np.sin(2 * np.pi * x_norm[j])
        
        # Fractal-like curvature with recursive sine modulation
        fractal_term = 0.0
        for i in range(self.dim):
            val = x_norm[i]
            for _ in range(3):
                val = np.sin(10 * val)
            fractal_term += val**2
            
        # Multi-scale harmonic interference with complex amplitude envelope
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(7 * x_norm[i]) * np.cos(4 * x_norm[i]) * \
                           np.exp(-0.1 * x_norm[i]**2) + \
                           0.5 * np.sin(13 * x_norm[i]) * np.cos(9 * x_norm[i]) * \
                           np.exp(-0.2 * x_norm[i]**2)
        
        # Cross-dimensional polynomial interaction with asymmetric weights
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x_norm[i]**3 + 0.5 * x_norm[j]**3) * \
                           np.sin(2 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[j])
        
        # Ergodic basin structure with logarithmic energy scaling
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += np.log(1 + np.abs(x_norm[i])) * np.tan(x_norm[i])
        
        # Final combined function with dynamic weighting
        return 0.25 * chaotic_term + 0.2 * rbfn_term + 0.15 * quat_term + \
               0.15 * fractal_term + 0.1 * harmonic_term + 0.1 * poly_term + \
               0.05 * basin_term