import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.57) * np.cos(i * 0.83) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with stronger non-linearity
        for i in range(self.dim):
            result += 0.91 * np.exp(-0.32 * np.abs(x[i])) * np.sin(3.7 * np.pi * x[i])
            
        # Multi-scale phase interactions with dynamic coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.68 * np.sin(phase_sum * 1.32) * np.cos(phase_sum * 0.89)
        
        # Increased frequency oscillations with variable amplitudes
        for i in range(self.dim):
            freq = 2.3 + 5.7 * np.sin(i * 0.45)
            amp = 1.56 + 0.67 * np.cos(i * 0.31)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.52)
            
        # Stronger cross-dimensional correlations with modified decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.067 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j] * 0.73)
                result += decay * interaction
                
        # Sharper, more numerous local minima
        for i in range(self.dim):
            result += 0.24 * np.sin(15.7 * x[i]) * np.cos(7.3 * x[i]) * np.exp(-0.024 * x[i]**2)
            
        # Dynamic global attractor with time-varying strength
        dynamic_scale = np.sum(np.sin(x)**2) + 1.43
        result += 0.37 * np.sin(np.sum(x) * dynamic_scale * 0.87) * np.cos(np.sum(x) * 0.51 * dynamic_scale)
        
        # High-order non-separable interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.128 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k] * 0.67)
                    
        # Enhanced logarithmic penalty for global minimization
        result += 0.038 * np.sum(np.log(1.0 + np.abs(x)))
        
        # New global minimum attractor with asymmetric basin
        result += 0.16 * np.prod(np.cos(0.78 * x)) * np.exp(-0.015 * np.sum(x**2))
        
        # Complex noise structure with multi-frequency components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.42 * np.sin(13.9 * x[i]) * np.cos(6.7 * x[i]) * np.exp(-0.071 * i)
        result += noise
        
        # Time-varying basin complexity with dynamic scaling
        time_factor = np.sin(np.sum(x) * 0.17) + 1.23
        result += 0.23 * np.sum(np.sin(x * time_factor * 1.15) * np.cos(x * time_factor * 0.41))
        
        # Multi-scale chaotic boundaries with variable sharpness
        for i in range(self.dim):
            result += 0.31 * np.sin(10.2 * x[i]) * np.cos(5.1 * x[i]) * np.exp(-0.031 * np.abs(x[i]))
            
        # High-frequency chaotic noise with memory effects
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.18 * np.sin(25.4 * x[i]) * np.cos(12.7 * x[i])
        result += freq_noise
        
        # Fractal self-similarity with enhanced complexity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.0 * x[i])
        result += 0.19 * fractal_term
        
        # Memory-dependent influence with historical scaling
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.087 * self.history[i] * np.sin(x[i] * 0.71)
        result += hist_influence
        self.history = x.copy()
        
        # Multi-modal structure with memory-enhanced complexity
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.124 * np.sin(7.2 * x[i]) * np.cos(3.6 * x[i]) * np.exp(-0.018 * np.abs(x[i]))
        result += multi_modal
        
        return result