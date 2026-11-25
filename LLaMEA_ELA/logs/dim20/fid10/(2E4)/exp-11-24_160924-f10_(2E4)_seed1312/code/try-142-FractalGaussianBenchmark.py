import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic scaling factors for each dimension
        self.fractal_factors = [0.1 + 0.9 * np.sin(0.7 * i + np.pi/4) * np.cos(0.3 * i) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic Gaussian peaks with fractal-based locations and widths
        for i in range(self.dim):
            xi = x[i]
            # Chaotic peak locations using sine-cosine combinations
            peak_loc = 4.0 * np.sin(0.6 * i + 1.0) * np.cos(0.4 * i + 0.5) * self.fractal_factors[i]
            peak_width = 0.5 + 0.7 * np.sin(0.8 * i + 0.3) * self.fractal_factors[i]
            result += np.exp(-0.5 * ((xi - peak_loc) / peak_width)**2)
            
        # Add multi-scale chaotic Gaussian components with varying amplitudes
        for i in range(self.dim):
            xi = x[i]
            amp = 2.0 + 1.5 * np.sin(0.9 * i + 0.7)
            width = 1.0 + 0.8 * np.cos(0.6 * i + 0.4)
            center = -4.0 + 8.0 * np.random.random() * self.fractal_factors[i]
            result += amp * np.exp(-0.5 * ((xi - center) / width)**2)
            
        # Add dynamic cross-correlation structure with chaotic coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr = 0.5 + 0.5 * np.sin(0.7 * (i + j) + 0.3) * self.fractal_factors[i] * self.fractal_factors[j]
                result += corr * x[i] * x[j]
                
        # Add chaotic ruggedness with dimension-dependent noise
        for i in range(self.dim):
            xi = x[i]
            # Varying noise intensity based on fractal factors with chaotic modulation
            noise_intensity = 0.3 + 0.5 * self.fractal_factors[i] * np.sin(12.0 * xi + 0.8)
            result += noise_intensity * np.sin(15.0 * xi) * np.cos(10.0 * xi)
            
        # Add chaotic multi-modal structure with nested peaks
        for i in range(self.dim):
            xi = x[i]
            # Nested peaks at different scales with chaotic amplitudes
            result += 0.8 * np.exp(-0.5 * ((xi - 1.2) / 0.4)**2)
            result += 0.6 * np.exp(-0.5 * ((xi + 1.8) / 0.6)**2)
            result += 0.4 * np.exp(-0.5 * ((xi - 2.8) / 0.9)**2)
            result += 0.2 * np.exp(-0.5 * ((xi + 3.2) / 1.1)**2)
            
        # Add dynamic coupling terms with chaotic interaction coefficients
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                coupling = 0.6 * self.fractal_factors[i] * self.fractal_factors[i+1] * np.sin(0.5 * (x[i] + x[i+1]) + 0.4)
                result += coupling * np.sin(x[i] + x[i+1]) * np.cos(0.7 * (x[i] - x[i+1]))
                
        # Add global scaling factor with chaotic variation
        global_scale = 1.5 + 0.8 * np.sin(0.3 * self.dim + 0.6)
        result *= global_scale
        
        return result