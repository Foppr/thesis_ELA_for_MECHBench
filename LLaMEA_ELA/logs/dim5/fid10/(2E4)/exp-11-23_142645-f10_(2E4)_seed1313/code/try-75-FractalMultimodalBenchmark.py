import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with varying degrees and mixed terms
        poly_chaos = np.sum(0.6 * x**2 + 0.12 * x**3 + 0.02 * x**4 + 0.003 * x**5 + 0.015 * np.sin(x) * np.cos(x))
        
        # Radial basis function terms with Gaussian kernels and adaptive centers
        rbfs = 0.0
        centers = np.linspace(-5, 5, min(11, self.dim // 2 + 3))
        for i in range(len(centers)):
            for j in range(self.dim):
                sigma = 0.35 + 0.08 * np.sin(i * 0.6)
                rbfs += np.exp(-0.25 * ((x[j] - centers[i % len(centers)]) / (sigma + 0.12 * i))**2)
        
        # Fractal-like sine-wave modulation with varying frequencies and amplitude
        fractal_sine = np.sum(np.sin(4.0 * x) * np.cos(6.0 * x) * np.sin(7.5 * x) * np.cos(3.5 * x))
        
        # Enhanced interaction terms with weighted distance, dynamic scaling, and coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.03)
                weight = 1.5 / (dist**2.2 + 0.06)
                interaction += weight * np.sin(4.5 * (x[i] + x[j])) * np.cos(2.5 * (x[i] - x[j]))
        
        # Modified asymmetric penalty with quintic scaling and adaptive thresholds
        penalty = np.sum(np.where(np.abs(x) > 4.6, 0.35 * (np.abs(x) - 4.6)**5, 0.0))
        
        # Add a global scaling factor to control the function's range and complexity
        return 0.23 * poly_chaos + 0.27 * rbfs + 0.18 * fractal_sine + 0.28 * interaction + penalty