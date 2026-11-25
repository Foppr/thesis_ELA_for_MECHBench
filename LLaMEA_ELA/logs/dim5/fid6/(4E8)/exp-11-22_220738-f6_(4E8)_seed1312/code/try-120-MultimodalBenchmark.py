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
        
        # Multi-scale fractal trigonometric interference with dynamic phase shifts and frequency modulation
        for i in range(self.dim):
            f_val += 2.5 * np.sin(7 * x[i]) * np.cos(6 * x[(i+1) % self.dim]) * np.sin(0.9 * x[(i+2) % self.dim])
            
        # Multi-scale Gaussian peaks with dynamic heights, widths, and positions
        num_peaks = min(15, self.dim)
        for i in range(num_peaks):
            center = -4.8 + 0.8 * i
            width = 0.02 + 0.6 * np.sin(i * 0.7)
            height = 2.0 + 0.8 * np.cos(i * 0.9)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Enhanced chaotic modulation using logistic map with time-varying parameters and multi-scale coupling
        chaos_val = self.seed
        for i in range(self.dim):
            chaos_val = self.chaos_param * chaos_val * (1 - chaos_val)
            f_val += 1.0 * chaos_val * np.cos(2.0 * x[i % self.dim]) * np.sin(0.4 * i)
            
        # Neural-like adaptive scaling with curvature-dependent factor and gradient magnitude
        grad_magnitude = np.mean(np.abs(np.gradient(x)))
        curvature_factor = 1.0 + 1.5 * np.std(np.gradient(x))
        scale_factor = curvature_factor * (1.0 + 0.6 * grad_magnitude)
        f_val *= scale_factor
        
        # Cross-dimensional interaction through higher-order product terms with dynamic coefficients and fractal coupling
        if self.dim >= 6:
            for i in range(0, self.dim - 5):
                coeff = 0.7 + 0.3 * np.sin(i * 0.6)
                f_val += coeff * x[i] * x[i+1] * x[i+2] * x[i+3] * x[i+4] * x[i+5]
                
        # Asymmetric exponential saddle points with fractal scaling and multi-scale modulation
        for i in range(self.dim):
            f_val += 0.7 * np.exp(-0.5 * (x[i] - 2.5)**2) - 0.4 * np.exp(-0.5 * (x[i] + 2.5)**2)
            
        # Add fractal noise component with dynamic amplitude and multi-scale frequency
        noise = 0.2 * np.random.rand() * np.sin(10 * np.sum(x))
        f_val += noise
        
        return f_val