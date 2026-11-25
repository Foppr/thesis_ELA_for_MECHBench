import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with higher-order terms and dynamic weights
        poly_chaos = np.sum(0.3 * x**2 + 0.15 * x**3 + 0.04 * x**4 + 0.008 * x**5 + 0.002 * x**6)
        
        # Radial basis function terms with multi-scale Gaussian kernels and dynamic centers
        rbfs = 0.0
        centers = np.linspace(-5, 5, min(7, self.dim // 3 + 3))
        for i in range(len(centers)):
            for j in range(self.dim):
                scale_factor = 0.6 + 0.4 * np.sin(i * 0.8)
                rbfs += scale_factor * np.exp(-0.2 * ((x[j] - centers[i % len(centers)]) / (0.15 + 0.08 * i))**2)
        
        # Fractal-like sine-wave modulation with multi-frequency interactions and phase shifts
        fractal_sine = np.sum(np.sin(3.0 * x) * np.sin(5.0 * x) * np.cos(3.0 * x) * np.cos(1.5 * x))
        
        # Enhanced interaction terms with non-linear coupling and adaptive weights
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.03)
                weight = 1.0 / (dist**2.5 + 0.06)
                interaction += weight * np.sin(4.0 * (x[i] + x[j]) + 0.4 * np.sin(x[i] - x[j]))
        
        # Modified asymmetric penalty with quintic scaling and boundary influence
        penalty = np.sum(np.where(np.abs(x) > 4.6, 0.3 * (np.abs(x) - 4.6)**5, 0.0))
        
        # Add dynamic global scaling factor based on dimensionality
        scaling_factor = 1.0 + 0.15 * np.log(self.dim + 1)
        
        # Combine all components with adjusted weights for increased complexity and better fitness
        return scaling_factor * (0.25 * poly_chaos + 0.2 * rbfs + 0.2 * fractal_sine + 0.25 * interaction + penalty)