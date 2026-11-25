import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with varying degrees
        poly_chaos = np.sum(0.5 * x**2 + 0.3 * x**3 + 0.1 * x**4 + 0.02 * x**5 + 0.005 * x**6)
        
        # Radial basis function terms with Gaussian kernels and adaptive widths
        rbfs = 0.0
        centers = np.linspace(-5, 5, min(11, self.dim // 2 + 3))
        for i in range(len(centers)):
            for j in range(self.dim):
                width = 0.3 + 0.1 * np.sin(i * 0.5) + 0.05 * np.cos(j * 0.3)
                rbfs += np.exp(-0.2 * ((x[j] - centers[i % len(centers)]) / width)**2)
        
        # Fractal-like sine-wave modulation with varying frequencies and amplitudes
        fractal_sine = np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.sin(3.0 * x) * np.cos(5.0 * x))
        
        # Enhanced interaction terms with weighted distance, dynamic scaling, and cross-terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                weight = 1.0 / (dist**2.0 + 0.05)
                interaction += weight * (np.sin(6.0 * (x[i] + x[j])) + 0.5 * np.cos(4.0 * (x[i] - x[j])))
        
        # Modified asymmetric penalty with quintic scaling and variable thresholds
        penalty = np.sum(np.where(np.abs(x) > 4.7, 0.3 * (np.abs(x) - 4.7)**5, 0.0))
        
        # Add a global scaling factor to control the function's range
        return 0.25 * poly_chaos + 0.35 * rbfs + 0.2 * fractal_sine + 0.2 * interaction + penalty