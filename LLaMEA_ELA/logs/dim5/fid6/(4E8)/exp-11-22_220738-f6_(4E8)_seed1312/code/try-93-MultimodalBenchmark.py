import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_param = 3.8
        self.seed = 0.2
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential with variable exponents
        f_val = 0.0 * np.sum(x**6) / self.dim + 0.5 * np.sum(x**4) / self.dim + 0.5 * np.sum(x**2) / self.dim
        
        # Complex trigonometric interference with phase shifts
        for i in range(self.dim):
            f_val += 1.5 * np.sin(4 * x[i]) * np.cos(3 * x[(i+1) % self.dim]) * np.sin(0.5 * x[(i+2) % self.dim])
            
        # Multi-scale Gaussian peaks with dynamic heights and widths
        num_peaks = min(9, self.dim)
        for i in range(num_peaks):
            center = -4.8 + 1.2 * i
            width = 0.1 + 0.6 * np.sin(i * 0.7)
            height = 1.0 + 0.8 * np.cos(i * 0.9)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Chaotic modulation using logistic map with varying parameters
        chaos_val = self.seed
        for i in range(self.dim):
            chaos_val = self.chaos_param * chaos_val * (1 - chaos_val)
            f_val += 0.7 * chaos_val * np.cos(1.3 * x[i % self.dim])
            
        # Adaptive scaling with curvature-dependent factor
        grad_magnitude = np.mean(np.abs(np.gradient(x)))
        curvature_factor = 1.0 + 0.8 * np.std(np.gradient(x))
        scale_factor = curvature_factor * (1.0 + 0.3 * grad_magnitude)
        f_val *= scale_factor
        
        # Cross-dimensional interaction through higher-order product terms
        if self.dim >= 4:
            for i in range(0, self.dim - 3):
                f_val += 0.5 * x[i] * x[i+1] * x[i+2] * x[i+3]
                
        # Add noise component to increase ruggedness
        noise = 0.1 * np.random.rand()
        f_val += noise
        
        return f_val