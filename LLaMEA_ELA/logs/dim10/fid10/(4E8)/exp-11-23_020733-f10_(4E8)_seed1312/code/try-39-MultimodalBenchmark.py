import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos-like term with mixed degrees creating complex valleys
        f1 = np.sum(0.5 * x_norm**8 + 0.3 * x_norm**6 + 0.2 * x_norm**4 + 0.1 * x_norm**2)
        
        # Trigonometric interference pattern with multiple frequencies and amplitudes
        f2 = np.sum(np.sin(10 * x_norm) * np.cos(15 * x_norm) * 
                   np.sin(7 * x_norm) * np.cos(12 * x_norm))
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        rb_f = 0.0
        for i in range(len(centers)):
            if i < len(x_norm):
                rb_f += np.exp(-10 * (x_norm[i] - centers[i%len(centers)])**2)
        f3 = rb_f
        
        # Cross-term interaction creating saddle points and ridges
        f4 = 0.05 * np.sum((x_norm[:-1] + x_norm[1:])**2 * (x_norm[:-1] - x_norm[1:])**2)
        
        # Combined function with competing forces
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4