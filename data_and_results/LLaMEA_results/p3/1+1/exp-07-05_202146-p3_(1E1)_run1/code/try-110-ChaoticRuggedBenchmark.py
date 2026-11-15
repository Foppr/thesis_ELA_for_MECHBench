import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.73) * np.cos(i * 0.91) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced rugged component with double exponential decay
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.35 * np.abs(x[i])) * np.sin(3.7 * np.pi * x[i]) * np.cos(1.9 * np.pi * x[i])
            
        # Stronger chaotic phase interactions with dynamic coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i)) * np.cos(x[i] * 0.31)
        result += 0.8 * np.sin(phase_sum * 1.4) * np.cos(phase_sum * 0.87)
        
        # Multi-scale oscillatory terms with frequency modulation
        for i in range(self.dim):
            freq = 2.1 + 5.3 * np.sin(i * 0.42) * np.cos(i * 0.29)
            amp = 1.5 + 0.6 * np.sin(i * 0.37) * np.cos(i * 0.53)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.61)
            
        # Cross-dimensional interaction with time-varying decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.06 * (i + j)) * np.sin(0.13 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                result += decay * interaction
                
        # Sharper and more numerous peaks with asymmetric ruggedness
        for i in range(self.dim):
            result += 0.25 * np.sin(17.3 * x[i]) * np.cos(9.4 * x[i]) * np.exp(-0.025 * x[i]**2)
            
        # Dynamic scaling with multi-dimensional feedback
        dynamic_scale = np.sum(np.sin(x)**2) + 1.5
        result += 0.42 * np.sin(np.sum(x) * dynamic_scale * 0.7) * np.cos(np.sum(x) * 0.55 * dynamic_scale)
        
        # High-order non-separable interactions with variable weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    weight = 0.12 * np.sin(i * 0.31) * np.cos(j * 0.27)
                    result += weight * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k] * 0.8)
                    
        # Global minimum enforcing with enhanced penalty
        result += 0.04 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(x))
        
        # New global minimum attractor with multi-dimensional resonance
        result += 0.18 * np.prod(np.cos(0.83 * x)) * np.sin(np.sum(x) * 0.29)
        
        # Enhanced noise with multi-frequency components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.5 * np.sin(15.7 * x[i]) * np.cos(7.8 * x[i]) * np.exp(-0.08 * i) * np.sin(0.23 * i)
        result += noise
        
        # Dynamic basin complexity with memory-dependent attractors
        time_factor = np.sin(np.sum(x) * 0.17) + 1.3
        result += 0.25 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.42) * np.exp(-0.015 * np.abs(x)))
        
        # Multi-scale chaotic basin boundaries with fractal-like behavior
        for i in range(self.dim):
            result += 0.31 * np.sin(11.2 * x[i]) * np.cos(5.6 * x[i]) * np.exp(-0.031 * np.abs(x[i])) * np.sin(0.19 * x[i])
            
        # High-frequency oscillatory noise with amplitude modulation
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.18 * np.sin(25.4 * x[i]) * np.cos(12.7 * x[i]) * np.cos(0.33 * i)
        result += freq_noise
        
        # Fractal-like self-similarity with enhanced complexity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.05 * x[i]) * np.sin(0.27 * x[i])
        result += 0.21 * fractal_term
        
        # Memory-dependent fitness with feedback loops
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.08 * self.history[i] * np.sin(x[i] * 0.71) * np.cos(x[i] * 0.43)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with dynamic peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.12 * np.sin(7.9 * x[i]) * np.cos(3.95 * x[i]) * np.exp(-0.018 * np.abs(x[i])) * np.sin(0.35 * x[i])
        result += multi_modal
        
        return result