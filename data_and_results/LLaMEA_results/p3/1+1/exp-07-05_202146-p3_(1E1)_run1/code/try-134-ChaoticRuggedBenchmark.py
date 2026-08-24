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
            result += 0.85 * np.exp(-0.28 * np.abs(x[i])) * np.sin(3.7 * np.pi * x[i])
            
        # Stronger phase coupling with time-varying coefficients
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.67 * np.sin(phase_sum * 1.23) * np.cos(phase_sum * 0.89)
        
        # Multi-scale oscillatory terms with increased amplitude and frequency
        for i in range(self.dim):
            freq = 2.3 + 5.7 * np.sin(i * 0.41)
            amp = 1.56 + 0.68 * np.cos(i * 0.31)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.52)
            
        # Cross-dimensional interaction with stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.065 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper and more numerous peaks
        for i in range(self.dim):
            result += 0.24 * np.sin(15.7 * x[i]) * np.cos(7.3 * x[i]) * np.exp(-0.023 * x[i]**2)
            
        # Dynamic scaling with enhanced chaotic behavior
        dynamic_scale = np.sum(np.sin(x)**2) + 1.45
        result += 0.38 * np.sin(np.sum(x) * dynamic_scale * 1.12) * np.cos(np.sum(x) * 0.51 * dynamic_scale)
        
        # Higher-order non-separable interactions with increased influence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.134 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k] * 1.3)
                    
        # Improved global minimum enforcing with logarithmic penalty
        result += 0.032 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Additional global minimum attractor with enhanced complexity
        result += 0.17 * np.prod(np.cos(0.71 * x))
        
        # Enhanced noise and perturbation components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.42 * np.sin(13.4 * x[i]) * np.cos(6.7 * x[i]) * np.exp(-0.071 * i)
        result += noise
        
        # Dynamic basin complexity with multi-time-varying attractors
        time_factor = np.sin(np.sum(x) * 0.17) + 1.0
        result += 0.23 * np.sum(np.sin(x * time_factor * 1.3) * np.cos(x * time_factor * 0.41))
        
        # Multi-scale chaotic basin boundaries with increased complexity
        for i in range(self.dim):
            result += 0.31 * np.sin(10.2 * x[i]) * np.cos(5.1 * x[i]) * np.exp(-0.031 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with increased intensity
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.18 * np.sin(25.6 * x[i]) * np.cos(12.8 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity with increased complexity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.05 * x[i])
        result += 0.19 * fractal_term
        
        # Memory-dependent fitness with stronger historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.087 * self.history[i] * np.sin(x[i] * 0.65)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with memory effects and enhanced complexity
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.123 * np.sin(7.2 * x[i]) * np.cos(3.6 * x[i]) * np.exp(-0.015 * np.abs(x[i]))
        result += multi_modal
        
        # Add a new chaotic basin structure with higher dimensionality
        basin_complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                basin_complexity += 0.057 * np.sin(x[i] * x[j]) * np.cos(x[i] * x[j] * 0.33)
        result += basin_complexity
        
        # Add a new multi-scale chaotic structure with enhanced complexity
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += 0.29 * np.sin(9.8 * x[i]) * np.cos(4.9 * x[i]) * np.exp(-0.038 * np.abs(x[i]))
        result += multi_scale
        
        return result