import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        poly_term = np.sum((x_norm**3) + 0.5 * (x_norm**4) + 0.1 * (x_norm**6))
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        rb_term = 0.0
        for i in range(len(centers)):
            if i < len(x_norm):
                rb_term += np.exp(-5.0 * (x_norm[i] - centers[i%len(centers)])**2)
        
        # Trigonometric component with varying frequencies and phase shifts
        trig_term = np.sum(np.sin(10.0 * x_norm) * np.cos(7.0 * x_norm) + 
                          0.5 * np.sin(15.0 * x_norm**2) * np.cos(12.0 * x_norm))
        
        # Scaled Ackley-like function for additional multimodality
        ackley_term = -20.0 * np.exp(-0.2 * np.sqrt(np.sum(x_norm**2) / self.dim)) - \
                      np.exp(np.sum(np.cos(2.0 * np.pi * x_norm)) / self.dim) + 20.0 + np.e
        
        # Modified Schwefel function component
        schwefel_term = 418.9829 * self.dim - np.sum(x_norm * np.sin(np.sqrt(np.abs(x_norm))))
        
        # Adaptive scaling based on dimensionality and input magnitude
        adaptive_scale = 1.0 + 0.5 * np.log(self.dim + 1) + 0.3 * np.std(np.abs(x_norm))
        
        # Combine all terms with carefully chosen weights
        result = adaptive_scale * (0.7 * poly_term + 0.4 * rb_term + 0.3 * trig_term + 
                                 0.2 * ackley_term + 0.1 * schwefel_term)
        
        return result