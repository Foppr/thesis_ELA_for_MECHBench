import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with varying degrees
        poly_chaos = np.sum(0.3 * x**2 + 0.25 * x**3 + 0.06 * x**4 + 0.015 * x**5)
        
        # Radial basis function terms with Gaussian kernels
        rbfs = 0.0
        centers = np.linspace(-5, 5, min(9, self.dim // 2 + 2))
        for i in range(len(centers)):
            for j in range(self.dim):
                rbfs += np.exp(-0.2 * ((x[j] - centers[i % len(centers)]) / (0.3 + 0.15 * i))**2)
        
        # Fractal-like sine-wave modulation with varying frequencies
        fractal_sine = np.sum(np.sin(4.5 * x) * np.sin(6.5 * x) * np.cos(3.5 * x))
        
        # Enhanced interaction terms with weighted distance and dynamic scaling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                weight = 1.0 / (dist**1.3 + 0.02)
                interaction += weight * np.sin(4.5 * (x[i] + x[j]))
        
        # Modified asymmetric penalty with quartic scaling
        penalty = np.sum(np.where(np.abs(x) > 4.5, 0.3 * (np.abs(x) - 4.5)**4, 0.0))
        
        # Add a global scaling factor to control the function's range
        return 0.25 * poly_chaos + 0.35 * rbfs + 0.18 * fractal_sine + 0.22 * interaction + penalty