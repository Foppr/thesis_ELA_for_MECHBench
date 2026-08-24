import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.39) * np.cos(i * 0.71) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
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
            freq = 2.1 + 3.9 * np.sin(i * 0.42)
            amp = 1.31 + 0.38 * np.cos(i * 0.29)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.51)
            
        # Enhanced cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.052 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper asymmetric ruggedness
        for i in range(self.dim):
            result += 0.21 * np.sin(14.3 * x[i]) * np.cos(7.2 * x[i]) * np.exp(-0.021 * x[i]**2)
            
        # Dynamic scaling chaotic component
        dynamic_scale = np.sum(np.sin(x)**2) + 1.32
        result += 0.34 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.49 * dynamic_scale)
        
        # Increased high-order non-separable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.108 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Improved global minimum enforcing
        result += 0.031 * np.sum(np.log(1.0 + np.abs(x)))
        
        # New global minimum attractor
        result += 0.15 * np.prod(np.cos(0.68 * x))
        
        # Enhanced noise and perturbation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.41 * np.sin(12.3 * x[i]) * np.cos(6.1 * x[i]) * np.exp(-0.065 * i)
        result += noise
        
        # Dynamic basin complexity with time-varying attractors
        time_factor = np.sin(np.sum(x) * 0.15) + 1.0
        result += 0.21 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.41))
        
        # Multi-scale chaotic basin boundaries
        for i in range(self.dim):
            result += 0.27 * np.sin(9.4 * x[i]) * np.cos(4.7 * x[i]) * np.exp(-0.028 * np.abs(x[i]))
            
        # High-frequency oscillatory noise
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.15 * np.sin(23.7 * x[i]) * np.cos(11.8 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity component
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(3.7 * x[i]) * np.cos(1.8 * x[i])
        result += 0.16 * fractal_term
        
        # Memory-dependent fitness with stronger influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.073 * self.history[i] * np.sin(x[i] * 0.65)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.107 * np.sin(6.4 * x[i]) * np.cos(3.2 * x[i]) * np.exp(-0.015 * np.abs(x[i]))
        result += multi_modal
        
        return result