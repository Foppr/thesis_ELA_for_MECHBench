import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with varying degrees and mixed terms
        poly_chaos = np.sum(0.5 * x**2 + 0.15 * x**3 + 0.03 * x**4 + 0.005 * x**5 + 0.02 * np.sin(x) * np.cos(x))
        
        # Radial basis function terms with Gaussian kernels and adaptive centers
        rbfs = 0.0
        centers = np.linspace(-5, 5, min(11, self.dim // 2 + 3))
        for i in range(len(centers)):
            for j in range(self.dim):
                sigma = 0.3 + 0.1 * np.sin(i * 0.5)
                rbfs += np.exp(-0.2 * ((x[j] - centers[i % len(centers)]) / (sigma + 0.1 * i))**2)
        
        # Fractal-like sine-wave modulation with varying frequencies and amplitude
        fractal_sine = np.sum(np.sin(3.5 * x) * np.cos(5.5 * x) * np.sin(7.0 * x) * np.cos(3.0 * x))
        
        # Enhanced interaction terms with weighted distance, dynamic scaling, and coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.02)
                weight = 1.0 / (dist**2.0 + 0.05)
                interaction += weight * np.sin(4.0 * (x[i] + x[j])) * np.cos(2.0 * (x[i] - x[j]))
        
        # Modified asymmetric penalty with quintic scaling and adaptive thresholds
        penalty = np.sum(np.where(np.abs(x) > 4.7, 0.3 * (np.abs(x) - 4.7)**5, 0.0))
        
        # Add a global scaling factor to control the function's range and complexity
        return 0.25 * poly_chaos + 0.25 * rbfs + 0.2 * fractal_sine + 0.25 * interaction + penalty