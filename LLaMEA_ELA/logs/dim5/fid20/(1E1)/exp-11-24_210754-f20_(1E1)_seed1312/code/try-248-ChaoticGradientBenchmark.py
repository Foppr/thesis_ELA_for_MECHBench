import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic gradient modulation with sine-based perturbations
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic scaling factor based on golden ratio and dimension
            scale = (1.0 + np.sin(i * 0.618)) * (1.0 + 0.3 * np.cos(i * 0.5))
            # Apply sine-modulated gradient with fractional power for nonlinearity
            f2 += scale * np.sin(20.0 * xi) * np.exp(-0.5 * xi**2)
        
        # Asymmetric multimodal structure with periodic peaks and valleys
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-scale periodic modulation with varying amplitudes
            f3 += (np.sin(15.0 * xi) + 0.5 * np.sin(40.0 * xi)) * np.exp(-0.1 * np.abs(xi))
        
        # Saddle point interference with exponential decay and asymmetric curvature
        f4 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric saddle term with varying decay rate
            f4 += (xi**3 - 0.5 * xi**2) * np.exp(-0.3 * np.abs(xi))
        
        # Cross-dimensional coupling with asymmetric interaction terms
        f5 = 0.0
        for i in range(self.dim - 1):
            xi, xj = x[i], x[i+1]
            # Asymmetric interaction with exponential weighting
            f5 += np.exp(-0.2 * (xi**2 + xj**2)) * np.sin(10.0 * xi) * np.cos(8.0 * xj)
        
        # Fractional Brownian motion-inspired roughness with multi-fractal scaling
        f6 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractional power with chaotic scaling factor
            f6 += (np.abs(xi)**1.7 + 0.3 * np.sin(25.0 * xi)) * np.exp(-0.15 * np.abs(xi))
        
        # Combine all components with dynamic weights based on dimensionality
        weight_sum = 1.0 + 0.5 * np.sin(self.dim * 0.3)
        return (f1 + f2 + f3 + f4 + f5 + f6) / weight_sum