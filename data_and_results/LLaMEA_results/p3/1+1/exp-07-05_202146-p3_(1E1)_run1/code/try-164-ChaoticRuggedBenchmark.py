import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.73) * np.cos(i * 0.91) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with modified coupling strengths
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.35 * np.abs(x[i])) * np.sin(3.7 * np.pi * x[i])
            
        # Stronger phase interactions with dynamic coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.15 * i))
        result += 0.83 * np.sin(phase_sum) * np.cos(phase_sum * 1.2)
        
        # Multi-scale oscillatory terms with increased frequency and amplitude variations
        for i in range(self.dim):
            freq = 2.3 + 6.7 * np.sin(i * 0.51)
            amp = 1.8 + 0.7 * np.cos(i * 0.42)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6)
            
        # Cross-dimensional interactions with stronger exponential decay and coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.07 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper and more numerous peaks with enhanced non-linearity
        for i in range(self.dim):
            result += 0.29 * np.sin(17.3 * x[i]) * np.cos(9.1 * x[i]) * np.exp(-0.028 * x[i]**2)
            
        # Dynamic scaling chaotic component with variable time factor
        dynamic_scale = np.sum(np.sin(x)**2) + 1.5
        result += 0.41 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.6 * dynamic_scale)
        
        # High-order non-separable interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        result += 0.15 * x[i] * x[j] * x[k] * x[l] * np.sin(x[i] * x[j] * x[k] * x[l])
                        
        # Global minimum enforcing with enhanced logarithmic penalty
        result += 0.04 * np.sum(np.log(1.0 + np.abs(x)))
        
        # New global minimum attractor with enhanced non-linearity
        result += 0.21 * np.prod(np.cos(0.87 * x))
        
        # Enhanced noise and perturbation components with additional chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.52 * np.sin(15.6 * x[i]) * np.cos(7.8 * x[i]) * np.exp(-0.083 * i)
        result += noise
        
        # Dynamic basin complexity with time-varying attractors and multi-scale influence
        time_factor = np.sin(np.sum(x) * 0.21) + 1.0
        result += 0.29 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.5))
        
        # Multi-scale chaotic basin boundaries with enhanced complexity
        for i in range(self.dim):
            result += 0.37 * np.sin(12.4 * x[i]) * np.cos(6.2 * x[i]) * np.exp(-0.038 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with enhanced amplitude
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.19 * np.sin(28.3 * x[i]) * np.cos(14.1 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity with increased complexity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.0 * x[i])
        result += 0.21 * fractal_term
        
        # Memory-dependent fitness with enhanced historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.093 * self.history[i] * np.sin(x[i] * 0.72)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with enhanced memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.14 * np.sin(7.9 * x[i]) * np.cos(3.9 * x[i]) * np.exp(-0.019 * np.abs(x[i]))
        result += multi_modal
        
        # Additional non-separable high-order term with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        for m in range(l+1, self.dim):
                            result += 0.08 * x[i] * x[j] * x[k] * x[l] * x[m] * np.sin(x[i] * x[j] * x[k] * x[l] * x[m])
        
        return result