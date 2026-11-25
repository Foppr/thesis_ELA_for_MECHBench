import numpy as np

class RadialMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base term with varying exponents
        poly_term = np.sum((x_norm**3) + 0.5 * (x_norm**4) + 0.2 * (x_norm**6))
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        rbfs = []
        for c in centers:
            rbf = np.exp(-5 * np.sum((x_norm - c)**2))
            rbfs.append(rbf)
        rbf_term = np.sum(rbfs)
        
        # Trigonometric interaction term with varying frequencies
        trig_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Adaptive scaling based on dimensionality and input magnitude
        adaptive_scale = 1.0 + 0.5 * np.log(self.dim + 1) + 0.3 * np.mean(np.abs(x_norm))
        
        # Cross-term interaction creating complex landscape
        cross_term = np.sum((x_norm[:-1] * x_norm[1:]) * np.sin(3 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Fractal-like self-similar pattern using recursive sine
        fractal = np.sum(np.sin(2**np.arange(self.dim) * np.pi * x_norm))
        
        # Final combined function with weighted components
        return adaptive_scale * (0.6 * poly_term + 0.3 * rbf_term + 0.2 * trig_term - 0.1 * cross_term + 0.05 * fractal) + 0.01 * np.sum(x_norm**8)