import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.73) * np.cos(i * 0.91) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with dynamic scaling
        for i in range(self.dim):
            result += 1.1 * np.exp(-0.3 * np.abs(x[i])) * np.sin(3.1 * np.pi * x[i])
            
        # Multi-dimensional phase coupling with time-varying coefficients
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.7 * np.sin(phase_sum) * np.cos(phase_sum * 0.85)
        
        # Increased frequency modulation and amplitude variations
        for i in range(self.dim):
            freq = 2.3 + 5.7 * np.sin(i * 0.42)
            amp = 1.5 + 0.6 * np.cos(i * 0.31)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Cross-dimensional interactions with stronger coupling and decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.06 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper and more numerous peaks with asymmetric profiles
        for i in range(self.dim):
            result += 0.25 * np.sin(15.7 * x[i]) * np.cos(7.3 * x[i]) * np.exp(-0.022 * x[i]**2)
            
        # Dynamic scaling with global sum influence
        dynamic_scale = np.sum(np.sin(x)**2) + 1.5
        result += 0.38 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.5 * dynamic_scale)
        
        # Higher-order non-separable interactions with stronger influence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.15 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Logarithmic penalty with increased weight
        result += 0.04 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Additional global minimum attractor with complex trigonometric structure
        result += 0.18 * np.prod(np.cos(0.8 * x))
        
        # Enhanced noise components with higher frequency and amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += 0.45 * np.sin(14.3 * x[i]) * np.cos(7.1 * x[i]) * np.exp(-0.07 * i)
        result += noise
        
        # Time-varying basin complexity with stronger influence
        time_factor = np.sin(np.sum(x) * 0.18) + 1.2
        result += 0.25 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.4))
        
        # Multi-scale chaotic boundaries with increased complexity
        for i in range(self.dim):
            result += 0.3 * np.sin(10.2 * x[i]) * np.cos(5.1 * x[i]) * np.exp(-0.03 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with enhanced amplitude
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.18 * np.sin(25.6 * x[i]) * np.cos(12.8 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity with stronger scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.0 * x[i])
        result += 0.2 * fractal_term
        
        # Memory-dependent influence with stronger historical impact
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.08 * self.history[i] * np.sin(x[i] * 0.7)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with enhanced memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.12 * np.sin(7.2 * x[i]) * np.cos(3.6 * x[i]) * np.exp(-0.015 * np.abs(x[i]))
        result += multi_modal
        
        # Add a new complex multi-scale structure with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.05 + 0.15 * np.sin(i * 0.3 + j * 0.2)
                result += coupling * x[i] * x[j] * np.sin(x[i] * x[j] * 0.5)
                
        # Add a global penalty term for large values
        result += 0.03 * np.sum(np.abs(x)**3)
        
        return result