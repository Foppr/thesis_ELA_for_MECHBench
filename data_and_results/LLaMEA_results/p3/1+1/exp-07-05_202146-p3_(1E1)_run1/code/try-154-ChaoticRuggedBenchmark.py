import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.38) * np.cos(i * 0.72) for i in range(dim)])
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced rugged component with sharper peaks
        for i in range(self.dim):
            result += 0.81 * np.exp(-0.25 * np.abs(x[i])) * np.sin(3.1 * np.pi * x[i])
            
        # Stronger chaotic phase interactions
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.11 * i))
        result += 0.63 * np.sin(phase_sum) * np.cos(phase_sum * 0.81)
        
        # Modified multi-scale oscillatory terms
        for i in range(self.dim):
            freq = 2.1 + 3.8 * np.sin(i * 0.42)
            amp = 1.31 + 0.38 * np.cos(i * 0.29)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.51)
            
        # Cross-dimensional interaction with stronger correlation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.052 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Asymmetric ruggedness with more pronounced peaks
        for i in range(self.dim):
            result += 0.22 * np.sin(14.1 * x[i]) * np.cos(7.3 * x[i]) * np.exp(-0.021 * x[i]**2)
            
        # Dynamic scaling chaotic component
        dynamic_scale = np.sum(np.sin(x)**2) + 1.32
        result += 0.34 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.49 * dynamic_scale)
        
        # Increased non-separable high-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.11 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Enhanced global minimum enforcing with logarithmic penalty
        result += 0.031 * np.sum(np.log(1.0 + np.abs(x)))
        
        # New global minimum attractor with stronger influence
        result += 0.15 * np.prod(np.cos(0.68 * x))
        
        # Improved noise and perturbation components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.41 * np.sin(12.3 * x[i]) * np.cos(6.1 * x[i]) * np.exp(-0.063 * i)
        result += noise
        
        # Dynamic basin complexity with stronger time-varying attractors
        time_factor = np.sin(np.sum(x) * 0.15) + 1.0
        result += 0.21 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.41))
        
        # Enhanced multi-scale chaotic basin boundaries
        for i in range(self.dim):
            result += 0.27 * np.sin(9.4 * x[i]) * np.cos(4.7 * x[i]) * np.exp(-0.028 * np.abs(x[i]))
            
        # Additional high-frequency oscillatory noise
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.15 * np.sin(23.7 * x[i]) * np.cos(11.8 * x[i])
        result += freq_noise
        
        # Improved fractal-like self-similarity component
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(3.7 * x[i]) * np.cos(1.8 * x[i])
        result += 0.17 * fractal_term
        
        # Memory-dependent fitness with stronger historical influence
        if hasattr(self, 'history'):
            hist_influence = 0.0
            for i in range(self.dim):
                hist_influence += 0.073 * self.history[i] * np.sin(x[i] * 0.64)
            result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with stronger memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.108 * np.sin(6.2 * x[i]) * np.cos(3.1 * x[i]) * np.exp(-0.014 * np.abs(x[i]))
        result += multi_modal
        
        return result