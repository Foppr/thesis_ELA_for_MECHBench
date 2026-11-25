import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with higher-order terms
        poly_chaos = np.sum(1.1 * x**2 + 0.3 * x**3 + 0.2 * x**4 + 0.02 * x**5 + 0.005 * x**6)
        
        # Modified radial basis function terms with Gaussian kernels and dynamic centers
        rbfs = 0.0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim // 3 + 1))
        for i in range(len(centers)):
            for j in range(self.dim):
                sigma = 0.8 + 0.2 * np.sin(i * 0.7)
                rbfs += np.exp(-0.5 * ((x[j] - centers[i % len(centers)]) / sigma)**2)
        
        # Fractal-like sine-wave modulation with more complex frequency interactions
        fractal_sine = np.sum(np.sin(4.0 * x) * np.cos(6.0 * x) * np.sin(8.0 * x))
        
        # Enhanced interaction terms with exponential weighting
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                if dist > 0:
                    weight = np.exp(-dist / 2.0)
                    interaction += weight * np.sin(3.0 * (x[i] + x[j]))
        
        # Modified penalty function with asymmetric scaling
        penalty = np.sum(np.where(np.abs(x) > 2.5, (np.abs(x) - 2.5)**4.0, 0.0))
        
        # Global scaling and mixing of components
        return 0.6 * poly_chaos + 0.25 * rbfs + 0.1 * fractal_sine + 0.05 * interaction + penalty