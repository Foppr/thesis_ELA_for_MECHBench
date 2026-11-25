import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like polynomial conditioning with recursive scaling and self-similarity
        poly_cond = np.sum((x**2 + 0.4 * x**4 + 0.1 * x**6 + 0.03 * x**8) * 
                          (1.0 + 0.3 * np.sin(self.dim * x) * np.cos(0.5 * self.dim * x)))
        
        # Chaotic sine-cosine wave interactions with fractional frequencies and phase locking
        wave_interaction = np.sum(np.sin(4.0 * x + 0.6 * np.cos(3.0 * x)) * 
                                np.cos(3.0 * x + 0.8 * np.sin(2.5 * x)) * 
                                np.exp(-0.15 * np.abs(x)) * 
                                (1.0 + 0.2 * np.sin(0.3 * x**2)))
        
        # Multi-scale Gaussian peaks with fractal dimension and dynamic positioning
        gaussian_sum = 0.0
        for i in range(min(8, self.dim)):
            height = 2.0 + 0.5 * np.sin(i * 1.2)
            width = 0.6 + 0.3 * np.cos(i * 0.8)
            center = -4.5 + 9.0 * (i / max(1, self.dim - 1))
            gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                           (1.0 + 0.1 * np.sin(i * 2.0 * x[i]))
        
        # Chaotic exponential coupling with fractional dimensions and cross-term interactions
        exp_coupling = np.sum(np.exp(-0.4 * (x[:-1]**2 + x[1:]**2)) * 
                             np.sin(5.0 * (x[:-1] - x[1:])) * 
                             np.cos(3.0 * (x[:-1] + x[1:])) * 
                             (1.0 + 0.2 * np.sin(0.5 * self.dim * (x[:-1] + x[1:]))))
        
        # Adaptive noise modulation with fractal characteristics and dynamic frequency
        noise = 0.15 * np.random.rand() * np.sum(np.sin(8.0 * x) * np.cos(4.0 * x) * 
                                               np.exp(-0.2 * np.abs(x)))
        
        # Gradient-based curvature with fractional Laplacian and non-uniform scaling
        grad_curvature = 0.6 * np.sum(np.gradient(x)**2 * (1.0 + 0.4 * np.abs(x)) * 
                                    np.log(1.0 + 0.1 * np.abs(x)))
        
        # Fractal dimension adjustment with recursive scaling factors
        fractal_adj = 0.05 * np.sum(np.sin(10.0 * x) * np.cos(5.0 * x) * 
                                  np.exp(-0.25 * np.abs(x)) * 
                                  (1.0 + 0.3 * np.sin(0.2 * self.dim * x)))
        
        # Combined function value with enhanced fitness landscape complexity
        return poly_cond + wave_interaction + gaussian_sum + exp_coupling + noise + grad_curvature + fractal_adj