import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.42) * np.cos(i * 0.81) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with dynamic scaling
        for i in range(self.dim):
            result += 0.72 * np.exp(-0.22 * np.abs(x[i])) * np.sin(3.1 * np.pi * x[i])
            
        # Multi-scale phase interactions with time-varying coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.52 * np.sin(phase_sum * 0.75) * np.cos(phase_sum * 0.52)
        
        # Increased frequency variations and amplitude modulation
        for i in range(self.dim):
            freq = 2.1 + 4.3 * np.sin(i * 0.38)
            amp = 1.3 + 0.45 * np.cos(i * 0.28)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.38)
            
        # Stronger cross-dimensional interactions with modified decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.045 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper and more numerous peaks
        for i in range(self.dim):
            result += 0.21 * np.sin(15.3 * x[i]) * np.cos(7.8 * x[i]) * np.exp(-0.021 * x[i]**2)
            
        # Dynamic scaling with global state influence
        dynamic_scale = np.sum(np.sin(x)**2) + 1.25
        result += 0.31 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.45 * dynamic_scale)
        
        # Higher-order non-separable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.12 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Enhanced global minimum enforcing with logarithmic penalty
        result += 0.028 * np.sum(np.log(1.0 + np.abs(x)))
        
        # New global minimum attractor with complex oscillatory behavior
        result += 0.15 * np.prod(np.cos(0.65 * x))
        
        # Introduce enhanced noise with chaotic frequency components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.38 * np.sin(12.7 * x[i]) * np.cos(6.3 * x[i]) * np.exp(-0.062 * i)
        result += noise
        
        # Add dynamic basin complexity with multi-time-scale attractors
        time_factor = np.sin(np.sum(x) * 0.15) + 1.0
        result += 0.21 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.37))
        
        # Multi-scale chaotic basin boundaries with increased complexity
        for i in range(self.dim):
            result += 0.27 * np.sin(9.8 * x[i]) * np.cos(4.9 * x[i]) * np.exp(-0.027 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with increased amplitude
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.15 * np.sin(24.8 * x[i]) * np.cos(12.4 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity with stronger scaling effects
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(3.7 * x[i]) * np.cos(1.85 * x[i])
        result += 0.18 * fractal_term
        
        # Memory-dependent fitness with enhanced historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.07 * self.history[i] * np.sin(x[i] * 0.62)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with enhanced memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.11 * np.sin(6.8 * x[i]) * np.cos(3.4 * x[i]) * np.exp(-0.015 * np.abs(x[i]))
        result += multi_modal
        
        # Additional chaotic basin complexity with asymmetric scaling
        asym_factor = 1.0 + 0.3 * np.sin(np.sum(x) * 0.22)
        result += 0.18 * np.sum(np.sin(x * asym_factor) * np.cos(x * asym_factor * 0.42))
        
        # Ultra-high frequency noise component
        ultra_noise = 0.0
        for i in range(self.dim):
            ultra_noise += 0.08 * np.sin(30.1 * x[i]) * np.cos(15.0 * x[i])
        result += ultra_noise
        
        return result