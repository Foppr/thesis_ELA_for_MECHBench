import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive polynomial conditioning with dynamic exponents and scaling
        poly_cond = np.sum((x**2 + 0.3 * x**4 + 0.05 * x**6) * (1.0 + 0.2 * np.sin(self.dim * x)))
        
        # Dynamic sine-cosine wave interactions with frequency modulation and phase shifts
        wave_interaction = np.sum(np.sin(3.0 * x + 0.5 * np.cos(2.0 * x)) * 
                                np.cos(2.0 * x + 0.7 * np.sin(1.5 * x)) * 
                                np.exp(-0.1 * np.abs(x)))
        
        # Multi-scale Gaussian peaks with varying heights, widths, and positions
        gaussian_sum = 0.0
        for i in range(min(6, self.dim)):
            height = 1.5 + 0.5 * np.sin(i * 0.8)
            width = 0.8 + 0.4 * np.cos(i * 0.6)
            center = -4.0 + 8.0 * (i / max(1, self.dim - 1))
            gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Chaotic exponential coupling with time-varying parameters and cross-terms
        exp_coupling = np.sum(np.exp(-0.3 * (x[:-1]**2 + x[1:]**2)) * 
                             np.sin(4.0 * (x[:-1] - x[1:])) * 
                             np.cos(2.5 * (x[:-1] + x[1:])))
        
        # Adaptive noise modulation with dynamic intensity and frequency
        noise = 0.1 * np.random.rand() * np.sum(np.sin(7.0 * x) * np.cos(3.0 * x))
        
        # Gradient-based curvature adjustment with non-uniform scaling
        grad_curvature = 0.5 * np.sum(np.gradient(x)**2 * (1.0 + 0.3 * np.abs(x)))
        
        # Combined function value with enhanced fitness landscape
        return poly_cond + wave_interaction + gaussian_sum + exp_coupling + noise + grad_curvature