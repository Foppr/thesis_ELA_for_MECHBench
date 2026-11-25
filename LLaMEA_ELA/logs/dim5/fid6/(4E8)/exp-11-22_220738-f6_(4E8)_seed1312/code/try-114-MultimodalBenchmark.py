import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_param = 3.9
        self.seed = 0.15
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential with variable exponents and adaptive weights
        f_val = 0.0 * np.sum(x**8) / self.dim + 0.6 * np.sum(x**5) / self.dim + 0.4 * np.sum(x**3) / self.dim
        
        # Complex trigonometric interference with phase shifts and frequency modulation
        for i in range(self.dim):
            f_val += 2.0 * np.sin(5 * x[i]) * np.cos(4 * x[(i+1) % self.dim]) * np.sin(0.7 * x[(i+2) % self.dim])
            
        # Multi-scale Gaussian peaks with dynamic heights, widths, and positions
        num_peaks = min(12, self.dim)
        for i in range(num_peaks):
            center = -4.5 + 1.0 * i
            width = 0.05 + 0.7 * np.sin(i * 0.6)
            height = 1.5 + 1.0 * np.cos(i * 0.8)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Chaotic modulation using logistic map with varying parameters and time-varying coupling
        chaos_val = self.seed
        for i in range(self.dim):
            chaos_val = self.chaos_param * chaos_val * (1 - chaos_val)
            f_val += 0.8 * chaos_val * np.cos(1.5 * x[i % self.dim]) * np.sin(0.3 * i)
            
        # Adaptive scaling with curvature-dependent factor and gradient magnitude
        grad_magnitude = np.mean(np.abs(np.gradient(x)))
        curvature_factor = 1.0 + 1.0 * np.std(np.gradient(x))
        scale_factor = curvature_factor * (1.0 + 0.4 * grad_magnitude)
        f_val *= scale_factor
        
        # Cross-dimensional interaction through higher-order product terms with dynamic coefficients
        if self.dim >= 5:
            for i in range(0, self.dim - 4):
                coeff = 0.6 + 0.2 * np.sin(i * 0.5)
                f_val += coeff * x[i] * x[i+1] * x[i+2] * x[i+3] * x[i+4]
                
        # Add asymmetric exponential saddle points to increase ruggedness
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-0.5 * (x[i] - 2)**2) - 0.3 * np.exp(-0.5 * (x[i] + 2)**2)
            
        # Add noise component to increase ruggedness with dynamic amplitude
        noise = 0.15 * np.random.rand()
        f_val += noise
        
        return f_val