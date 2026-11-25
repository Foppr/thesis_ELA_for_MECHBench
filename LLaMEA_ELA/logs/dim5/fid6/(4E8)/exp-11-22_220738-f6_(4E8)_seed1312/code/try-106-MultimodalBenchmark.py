import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_param = 3.9
        self.seed = 0.15
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential with variable exponents and adaptive scaling
        f_val = 0.3 * np.sum(x**6) / self.dim + 0.4 * np.sum(x**4) / self.dim + 0.3 * np.sum(x**2) / self.dim
        
        # Complex trigonometric interference with phase shifts and dynamic frequencies
        for i in range(self.dim):
            freq1 = 3.0 + 0.5 * np.sin(i * 0.8)
            freq2 = 2.5 + 0.3 * np.cos(i * 0.6)
            f_val += 1.2 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[(i+1) % self.dim]) * np.sin(0.7 * x[(i+2) % self.dim])
            
        # Multi-scale Gaussian peaks with dynamic heights, widths, and positions
        num_peaks = min(8, self.dim)
        for i in range(num_peaks):
            center = -4.5 + 1.0 * i
            width = 0.15 + 0.5 * np.sin(i * 0.9)
            height = 1.2 + 0.6 * np.cos(i * 1.1)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Chaotic modulation using logistic map with varying parameters and enhanced coupling
        chaos_val = self.seed
        for i in range(self.dim):
            chaos_val = self.chaos_param * chaos_val * (1 - chaos_val)
            f_val += 0.8 * chaos_val * np.cos(1.5 * x[i % self.dim])
            
        # Adaptive scaling with curvature-dependent factor and gradient magnitude effects
        grad_magnitude = np.mean(np.abs(np.gradient(x)))
        curvature_factor = 1.0 + 0.9 * np.std(np.gradient(x))
        scale_factor = curvature_factor * (1.0 + 0.4 * grad_magnitude)
        f_val *= scale_factor
        
        # Cross-dimensional interaction through higher-order product terms with variable coefficients
        if self.dim >= 4:
            for i in range(0, self.dim - 3):
                coeff = 0.6 + 0.2 * np.sin(i * 0.5)
                f_val += coeff * x[i] * x[i+1] * x[i+2] * x[i+3]
                
        # Add enhanced noise component with dynamic amplitude to increase ruggedness
        noise_amplitude = 0.15 + 0.05 * np.sin(np.sum(x))
        noise = noise_amplitude * np.random.rand()
        f_val += noise
        
        return f_val