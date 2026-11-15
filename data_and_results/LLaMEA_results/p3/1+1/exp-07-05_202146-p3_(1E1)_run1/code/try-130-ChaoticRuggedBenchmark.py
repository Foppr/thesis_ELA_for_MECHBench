import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.73) * np.cos(i * 0.91) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with higher frequency oscillations
        for i in range(self.dim):
            result += 1.12 * np.exp(-0.35 * np.abs(x[i])) * np.sin(4.2 * np.pi * x[i])
            
        # Stronger phase coupling with dynamic weights
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.87 * np.sin(phase_sum) * np.cos(phase_sum * 1.15)
        
        # Multi-scale oscillatory terms with increased amplitude and frequency
        for i in range(self.dim):
            freq = 2.5 + 6.3 * np.sin(i * 0.52)
            amp = 1.85 + 0.67 * np.cos(i * 0.41)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.63)
            
        # Cross-dimensional interactions with stronger coupling and non-linear decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.073 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper and more numerous peaks with asymmetric ruggedness
        for i in range(self.dim):
            result += 0.29 * np.sin(17.4 * x[i]) * np.cos(9.3 * x[i]) * np.exp(-0.029 * x[i]**2)
            
        # Dynamic scaling chaotic component with variable influence
        dynamic_scale = np.sum(np.sin(x)**2) + 1.53
        result += 0.42 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.61 * dynamic_scale)
        
        # Increased high-order non-separable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.153 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Enhanced global minimum enforcing with logarithmic penalty
        result += 0.041 * np.sum(np.log(1.0 + np.abs(x)))
        
        # New global minimum attractor with complex trigonometric structure
        result += 0.19 * np.prod(np.cos(0.87 * x))
        
        # Introduce highly perturbed noise with multi-frequency components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.51 * np.sin(15.7 * x[i]) * np.cos(7.8 * x[i]) * np.exp(-0.084 * i)
        result += noise
        
        # Add time-varying basin complexity with chaotic modulation
        time_factor = np.sin(np.sum(x) * 0.21) + 1.0
        result += 0.27 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.52))
        
        # Multi-scale chaotic basin boundaries with enhanced complexity
        for i in range(self.dim):
            result += 0.35 * np.sin(11.3 * x[i]) * np.cos(5.6 * x[i]) * np.exp(-0.037 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with variable amplitudes
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.19 * np.sin(27.6 * x[i]) * np.cos(13.8 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity with modified scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.0 * x[i])
        result += 0.21 * fractal_term
        
        # Memory-dependent fitness with enhanced historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.097 * self.history[i] * np.sin(x[i] * 0.72)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with memory effects and enhanced peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.145 * np.sin(7.9 * x[i]) * np.cos(3.9 * x[i]) * np.exp(-0.018 * np.abs(x[i]))
        result += multi_modal
        
        return result