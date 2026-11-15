import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.51) * np.cos(i * 0.73) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with higher frequency oscillations
        for i in range(self.dim):
            result += 0.81 * np.exp(-0.27 * np.abs(x[i])) * np.sin(3.4 * np.pi * x[i])
            
        # Stronger phase interactions with time-varying coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.63 * np.sin(phase_sum) * np.cos(phase_sum * 0.81)
        
        # Multi-scale oscillatory terms with increased frequency and amplitude variations
        for i in range(self.dim):
            freq = 2.1 + 5.3 * np.sin(i * 0.42)
            amp = 1.41 + 0.58 * np.cos(i * 0.31)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.51)
            
        # Cross-dimensional interaction with stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.058 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper and more numerous peaks
        for i in range(self.dim):
            result += 0.23 * np.sin(15.7 * x[i]) * np.cos(7.9 * x[i]) * np.exp(-0.021 * x[i]**2)
            
        # Dynamic scaling with enhanced chaotic behavior
        dynamic_scale = np.sum(np.sin(x)**2) + 1.37
        result += 0.34 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.51 * dynamic_scale)
        
        # Increased high-order non-separable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.128 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Enhanced global minimum enforcing with logarithmic penalty
        result += 0.031 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Additional global minimum attractor with increased complexity
        result += 0.15 * np.prod(np.cos(0.71 * x))
        
        # Enhanced noise and perturbation components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.42 * np.sin(13.7 * x[i]) * np.cos(6.8 * x[i]) * np.exp(-0.071 * i)
        result += noise
        
        # Dynamic basin complexity with stronger time-varying attractors
        time_factor = np.sin(np.sum(x) * 0.17) + 1.0
        result += 0.22 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.42))
        
        # Multi-scale chaotic basin boundaries with higher complexity
        for i in range(self.dim):
            result += 0.29 * np.sin(10.2 * x[i]) * np.cos(5.1 * x[i]) * np.exp(-0.031 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with increased intensity
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.15 * np.sin(25.4 * x[i]) * np.cos(12.7 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity with higher dimensional complexity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.0 * x[i])
        result += 0.18 * fractal_term
        
        # Memory-dependent fitness with stronger historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.083 * self.history[i] * np.sin(x[i] * 0.67)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with enhanced memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.124 * np.sin(7.2 * x[i]) * np.cos(3.6 * x[i]) * np.exp(-0.015 * np.abs(x[i]))
        result += multi_modal
        
        # Additional chaotic basin complexity with increased dimensionality
        basin_complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                basin_complexity += 0.047 * np.sin(x[i] * x[j]) * np.cos(x[i] * x[j] * 0.29)
        result += basin_complexity
        
        # Ultra-high frequency noise component
        ultra_noise = 0.0
        for i in range(self.dim):
            ultra_noise += 0.08 * np.sin(32.9 * x[i]) * np.cos(16.4 * x[i])
        result += ultra_noise
        
        # Increased non-separability with higher-order terms
        non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        non_sep += 0.032 * x[i] * x[j] * x[k] * x[l] * np.sin(x[i] * x[j] * x[k] * x[l])
        result += non_sep
        
        return result