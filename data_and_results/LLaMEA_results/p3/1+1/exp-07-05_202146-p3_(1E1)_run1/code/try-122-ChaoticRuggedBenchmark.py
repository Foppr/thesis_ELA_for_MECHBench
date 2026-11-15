import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.73) * np.cos(i * 0.91) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced ruggedness with double harmonic modulation
        for i in range(self.dim):
            result += 1.15 * np.exp(-0.32 * np.abs(x[i])) * np.sin(3.7 * np.pi * x[i]) * np.cos(1.9 * np.pi * x[i])
            
        # Stronger chaotic phase interactions
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i)) * np.cos(x[i] * 0.45)
        result += 0.78 * np.sin(phase_sum * 1.3) * np.cos(phase_sum * 0.87)
        
        # Multi-scale oscillatory terms with increased frequency diversity
        for i in range(self.dim):
            freq = 2.3 + 5.8 * np.sin(i * 0.47)
            amp = 1.56 + 0.68 * np.cos(i * 0.32)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.63)
            
        # Cross-dimensional interaction with power-law decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = (i + j + 1)**(-1.2)
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper and more numerous peaks
        for i in range(self.dim):
            result += 0.28 * np.sin(17.4 * x[i]) * np.cos(9.2 * x[i]) * np.exp(-0.025 * x[i]**2)
            
        # Dynamic scaling chaotic component
        dynamic_scale = np.sum(np.sin(x)**2) + 1.53
        result += 0.41 * np.sin(np.sum(x) * dynamic_scale * 0.7) * np.cos(np.sum(x) * 0.61 * dynamic_scale)
        
        # High-order non-separable interactions with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.145 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k] * 0.8)
                    
        # Global minimum enforcing with inverse-logarithmic penalty
        result += 0.042 * np.sum(1.0 / (1.0 + np.abs(x)))
        
        # New global minimum attractor with hyperbolic tangent
        result += 0.19 * np.prod(np.tanh(0.78 * x))
        
        # Enhanced noise and perturbation with adaptive weights
        noise = 0.0
        for i in range(self.dim):
            noise += 0.48 * np.sin(14.7 * x[i]) * np.cos(7.3 * x[i]) * np.exp(-0.071 * i)
        result += noise
        
        # Dynamic basin complexity with dual time-varying attractors
        time_factor1 = np.sin(np.sum(x) * 0.17) + 1.0
        time_factor2 = np.cos(np.sum(x) * 0.23) + 1.0
        result += 0.24 * np.sum(np.sin(x * time_factor1) * np.cos(x * time_factor2 * 0.42))
        
        # Multi-scale chaotic basin boundaries with asymmetric scaling
        for i in range(self.dim):
            result += 0.31 * np.sin(10.2 * x[i]) * np.cos(5.1 * x[i]) * np.exp(-0.031 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with variable amplitude
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.18 * np.sin(25.3 * x[i]) * np.cos(12.6 * x[i]) * (1.0 + 0.2 * np.sin(i * 0.5))
        result += freq_noise
        
        # Fractal-like self-similarity with variable scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.0 * x[i])
        result += 0.19 * fractal_term
        
        # Memory-dependent fitness with exponential influence decay
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.087 * self.history[i] * np.sin(x[i] * 0.71) * np.exp(-0.015 * i)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with overlapping basins
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.134 * np.sin(7.2 * x[i]) * np.cos(3.6 * x[i]) * np.exp(-0.018 * np.abs(x[i]))
        result += multi_modal
        
        return result