import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize dynamic parameters that change with evaluation count
        self.eval_count = 0
        self.base_freqs = np.random.uniform(1.5, 4.0, dim)
        self.correlation_strength = np.random.uniform(0.2, 1.0, dim)
        self.saddle_positions = np.random.uniform(-4.5, 4.5, dim)
        self.basin_shifts = np.random.uniform(-0.8, 0.8, dim)
        self.fractal_dims = np.random.uniform(1.1, 2.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Update dynamic parameters based on evaluation count
        self.eval_count += 1
        time_factor = 0.02 * self.eval_count
        current_freqs = self.base_freqs * (1.0 + 0.3 * np.sin(time_factor))
        current_corr = self.correlation_strength * (1.0 + 0.2 * np.cos(time_factor))
        
        # Saddle point landscape with dynamic positioning and fractal structure
        saddle_term = 0.0
        for i in range(self.dim):
            pos = self.saddle_positions[i] + 0.15 * np.sin(time_factor * (i + 1))
            # Fractal-inspired saddle with hyper-saddle characteristics
            fractal_saddle = (x[i] - pos)**2 * (x[i]**4 - 8.0 * x[i]**2 + 16.0) * np.exp(-0.15 * (x[i] - pos)**2)
            saddle_term += fractal_saddle
        saddle_term /= self.dim
        
        # Enhanced adaptive correlation structure with fractal dimensions
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr = current_corr[i] * current_corr[j]
                # Fractal correlation with multi-scale interaction
                fractal_corr = corr * np.sin(x[i] + x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                fractal_corr *= (1.0 + 0.1 * np.sin(self.fractal_dims[i] * x[i] + self.fractal_dims[j] * x[j]))
                corr_term += fractal_corr
        corr_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Time-varying basin structure with chaotic shifts and fractal basins
        basin_term = 0.0
        for i in range(self.dim):
            shift = self.basin_shifts[i] + 0.1 * np.sin(time_factor * (i + 1) * 3.0)
            # Fractal basin structure with higher-order polynomial
            basin = (x[i]**6 - 15.0 * x[i]**4 + 70.0 * x[i]**2 - 64.0) * np.exp(-0.1 * (x[i] - shift)**2)
            basin_term += basin
        basin_term /= self.dim
        
        # Multi-frequency oscillation with chaotic phase modulation and fractal harmonics
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = current_freqs[i]
            phase = 0.4 * np.sin(time_factor + i * 0.7)
            # Fractal harmonic oscillation
            oscillation = np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            oscillation *= (1.0 + 0.2 * np.sin(self.fractal_dims[i] * x[i]))
            oscillation_term += oscillation
        oscillation_term /= self.dim
        
        # Dynamic fitness scaling based on current evaluation with chaotic factor
        scale_factor = 1.0 + 0.5 * np.sin(time_factor * 0.7)
        
        # Combine all terms with adaptive weights
        total = (0.25 * saddle_term + 
                 0.25 * corr_term + 
                 0.3 * basin_term + 
                 0.2 * oscillation_term) * scale_factor
        
        return total