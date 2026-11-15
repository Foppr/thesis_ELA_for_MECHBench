import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.42) * np.cos(i * 0.68) for i in range(dim)])
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced rugged component with sharper peaks
        for i in range(self.dim):
            result += 0.72 * np.exp(-0.22 * np.abs(x[i])) * np.sin(3.1 * np.pi * x[i])
            
        # Chaotic phase interactions with stronger coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.52 * np.sin(phase_sum) * np.cos(phase_sum * 0.72)
        
        # Multi-scale oscillatory terms with frequency variations
        for i in range(self.dim):
            freq = 1.8 + 4.2 * np.sin(i * 0.38)
            amp = 1.25 + 0.42 * np.cos(i * 0.25)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.38)
            
        # Cross-dimensional interaction with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.042 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Asymmetric ruggedness with sharper peaks
        for i in range(self.dim):
            result += 0.18 * np.sin(14.2 * x[i]) * np.cos(7.1 * x[i]) * np.exp(-0.018 * x[i]**2)
            
        # Dynamic scaling component
        dynamic_scale = np.sum(np.sin(x)**2) + 1.22
        result += 0.31 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.45 * dynamic_scale)
        
        # High-order non-separable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.105 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Global minimum enforcing with logarithmic penalty
        result += 0.025 * np.sum(np.log(1.0 + np.abs(x)))
        
        # New global minimum attractor
        result += 0.13 * np.prod(np.cos(0.62 * x))
        
        # Enhanced noise and perturbation components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.38 * np.sin(11.8 * x[i]) * np.cos(5.9 * x[i]) * np.exp(-0.061 * i)
        result += noise
        
        # Dynamic basin complexity with time-varying attractors
        time_factor = np.sin(np.sum(x) * 0.13) + 1.0
        result += 0.19 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.35))
        
        # Multi-scale chaotic basin boundaries
        for i in range(self.dim):
            result += 0.25 * np.sin(9.1 * x[i]) * np.cos(4.5 * x[i]) * np.exp(-0.025 * np.abs(x[i]))
            
        # High-frequency oscillatory noise
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.13 * np.sin(22.3 * x[i]) * np.cos(11.1 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity component
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(3.5 * x[i]) * np.cos(1.75 * x[i])
        result += 0.15 * fractal_term
        
        # Memory-dependent fitness with historical influence
        if hasattr(self, 'history'):
            hist_influence = 0.0
            for i in range(self.dim):
                hist_influence += 0.065 * self.history[i] * np.sin(x[i] * 0.58)
            result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.105 * np.sin(6.1 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.013 * np.abs(x[i]))
        result += multi_modal
        
        return result