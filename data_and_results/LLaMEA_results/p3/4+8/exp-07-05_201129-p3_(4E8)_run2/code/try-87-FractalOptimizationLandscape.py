import numpy as np

class FractalOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.scale_factors = np.array([2**i for i in range(1, min(6, dim + 1))])
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Radial component with fractal scaling
        r = np.sqrt(np.sum(x_norm**2))
        
        # Multi-scale fractal pattern using polynomial chaos expansion
        fractal = 0.0
        for i in range(min(5, self.dim)):
            scale = self.scale_factors[i % len(self.scale_factors)] if len(self.scale_factors) > 0 else 1.0
            freq = scale * (i + 1) * 2
            amp = 1.0 / (scale * (i + 1))
            fractal += amp * np.sin(freq * r + i * np.pi / 6) * np.cos(freq * r * 0.5 + i * np.pi / 4)
        
        # Radial basis function component with varying widths
        rbf = 0.0
        centers = np.linspace(-1, 1, min(8, self.dim + 1))
        for i in range(len(centers)):
            center = centers[i % len(centers)]
            width = 0.1 + 0.2 * (i % 3)
            rbf += np.exp(-((x_norm - center)**2) / (2 * width**2))
        
        # Polynomial chaos expansion with mixed terms
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**3) * np.sin(x_norm[i] * 2) + 0.5 * (x_norm[i]**2) * np.cos(x_norm[i])
        
        # Multi-modal interaction terms with varying amplitudes
        modal = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                modal += 0.3 * np.sin(x_norm[i] * x_norm[j] * 5) * np.cos(x_norm[i] - x_norm[j])
        
        # Gradient conditioning with non-linear transformation
        grad_cond = 0.0
        for i in range(self.dim):
            grad_cond += (x_norm[i]**4) * (1.0 + 0.3 * np.sin(x_norm[i] * 10))
        
        # Final combination with global scaling
        return 2.0 * fractal + 0.5 * rbf + 0.3 * poly + 0.2 * modal + 0.1 * grad_cond + 1.5 * r * np.exp(-r**2 * 0.5)