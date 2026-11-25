import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with varying degrees
        poly_chaos = np.sum((0.9 * x**2 + 0.25 * x**3 + 0.18 * x**4 + 0.015 * x**5))
        
        # Radial basis function terms with Gaussian kernels
        rbfs = 0.0
        centers = np.linspace(-3.5, 3.5, self.dim // 4 + 1)
        for i in range(len(centers)):
            for j in range(self.dim):
                rbfs += np.exp(-0.5 * ((x[j] - centers[i % len(centers)]) / (1.0 + 0.2 * i))**2)
        
        # Fractal-like sine-wave modulation with varying frequencies
        fractal_sine = np.sum(np.sin(3.5 * x) * np.sin(7.5 * x) * np.cos(5.5 * x))
        
        # Interaction terms with inverse distance weighting
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                if dist > 0:
                    interaction += 1.0 / (dist + 0.03) * np.sin(2.5 * (x[i] + x[j]))
        
        # Asymmetric penalty for large values
        penalty = np.sum(np.where(np.abs(x) > 2.0, (np.abs(x) - 2.0)**3.5, 0.0))
        
        # Add a global scaling factor to control the function's range
        return 0.55 * poly_chaos + 0.3 * rbfs + 0.12 * fractal_sine + 0.08 * interaction + penalty