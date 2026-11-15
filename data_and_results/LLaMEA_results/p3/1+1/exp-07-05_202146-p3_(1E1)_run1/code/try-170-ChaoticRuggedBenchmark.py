import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.51) * np.cos(i * 0.73) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with dynamic frequency modulation
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(x[i] * 0.3)
            result += 0.85 * np.exp(-0.18 * np.abs(x[i])) * np.sin(freq_mod * 2.7 * np.pi * x[i])
            
        # Multi-scale phase interactions with time-varying coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i)) * np.cos(x[i] * 0.42)
        result += 0.63 * np.sin(phase_sum * 1.2) * np.cos(phase_sum * 0.85)
        
        # Complex oscillatory terms with variable amplitude and frequency
        for i in range(self.dim):
            freq = 2.1 + 3.9 * np.sin(i * 0.41)
            amp = 1.35 + 0.38 * np.cos(i * 0.29)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.52)
            
        # Cross-dimensional interactions with non-uniform decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.06 * (i + j) * np.sin(x[i] + x[j]))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j] * 0.3)
                result += decay * interaction
                
        # Sharp, asymmetric peaks with enhanced non-linearity
        for i in range(self.dim):
            result += 0.22 * np.sin(15.3 * x[i]) * np.cos(7.2 * x[i]) * np.exp(-0.022 * x[i]**2)
            
        # Dynamic scaling chaotic attractor with multi-dimensional influence
        dynamic_scale = np.sum(np.sin(x)**2) + 1.35
        result += 0.34 * np.sin(np.sum(x) * dynamic_scale * 0.8) * np.cos(np.sum(x) * 0.5 * dynamic_scale)
        
        # High-order non-separable interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.11 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k] * 0.7)
                    
        # Global minimum enforcing with enhanced penalty
        result += 0.03 * np.sum(np.log(1.0 + np.abs(x)) * np.exp(-0.01 * np.sum(x**2)))
        
        # Multi-modal attractor with fractal basin boundaries
        result += 0.15 * np.prod(np.cos(0.7 * x))
        
        # Enhanced noise and perturbation with multi-frequency components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.41 * np.sin(13.7 * x[i]) * np.cos(6.8 * x[i]) * np.exp(-0.07 * i)
        result += noise
        
        # Time-varying basin complexity with dynamic attractor positioning
        time_factor = np.sin(np.sum(x) * 0.17) + 1.15
        result += 0.21 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.42))
        
        # Multi-scale chaotic boundaries with enhanced complexity
        for i in range(self.dim):
            result += 0.27 * np.sin(9.5 * x[i]) * np.cos(4.7 * x[i]) * np.exp(-0.028 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with amplitude modulation
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.15 * np.sin(24.1 * x[i]) * np.cos(12.0 * x[i]) * np.cos(x[i] * 0.3)
        result += freq_noise
        
        # Fractal-like self-similarity with enhanced dimensionality
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(3.8 * x[i]) * np.cos(1.9 * x[i])
        result += 0.18 * fractal_term
        
        # Memory-dependent fitness with historical influence and feedback
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.07 * self.history[i] * np.sin(x[i] * 0.65) * np.cos(x[i] * 0.3)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with memory effects and dynamic peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.11 * np.sin(6.5 * x[i]) * np.cos(3.2 * x[i]) * np.exp(-0.015 * np.abs(x[i]))
        result += multi_modal
        
        return result