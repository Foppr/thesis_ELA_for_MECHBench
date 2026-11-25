import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute angular frequencies for trigonometric components
        self.frequencies = np.arange(1, dim + 1) * np.pi / 4.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic term
        f1 = np.sum(x**2)
        
        # High-frequency trigonometric oscillations
        f2 = np.sum(np.sin(self.frequencies * x) * np.cos(self.frequencies * x))
        
        # Multi-modal radial component with Gaussian peaks
        f3 = 0.0
        for i in range(self.dim):
            peak_pos = 2.0 * np.sin(i)
            f3 += np.exp(-0.5 * ((x[i] - peak_pos) / 1.5)**2) * np.cos(3.0 * x[i])
        
        # Cross-dimensional coupling with sine interaction
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.sin(x[i] * x[i+1]) * (i + 1)
        f4 *= 0.3
        
        # Polynomial chaos with varying exponents
        f5 = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.sin(i)
            f5 += (x[i]**exp_factor) * np.cos(x[i])
        f5 *= 0.2
        
        # Radial basis function with dynamic centers
        f6 = 0.0
        for i in range(self.dim):
            center = 3.0 * np.cos(i)
            f6 += np.exp(-0.5 * ((x[i] - center) / 2.0)**2)
        f6 *= 0.15
        
        # Sine-cosine coupled oscillations
        f7 = np.sum(np.sin(x) * np.cos(2.0 * x) * np.sin(3.0 * x))
        
        # Asymmetric multimodal component
        f8 = 0.0
        for i in range(self.dim):
            asym_term = (x[i] + 1.0)**3 - (x[i] - 1.0)**3
            f8 += asym_term * np.sin(2.0 * x[i])
        f8 *= 0.1
        
        # Fractional polynomial with trigonometric modulation
        f9 = 0.0
        for i in range(self.dim):
            f9 += (x[i]**1.5) * np.cos(1.5 * x[i])
        f9 *= 0.25
        
        # Interaction between all dimensions via product of sines
        f10 = np.prod(np.sin(x)) * 0.2
        
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)