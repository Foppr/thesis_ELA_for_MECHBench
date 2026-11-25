import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize dynamic parameters that change with evaluation count
        self.eval_count = 0
        self.base_freqs = np.random.uniform(1.2, 3.8, dim)
        self.correlation_strength = np.random.uniform(0.15, 0.95, dim)
        self.saddle_positions = np.random.uniform(-4.5, 4.5, dim)
        self.basin_shifts = np.random.uniform(-0.7, 0.7, dim)
        self.fractal_dims = np.random.uniform(1.05, 2.4, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Update dynamic parameters based on evaluation count
        self.eval_count += 1
        time_factor = 0.02 * self.eval_count
        current_freqs = self.base_freqs * (1.0 + 0.25 * np.sin(time_factor))
        current_corr = self.correlation_strength * (1.0 + 0.18 * np.cos(time_factor))
        
        # Enhanced saddle point landscape with higher-order hyper-saddle characteristics
        saddle_term = 0.0
        for i in range(self.dim):
            pos = self.saddle_positions[i] + 0.12 * np.sin(time_factor * (i + 1))
            # Higher-order fractal saddle with enhanced non-linearity
            x_i = x[i] - pos
            fractal_saddle = (x_i**2) * (x_i**6 - 12.0 * x_i**4 + 48.0 * x_i**2 - 32.0) * np.exp(-0.12 * x_i**2)
            saddle_term += fractal_saddle
        saddle_term /= self.dim
        
        # Refined adaptive correlation structure with multi-scale interaction
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr = current_corr[i] * current_corr[j]
                # Enhanced fractal correlation with asymmetric coupling
                asym_corr = corr * np.sin(x[i] + x[j]) * np.cos(0.5 * (x[i] - x[j]))
                asym_corr *= (1.0 + 0.12 * np.sin(self.fractal_dims[i] * x[i] + self.fractal_dims[j] * x[j]))
                corr_term += asym_corr
        corr_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Improved basin structure with enhanced chaotic shifts and fractal characteristics
        basin_term = 0.0
        for i in range(self.dim):
            shift = self.basin_shifts[i] + 0.08 * np.sin(time_factor * (i + 1) * 2.5)
            # Enhanced fractal basin with polynomial and exponential components
            x_i = x[i] - shift
            basin = (x_i**8 - 28.0 * x_i**6 + 336.0 * x_i**4 - 1792.0 * x_i**2 + 1024.0) * np.exp(-0.08 * x_i**2)
            basin_term += basin
        basin_term /= self.dim
        
        # Refined oscillation term with improved chaotic phase modulation and fractal harmonics
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = current_freqs[i]
            phase = 0.3 * np.sin(time_factor + i * 0.6)
            # Enhanced fractal harmonic with asymmetric components
            sin_part = np.sin(freq * x[i] + phase)
            cos_part = np.cos(freq * x[i] + phase)
            oscillation = sin_part * cos_part * (1.0 + 0.15 * np.sin(self.fractal_dims[i] * x[i]))
            oscillation_term += oscillation
        oscillation_term /= self.dim
        
        # Enhanced dynamic fitness scaling with improved chaotic factor
        scale_factor = 1.0 + 0.4 * np.sin(time_factor * 0.6)
        
        # Combine all terms with refined weights for better optimization challenge
        total = (0.3 * saddle_term + 
                 0.25 * corr_term + 
                 0.35 * basin_term + 
                 0.1 * oscillation_term) * scale_factor
        
        return total