import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with higher-order terms and dynamic weights
        poly_chaos = np.sum(0.4 * x**2 + 0.2 * x**3 + 0.05 * x**4 + 0.01 * x**5 + 0.003 * x**6)
        
        # Radial basis function terms with multi-scale Gaussian kernels and dynamic centers
        rbfs = 0.0
        centers = np.linspace(-5, 5, min(9, self.dim // 2 + 2))
        for i in range(len(centers)):
            for j in range(self.dim):
                scale_factor = 0.5 + 0.5 * np.sin(i * 0.7)
                rbfs += scale_factor * np.exp(-0.15 * ((x[j] - centers[i % len(centers)]) / (0.2 + 0.1 * i))**2)
        
        # Fractal-like sine-wave modulation with multi-frequency interactions and phase shifts
        fractal_sine = np.sum(np.sin(4.0 * x) * np.sin(6.0 * x) * np.cos(4.0 * x) * np.cos(2.0 * x))
        
        # Enhanced interaction terms with non-linear coupling and adaptive weights
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.02)
                weight = 1.0 / (dist**3.0 + 0.08)
                interaction += weight * np.sin(5.0 * (x[i] + x[j]) + 0.5 * np.sin(x[i] - x[j]))
        
        # Modified asymmetric penalty with quartic scaling and boundary influence
        penalty = np.sum(np.where(np.abs(x) > 4.7, 0.4 * (np.abs(x) - 4.7)**4, 0.0))
        
        # Add dynamic global scaling factor based on dimensionality
        scaling_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combine all components with adjusted weights for increased complexity
        return scaling_factor * (0.3 * poly_chaos + 0.2 * rbfs + 0.25 * fractal_sine + 0.2 * interaction + penalty)