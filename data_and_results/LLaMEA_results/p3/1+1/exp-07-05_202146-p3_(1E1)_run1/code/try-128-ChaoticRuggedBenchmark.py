import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.51) * np.cos(i * 0.73) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with non-linear coupling
        for i in range(self.dim):
            result += 0.81 * np.exp(-0.27 * np.abs(x[i])) * np.sin(3.1 * np.pi * x[i])
            
        # Multi-scale phase interactions with dynamic coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.63 * np.sin(phase_sum) * np.cos(phase_sum * 0.81)
        
        # Complex oscillatory terms with frequency modulation
        for i in range(self.dim):
            freq = 2.1 + 4.7 * np.sin(i * 0.42)
            amp = 1.35 + 0.48 * np.cos(i * 0.29)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.51)
            
        # Cross-dimensional interaction with variable decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.052 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharp peak ruggedness with exponential decay
        for i in range(self.dim):
            result += 0.23 * np.sin(15.7 * x[i]) * np.cos(7.3 * x[i]) * np.exp(-0.022 * x[i]**2)
            
        # Dynamic scaling chaotic component
        dynamic_scale = np.sum(np.sin(x)**2) + 1.34
        result += 0.34 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.49 * dynamic_scale)
        
        # High-order non-separable interactions with variable weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.11 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k] * 0.7)
                    
        # Global minimum enforcing with logarithmic penalty
        result += 0.03 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Multi-minimum attractor with enhanced basin complexity
        result += 0.15 * np.prod(np.cos(0.71 * x))
        
        # Enhanced noise with dynamic frequency components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.41 * np.sin(12.3 * x[i]) * np.cos(6.1 * x[i]) * np.exp(-0.065 * i)
        result += noise
        
        # Time-varying basin complexity with memory effects
        time_factor = np.sin(np.sum(x) * 0.17) + 1.0
        result += 0.21 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.41))
        
        # Multi-scale chaotic boundaries with enhanced complexity
        for i in range(self.dim):
            result += 0.27 * np.sin(9.4 * x[i]) * np.cos(4.7 * x[i]) * np.exp(-0.028 * np.abs(x[i]))
            
        # High-frequency noise with phase modulation
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.15 * np.sin(23.7 * x[i]) * np.cos(11.8 * x[i])
        result += freq_noise
        
        # Fractal self-similarity with increased complexity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(3.8 * x[i]) * np.cos(1.9 * x[i])
        result += 0.17 * fractal_term
        
        # Memory-dependent fitness with historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.073 * self.history[i] * np.sin(x[i] * 0.65)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with enhanced memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.11 * np.sin(6.5 * x[i]) * np.cos(3.2 * x[i]) * np.exp(-0.015 * np.abs(x[i]))
        result += multi_modal
        
        # Additional chaotic basin complexity with variable parameters
        basin_complexity = 0.0
        for i in range(self.dim):
            basin_complexity += 0.08 * np.sin(10.2 * x[i]) * np.cos(5.1 * x[i]) * np.exp(-0.031 * np.abs(x[i]))
        result += basin_complexity
        
        # Add a new type of interaction term with increased complexity
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        interaction_term += 0.03 * x[i] * x[j] * x[k] * x[l] * np.sin(x[i] * x[j] * x[k] * x[l] * 0.5)
        result += interaction_term
        
        return result