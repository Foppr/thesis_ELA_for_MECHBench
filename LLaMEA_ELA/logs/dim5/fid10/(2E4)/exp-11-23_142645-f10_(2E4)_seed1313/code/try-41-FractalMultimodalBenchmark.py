import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with higher-order terms
        poly_chaos = np.sum(0.7 * x**2 + 0.2 * x**3 + 0.1 * x**4 + 0.05 * x**5 + 0.01 * x**6)
        
        # Modified radial basis function terms with Gaussian kernels and varying widths
        rbfs = 0.0
        centers = np.linspace(-4.5, 4.5, min(5, self.dim // 2 + 1))
        for i in range(len(centers)):
            for j in range(self.dim):
                width = 1.0 + 0.2 * np.sin(i * 0.5)
                rbfs += np.exp(-0.5 * ((x[j] - centers[i % len(centers)]) / width)**2)
        
        # Fractal-like sine-wave modulation with varying frequencies and amplitudes
        fractal_sine = np.sum(np.sin(3.0 * x) * np.cos(7.0 * x) * np.sin(5.0 * x) + 
                             0.5 * np.cos(9.0 * x) * np.sin(4.0 * x))
        
        # Novel interaction terms with cosine-based distance weighting
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                interaction += np.cos(2.0 * dist) * np.sin(3.0 * (x[i] + x[j]))
        
        # Enhanced asymmetric penalty for large values with non-linear scaling
        penalty = np.sum(np.where(np.abs(x) > 3.0, (np.abs(x) - 3.0)**3.5, 0.0))
        
        # Add a global scaling factor to control the function's range
        return 0.5 * poly_chaos + 0.3 * rbfs + 0.1 * fractal_sine + 0.05 * interaction + penalty