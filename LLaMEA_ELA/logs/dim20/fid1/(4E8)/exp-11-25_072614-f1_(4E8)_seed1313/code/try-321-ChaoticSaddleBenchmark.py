import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize dynamic parameters that change with evaluation count
        self.eval_count = 0
        self.base_freqs = np.random.uniform(1.0, 3.0, dim)
        self.correlation_strength = np.random.uniform(0.1, 0.9, dim)
        self.saddle_positions = np.random.uniform(-4.0, 4.0, dim)
        self.basin_shifts = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Update dynamic parameters based on evaluation count
        self.eval_count += 1
        time_factor = 0.01 * self.eval_count
        current_freqs = self.base_freqs * (1.0 + 0.2 * np.sin(time_factor))
        current_corr = self.correlation_strength * (1.0 + 0.1 * np.cos(time_factor))
        
        # Saddle point landscape with dynamic positioning
        saddle_term = 0.0
        for i in range(self.dim):
            pos = self.saddle_positions[i] + 0.1 * np.sin(time_factor * (i + 1))
            saddle_term += (x[i] - pos)**2 * (x[i]**2 - 4.0) * np.exp(-0.1 * (x[i] - pos)**2)
        saddle_term /= self.dim
        
        # Adaptive correlation structure
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr = current_corr[i] * current_corr[j]
                corr_term += corr * np.sin(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        corr_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Time-varying basin structure with chaotic shifts
        basin_term = 0.0
        for i in range(self.dim):
            shift = self.basin_shifts[i] + 0.05 * np.sin(time_factor * (i + 1) * 2.0)
            basin_term += (x[i]**4 - 6.0 * x[i]**2 + 8.0) * np.exp(-0.1 * (x[i] - shift)**2)
        basin_term /= self.dim
        
        # Multi-frequency oscillation with chaotic phase modulation
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = current_freqs[i]
            phase = 0.3 * np.sin(time_factor + i * 0.5)
            oscillation_term += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
        oscillation_term /= self.dim
        
        # Dynamic fitness scaling based on current evaluation
        scale_factor = 1.0 + 0.3 * np.sin(time_factor * 0.5)
        
        # Combine all terms with adaptive weights
        total = (0.3 * saddle_term + 
                 0.2 * corr_term + 
                 0.3 * basin_term + 
                 0.2 * oscillation_term) * scale_factor
        
        return total