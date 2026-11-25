import numpy as np

class FractalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters with fractal-like scaling
        self.freq_params = np.random.uniform(0.5, 3.0, dim)
        self.exp_params = np.random.uniform(0.1, 1.5, dim)
        self.poly_params = np.random.uniform(-0.5, 0.5, dim)
        self.fractal_scale = np.random.uniform(0.3, 0.8, dim)
        self.modulation_freq = np.random.uniform(2.0, 6.0, dim)
        
    def f(self, x):
        # Clip input to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Main sinusoidal + exponential components with dynamic modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.freq_params[i]
            exp_decay = self.exp_params[i]
            
            # Sinusoidal term modulated by exponential decay
            sin_term = np.sin(freq * xi) * np.exp(-exp_decay * np.abs(xi))
            
            # Add polynomial correction
            poly_corr = self.poly_params[i] * xi**4
            
            result += sin_term + poly_corr
            
        # Cross-dimensional coupling with fractal scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                xi, xj = x[i], x[j]
                scale = self.fractal_scale[i] * self.fractal_scale[j]
                
                # Fractal-like interaction with scaling factor
                coupling = scale * np.sin(xi + xj) * np.cos(xi - xj)
                result += coupling
                
        # Dynamic modulation component based on sum of variables
        sum_x = np.sum(x)
        for i in range(self.dim):
            xi = x[i]
            mod_freq = self.modulation_freq[i]
            
            # Time-varying modulation with dynamic frequency
            modulation = np.sin(mod_freq * sum_x + 0.5 * i) * np.cos(0.3 * xi)
            result += 0.1 * modulation
            
        # Add polynomial ridge structure
        ridge_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            ridge_height = 0.2 + 0.1 * np.sin(0.5 * i)
            ridge_width = 0.8 + 0.3 * np.cos(0.4 * i)
            
            # Ridge-like structure with variable height and width
            ridge_term += ridge_height * (np.sin(ridge_width * xi) ** 2) * np.exp(-0.1 * xi**2)
            
        result += ridge_term
        
        # Add global scaling factor with fractal characteristics
        global_factor = 1.0 + 0.3 * np.sin(0.2 * self.dim + 0.1 * sum_x)
        result *= global_factor
        
        return result