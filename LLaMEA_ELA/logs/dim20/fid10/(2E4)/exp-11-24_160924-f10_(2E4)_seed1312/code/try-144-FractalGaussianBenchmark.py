import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors for each dimension
        self.fractal_factors = [0.5 + 0.5 * np.sin(0.3 * i) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add fractal-like self-similar Gaussian peaks with adaptive scales
        for i in range(self.dim):
            xi = x[i]
            # Dynamic peak locations and widths based on fractal factors
            peak_loc = 3.0 * np.sin(0.5 * i) * self.fractal_factors[i]
            peak_width = 0.8 + 0.4 * np.cos(0.4 * i) * self.fractal_factors[i]
            result += np.exp(-0.5 * ((xi - peak_loc) / peak_width)**2)
            
        # Add multi-scale Gaussian components with varying amplitudes
        for i in range(self.dim):
            xi = x[i]
            amp = 1.5 + 0.8 * np.sin(0.7 * i)
            width = 1.2 + 0.6 * np.cos(0.6 * i)
            center = -2.0 + 4.0 * np.random.random() * self.fractal_factors[i]
            result += amp * np.exp(-0.5 * ((xi - center) / width)**2)
            
        # Add adaptive correlation structure between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr = 0.3 + 0.4 * np.sin(0.5 * (i + j)) * self.fractal_factors[i] * self.fractal_factors[j]
                result += corr * x[i] * x[j]
                
        # Add dynamic ruggedness with dimension-dependent noise
        for i in range(self.dim):
            xi = x[i]
            # Varying noise intensity based on fractal factors
            noise_intensity = 0.2 + 0.3 * self.fractal_factors[i]
            result += noise_intensity * np.sin(10.0 * xi) * np.cos(8.0 * xi)
            
        # Add hierarchical multi-modal structure with self-similarity
        for i in range(self.dim):
            xi = x[i]
            # Nested peaks at different scales
            result += 0.5 * np.exp(-0.5 * ((xi - 1.0) / 0.5)**2)
            result += 0.3 * np.exp(-0.5 * ((xi + 1.5) / 0.7)**2)
            result += 0.2 * np.exp(-0.5 * ((xi - 2.5) / 1.0)**2)
            
        # Add dynamic coupling terms that adapt based on fractal properties
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                coupling = 0.4 * self.fractal_factors[i] * self.fractal_factors[i+1]
                result += coupling * np.sin(x[i] + x[i+1]) * np.cos(0.5 * (x[i] - x[i+1]))
                
        # Add global scaling factor that changes with dimension
        global_scale = 1.0 + 0.5 * np.sin(0.2 * self.dim)
        result *= global_scale
        
        # Add a new component to improve fitness score: chaotic multi-modal structure
        chaos_factor = 0.1
        for i in range(self.dim):
            xi = x[i]
            # Introduce chaotic behavior through sine and cosine combinations
            result += chaos_factor * np.sin(3.0 * xi) * np.cos(2.0 * xi) * np.sin(0.5 * xi)
            
        # Add a complex interaction term between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j < self.dim:
                    interaction = 0.2 * np.cos(0.3 * (i + j)) * self.fractal_factors[i] * self.fractal_factors[j]
                    result += interaction * (x[i]**2 + x[j]**2)
                    
        return result